from PIL import Image
import numpy as np
import flask
import io
import json
from flask import render_template
app = flask.Flask(__name__)

    
def prepare_image(image, target):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target)
    image = np.asarray(image)
    return image

@app.route("/static/", methods=["POST"])

def predict():
    data = {"success": False}
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))
            image = prepare_image(image, target=(224, 224))
            results = str(np.sum(image))
            data["predictions"] = []
            r = {"label": results, "probability": float(0.2)}
            data["predictions"].append(r)
            data["success"] = True
            data2=json.dumps(data, sort_keys=True, indent=4)
    return flask.jsonify(data2)

if __name__ == "__main__":
    print(("* Loading  Flask starting server..."
        "please wait until server has fully started"))
    app.run()

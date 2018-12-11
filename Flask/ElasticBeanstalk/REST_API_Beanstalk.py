from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io
from skimage.transform import resize


app = flask.Flask(__name__)
model = None

def load_model():
    global model
    model = ResNet50(weights="imagenet")
    
def prepare_image(image):
    resized_image = resize(image,(224,224))
    rescaled_image = 255 * resized_image
    final_image = rescaled_image.astype(np.uint8)
    image = np.expand_dims(final_image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    return image

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}

    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            image = flask.request.files["image"].read()
            image = prepare_image(image)
            preds = model.predict(image)
            results = imagenet_utils.decode_predictions(preds)
            data["predictions"] = []
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)
            data["success"] = True
    return flask.jsonify(data)

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    load_model()
    app.run()

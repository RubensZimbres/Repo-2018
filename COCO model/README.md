# Pull Request for pycocotools library

At https://github.com/cocodataset/cocoapi

<b> Problem </b>

Incompatibility between Python 2 and Python 3 code in coco.py generating the following error:

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/COCO%20model/Pictures/COCO_evaluate_Error_unicode.png>

  
<b> Solution </b>

Replace code line 308 in coco.py:  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/COCO%20model/Pictures/COCO_change.png>  

<b> Result </b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/COCO%20model/Pictures/COCO_Success.png>

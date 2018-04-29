# Cycle GAN: Style Transfer with Deep Learning for Paintings

Repos used in this task: Wikiart (https://github.com/lucasdavid/wikiart) and CycleGAN (https://github.com/xhujoy/CycleGAN-tensorflow)

<b> Linux Wikiart Steps: </b>

git clone https://github.com/lucasdavid/wikiart

python3 wikiart.py --datadir ./wikiart-saved/ fetch --only artists

Edit .JSON file to the artists you want (see .json example in this folder)

Download datasets

python3 wikiart.py --datadir /datasets/wikiart/ fetch

<b> Python Steps: </b>

Use file open_resize.py (https://github.com/RubensZimbres/Repo-2018/blob/master/OpenCV/open_resize_IMG.py) to adjust image size that will be the input of the Cycle GAN = (256,256,3)

<b> Linux CycleGAN Steps: </b>

git clone https://github.com/xhujoy/CycleGAN-tensorflow

cd CycleGAN-tensorflow

Upload your dataset (painter) to datasets dir

Train the model: CUDA_VISIBLE_DEVICES=0 python main.py --dataset_dir=painter

(This will take 83 hours in a Tesla K-80 GPU (Amazon AWS p2.xlarge) 200 epochs, batch_size=1, 994 images)

Test your model:

CUDA_VISIBLE_DEVICES=0 python main.py --dataset_dir=painter --phase=test --which_direction=AtoB

Models are saved to ./checkpoint

In this task I transferred styles between Vincent van Gogh (B) and Pablo Picasso (A)


<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/A2BScreenshot%20from%202018-04-28%2023-24-48.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/A2BScreenshot%20from%202018-04-28%2023-25-44.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/AtoBScreenshot%20from%202018-04-28%2023-25-19.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/Screenshot%20from%202018-04-28%2023-16-06.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/Screenshot%20from%202018-04-28%2023-16-54.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/Screenshot%20from%202018-04-28%2023-17-23.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/Screenshot%20from%202018-04-28%2023-17-51.png>

<img src= https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/Screenshot%20from%202018-04-28%2023-18-26.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CycleGAN%20Project/Screenshot%20from%202018-04-28%2023-19-43.png>

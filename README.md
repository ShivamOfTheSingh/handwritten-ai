# Handwritten AI
An AI that can recognize handwritten characters trained with the mnist special database 19, made using tensorflow/keras

## Collecting data
As the dataset can only be downloaded, a data collection and formatting method was required. `data_collect.ipynb` iterates through the `by_merge` dataset and extracts all the images/labels using cv2. Afterwards, the data was randomly shuffled and stored in X (images) and y (labels).

## Creating AI
### tfai.ipynb
My first attempt at making an AI that would read the 64x64 images. Used tensorflow/keras to split and normalize the training and testing data (I used a 85-15 split). Afterwards, a neural network with 3 hidden (dense) layers of 512 nodes each was made, using the softplus activation function for the hidden layers

With 5 epochs, I achieved a loss of 0.4810 (using `sparse_categorical_crossentropy`) and an accuracy of 0.8452. The model was stored in `model` folder

## Final Details
### App
Using kivy, a front end gui was made that would input your own custom image into the model. A canvas which can be written on with a mouse was created, which would pass that canvas to the `model` folder which would then give the AI's prediction.

Sourced from https://www.nist.gov/srd/nist-special-database-19

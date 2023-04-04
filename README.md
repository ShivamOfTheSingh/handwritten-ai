# Handwritten AI
An AI that can recognize handwritten characters trained with the mnist special database 19
Made the neural network with tensorflow/keras and hadcoded my own version of it

## Collecting data
As the dataset can only be downloaded, a data collection and formatting method was required. 'data_collect.ipynb' iterates through the 'by_merge' dataset and extracts all the images/labels using cv2. Afterwards, the data was randomly shuffled and stored in X (images) and y (labels)

## Creating AI
### tfai.ipynb
My first attempt at making an AI that would read the 64x64 images. Used tensorflow/keras to split and normalize the training and testing data (I used a 85-15 split). Afterwards, a neural network with 2 hidden (dense) layers of 256 nodes each was made, using the Rectified Linear activation fucntion (ReLU) and the softmax activation function for the output nodes. With 5 epochs, I acheived a loss of 0.6147 (using 'sparse_categorical_crossentropy') and an accuracy of 0.8058.

Sourced from https://www.nist.gov/srd/nist-special-database-19

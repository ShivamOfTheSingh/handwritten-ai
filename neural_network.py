import numpy as np

class denseLayer():
    def __init__(self, input, neuronNumber):
        input_size = len(input)
        self.weights = np.random.randn(input_size, neuronNumber)
        self.bias = np.zeros((1, neuronNumber))
    def forward(self, input):
        self.output = np.dot(input, self.weights)
    
class activationReLU():
    def __init__(self, input):
        self.forward(self, input)
    def forward(self, input):
        self.output = np.maximum(0, input)
        
class activationSoftMax():
    def __init__(self, input):
        self.forward(self, input)
    def forward(self, input):
        self.output = self.normalize(input)
    def normalize(input):
        max = np.max(input, axis=1, keepdims=True)
        X = np.exp(input) - max
        rowSum = np.sum(input, axis=1, keepdims=True)
        return X / rowSum
        
        
def normalizeGreyScale(input):
    for img in input:
        for i in range(len(img)):
            img[i] /= 255
            
def prepareSquareImg(input):
    input = input.reshape(-1, len(input[0])**2)
    input = input.astype(np.float32)
    normalizeGreyScale(input)
    return input
import numpy as np

class Layer():
    pass

class Activation():
    def __init__(self, input):
        self.forward(input)
        
class Loss:
    def __init__(self, output, target, oneshot=False):
        self.calculate(output, target, oneshot)
    def calculate(self, output, target, oneshot=False):
        batchLoss = self.forward(output, target, oneshot)
        dataLost = np.mean(batchLoss)
        return dataLost

# Implementation of simple hidden dense layer
# The constuctor will automatically calculate the output values per neuron (found in self.output)
class layer_Dense(Layer):
    def __init__(self, input, neuronNumber):
        input_size = len(input[0])
        # Creates numpy array of random weights per input and intial bias of zero
        self.weights = np.random.randn(input_size, neuronNumber)
        self.bias = np.zeros((1, neuronNumber))
        self.forward(input)
    # The summation of the weights and inputs + bias (found in self.output)
    def forward(self, input):
        self.output = np.dot(input, self.weights) + self.bias

# Implementation of the Rectified Linear Unit actication function -
# -which is simpler and quicker than the sigmoid function (found in self.output)
# Putting in the input in the constuctor will automatically perform the activation
class activation_ReLU(Activation):
    def forward(self, input):
        self.output = np.maximum(0, input)

# Implementation of the softmax activation function, which will output the -
# - probabilites of each output neuron (found in self.output)
# Putting in the input in the constuctor will automatically perform the activation
class activationSoftMax(Activation):
    def forward(self, input):
        self.output = self.normalize(input)
    def normalize(self, input):
        max = np.max(input, axis=1, keepdims=True)
        X = np.exp(input - max)
        rowSum = np.sum(input, axis=1, keepdims=True)
        return X / rowSum

# The implementation of categorical cross entropy
class lossCrossEntropy(Loss):
    def forward(self, softMaxOut, target, oneshot=False):
        size = len(softMaxOut)
        softMaxOutClip = np.clip(softMaxOut, 1e-7, 1 - 1e-7)
        
        if(oneshot):
            targetCorreletion = np.sum(softMaxOutClip * target, axis=1)
        else:
            targetCorreletion = softMaxOutClip[range(size), target]
            
        crossEntropy = -np.log(targetCorreletion)
        return crossEntropy

def accuracy(softMax, target, oneshot=False):
        prediction = np.argmax(softMax, axis=1)
        accurate = np.mean(prediction == target)
        return accurate
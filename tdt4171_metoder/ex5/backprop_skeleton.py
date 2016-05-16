import math
import random
import copy


# The transfer function of neurons, g(x)
def log_func(x):
    return 1.0 / (1.0 + math.exp(-x))


# The derivative of the transfer function, g'(x)
def log_func_derivative(x):
    return math.exp(-x) / (pow(math.exp(-x) + 1, 2))


def random_float(low, high):
    return random.random() * (high - low) + low


# Initializes a matrix of all zeros
def make_matrix(i, j):
    m = []
    for i in range(i):
        m.append([0] * j)
    return m


class NeuralNet(object):  # Neural Network

    def __init__(self, num_inputs, num_hidden, learning_rate=0.001):
        # Inputs: number of input and hidden nodes. Assuming a single output node.
        # +1 for bias node: A node with a constant input of 1. Used to shift the transfer function.
        self.num_inputs = num_inputs + 1
        self.num_hidden = num_hidden

        # Current activation levels for nodes (in other words, the nodes' output value)
        self.input_activation = [1.0] * self.num_inputs
        self.hidden_activations = [1.0] * self.num_hidden
        self.output_activation = 1.0  # Assuming a single output.
        self.learning_rate = learning_rate

        # Create weights
        # A matrix with all weights from input layer to hidden layer
        self.weights_input = make_matrix(self.num_inputs, self.num_hidden)
        # A list with all weights from hidden layer to the single output neuron.
        self.weights_output = [0] * self.num_hidden  # Assuming single output
        # set them to random vaules
        for i in range(self.num_inputs):
            for j in range(self.num_hidden):
                self.weights_input[i][j] = random_float(-0.5, 0.5)
        for j in range(self.num_hidden):
            self.weights_output[j] = random_float(-0.5, 0.5)

        # Data for the backpropagation step in RankNets.
        # For storing the previous activation levels (output levels) of all neurons
        self.prev_input_activations = []
        self.prev_hidden_activations = []
        self.prev_output_activation = 0
        # For storing the previous delta in the output and hidden layer
        self.prev_delta_output = 0
        self.prev_delta_hidden = [0 for i in range(self.num_hidden)]
        # For storing the current delta in the same layers
        self.delta_output = 0
        self.delta_hidden = [0 for i in range(self.num_hidden)]

    def propagate(self, inputs):
        if len(inputs) != self.num_inputs-1:
            raise ValueError('wrong number of inputs')

        # input activations
        self.prev_input_activations = copy.deepcopy(self.input_activation)
        for i in range(self.num_inputs-1):
            self.input_activation[i] = inputs[i]
        self.input_activation[-1] = 1  # Set bias node to -1.

        # hidden activations
        self.prev_hidden_activations = copy.deepcopy(self.hidden_activations)
        for j in range(self.num_hidden):
            sum_ = 0.0
            for i in range(self.num_inputs):
                # print self.ai[i] ," * " , self.wi[i][j]
                sum_ += self.input_activation[i] * self.weights_input[i][j]
            self.hidden_activations[j] = log_func(sum_)

        # output activations
        self.prev_output_activation = self.output_activation
        sum_ = 0.0
        for j in range(self.num_hidden):
            sum_ += self.hidden_activations[j] * self.weights_output[j]
        self.output_activation = log_func(sum_)
        return self.output_activation

    def compute_output_delta(self):
        # Equation 1 from the exercise text
        p_ab = log_func(self.prev_output_activation - self.output_activation)
        # Equation 2 from the exercise text
        self.prev_delta_output = log_func_derivative(self.prev_output_activation) * (1 - p_ab)
        # Equation 3 from the exercise text
        self.delta_output = log_func_derivative(self.output_activation) * (1 - p_ab)

    def compute_hidden_delta(self):
        # Equation 4 and 5 in the exercise text
        for h in range(self.num_hidden):
            # Equation 4
            self.prev_delta_hidden[h] = log_func_derivative(self.prev_hidden_activations[h]) * self.weights_output[h] * (self.prev_delta_output - self.delta_output)
            # Equation 5
            self.delta_hidden[h] = log_func_derivative(self.hidden_activations[h]) * self.weights_output[h] * (self.prev_delta_output - self.delta_output)

    def update_weights(self):
        # Equation 6 in the exercise text, firstly for the input weights, and then for the output weights
        for weight_i in range(self.num_inputs):
            for weight_j in range(self.num_hidden):
                self.weights_input[weight_i][weight_j] += self.learning_rate * \
                                                          ((self.prev_delta_hidden[weight_j] * self.prev_input_activations[weight_i]) - \
                                                          (self.delta_hidden[weight_j] * self.input_activation[weight_i]))
        for weight_i in range(self.num_hidden):
            self.weights_output[weight_i] += self.learning_rate * \
                                             ((self.prev_hidden_activations[weight_i] * self.prev_delta_output) - \
                                              (self.hidden_activations[weight_i] * self.delta_output))

    def backpropagate(self):
        self.compute_output_delta()
        self.compute_hidden_delta()
        self.update_weights()

    # Prints the network weights
    def weights(self):
        print('Input weights:')
        for i in range(self.num_inputs):
            print(self.weights_input[i])
        print()
        print('Output weights:')
        print(self.weights_output)

    def train(self, patterns, iterations=1):
        # Backpropagate
        error_during_iterations = list()
        for iteration in range(iterations):
            for a, b in patterns:
                self.propagate(a.features)
                self.propagate(b.features)
                self.backpropagate()
            error_during_iterations.append(self.count_misordered_pairs(patterns))
        return error_during_iterations

    def count_misordered_pairs(self, patterns):
        # errorRate = numMisses/(numRight+numMisses)
        num_misses = 0
        for a, b in patterns:
            activation_a = self.propagate(a.features)
            activation_b = self.propagate(b.features)
            """
            # Not necessary due to patterns already being sorted and reversed
            if activation_a > activation_b:
                if a.rating > b.rating:
                    num_right += 1
                else:
                    num_misses += 1
            else:
                if b.rating > a.rating:
                    num_right += 1
                else:
                    num_misses += 1
            """

            if activation_a < activation_b:
                num_misses += 1

        # print(num_misses, num_right, len(patterns))
        return num_misses / len(patterns)

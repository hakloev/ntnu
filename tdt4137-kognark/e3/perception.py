import argparse
from random import uniform

parser = argparse.ArgumentParser(description="Single perceptron using step function")
parser.add_argument("-debug", "-d", dest="d", type=int, default=False, help="Debug, default=0")
parser.add_argument("-method", "-m", dest="m", default="AND", help="Training set type, default=AND")
parser.add_argument("-learningrate", "-lr", dest="lr", type=float, default=0.1, help="Learning rate for training, default=0.1")
parser.add_argument("-ephocs", "-e", dest="e", type=int, default=1000, help="Max epochs for training, default=1000")

args = parser.parse_args()

DEBUG = args.d
learning_rate = args.lr
max_p = args.e
method = args.m

threshold_limit = (-0.5, 0.5)
weight_limit = (-0.5, 0.5)

class Perceptron(object):

	or_training_sets = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)]  # OR
	and_training_sets = [((0, 0), 0), ((0, 1), 0), ((1, 0), 0), ((1, 1), 1)]  # AND
	
	def __init__(self):
		"""
		Initiate the perceptron with a random threshold and weight, but within
		the interval given from the limit tuples
		"""
		self.threshold = round(uniform(*threshold_limit), 1)
		self.weights = [round(uniform(*weight_limit), 1), round(uniform(*weight_limit), 1)]
		if DEBUG:
			print("Initiated perceptron with %s, %.1f" % (repr(self.weights), self.threshold))

	def step_sum(self, values):
		"""
		Calculate the sum of the input values and subtract the threshold
		This is equal to the dot product of the input values and subract the threshold
		"""
		return sum([Wi * Xi for Wi, Xi in zip(self.weights, values)]) - self.threshold  # More pythonic way 

	def train(self, training_set):
		learned = False
		p = 0
		previous_iteration = [[self.weights] * len(training_set)]
		while not learned:
			p += 1
			print('=' * 12)
			num_of_errors = 0
			current_iteration = []
			for inputs, Yd in training_set:
				Y = 1 if self.step_sum(inputs) >= 0 else 0 # Step 2
				e = Yd - Y
				if DEBUG: print("Inputs: %s, Yd: %d, Y: %d, e: %d" % (repr(inputs), Yd, Y, e))
				if e != 0:
					num_of_errors += 1
					self.weights = [round(Wi + (learning_rate * Xi * e), 1) for Wi, Xi in zip(self.weights, inputs)]
				current_iteration.append(self.weights)
				if DEBUG: print("Current iteration %s" % repr(current_iteration))
				print(self.weights)

			if num_of_errors == 0:
				learned = True
				print("Training converged with %d iterations needed" % (p))
				break 
			elif p >= max_p:
				print("Training reached the maximum number of epochs (%d), and terminated" % (max_p))
			elif previous_iteration == current_iteration:
				print("Training will not converge (errors exist, but it isn't able to correct it)")
				break
			previous_iteration = current_iteration

if __name__ == "__main__":
	p = Perceptron()
	if method == "OR":
		p.train(Perceptron.or_training_sets)
	else:
		p.train(Perceptron.and_training_sets)


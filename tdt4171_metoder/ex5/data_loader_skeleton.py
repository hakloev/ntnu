import backprop_skeleton as bp
from matplotlib import pyplot as plt


class DataInstance(object):
    """
    Class for holding your data - one object for each line in the dataset
    """

    def __init__(self, qid, rating, features):
        self.qid = qid  # ID of the query
        self.rating = rating  # Rating of this site for this query
        self.features = features  # The features of this query-site pair.

    def __str__(self):
        return "DataInstance - qid: " + str(self.qid) + ". rating: " + str(self.rating) + ". features: " + str(self.features)


class DataHolder(object):
    """
    A class that holds all the data in one of our sets (the training set or the testset)
    """
    def __init__(self, data_set):
        self.data_set = self.load_data(data_set)

    def load_data(self, file):
        # Input: A file with the data.
        # Output: A dict mapping each query ID to the relevant documents, like this:
        # data_set[queryID] = [dataInstance1, dataInstance2, ...]
        data = open(file)
        data_set = {}
        for line in data:
            # Extracting all the useful info from the line of data
            line_data = line.split()
            rating = int(line_data[0])
            qid = int(line_data[1].split(':')[1])
            features = []
            for elem in line_data[2:]:
                if '#docid' in elem:  # We reached a comment. Line done.
                    break
                features.append(float(elem.split(':')[1]))
            # Creating a new data instance, inserting in the dict.
            di = DataInstance(qid, rating, features)
            if qid in data_set.keys():
                data_set[qid].append(di)
            else:
                data_set[qid] = [di]
        data.close()  # The file should be closed when done processing
        return data_set


def generate_pairs(query, pattern_list):
    """
    Generates every possible pairs of the query set.
    Sorts the list by rating, then reverses it so the highest number is first
    :param query: The list of queries
    :param pattern_list: The list to return, with every pair
    :return: pattern_list
    """
    query = list(reversed(sorted(query, key=lambda x: x.rating)))
    for first_instance in range(len(query) - 1):
        for second_instance in range(first_instance + 1, len(query)):
            if query[first_instance].rating == query[second_instance].rating:
                continue
            pattern_list.append((query[first_instance], query[second_instance]))


def plot_history(*history, save=False):
    """
    Method for ploting x lists to a
    :param history: A collection of tuples on the format (list, color, label)
    :param save: Whether or not the plot should be saved
    :return: None
    """
    plt.figure(1)
    for hist, color, label in history:
        plt.plot(hist, color, label=label)
    # plt.axis([-5, len(history) + 10, min(history) - 0.001, max(history) + 0.001])
    plt.ylim(0, 1)
    plt.xlabel('Epochs')
    plt.ylabel('Error Rate')
    plt.legend()
    if save:
        plt.savefig('figures/history.png')
    else:
        plt.show(block=True)


def run_ranker(training_set, test_set, iterations=25):
    # Data holders for training- and test set
    dh_training = DataHolder(training_set)
    dh_testing = DataHolder(test_set)

    # Creating an ANN instance - feel free to experiment with the learning rate (the third parameter).
    nn = bp.NeuralNet(46, 10, 0.001)

    training_patterns = []  # For holding all the training patterns we will feed the network
    test_patterns = []  # For holding all the test patterns we will feed the network
    for qid in dh_training.data_set.keys():
        # This iterates through every query ID in our training set
        data_instance = dh_training.data_set[qid]  # All data instances (query, features, rating) for query qid
        generate_pairs(data_instance, training_patterns)

    for qid in dh_testing.data_set.keys():
        # This iterates through every query ID in our test set
        data_instance = dh_testing.data_set[qid]
        generate_pairs(data_instance, test_patterns)

    # Check ANN performance before training
    test_errors = [nn.count_misordered_pairs(test_patterns)]
    training_erros = [nn.count_misordered_pairs(training_patterns)]
    print('Starting training of Neural Net')
    for i in range(iterations):
        # Running 25 iterations, measuring testing performance after each round of training.
        # Training
        test_history_for_epoch = nn.train(training_patterns, iterations=1)
        # Check ANN performance after training.
        error_epoch_test = nn.count_misordered_pairs(test_patterns)
        error_epoch_training = nn.count_misordered_pairs(training_patterns)
        test_errors.append(error_epoch_test)
        training_erros.append(error_epoch_training)
        print('Error rate during iteration %i: %s' % (i + 1, str(error_epoch_test)))

    return test_errors, training_erros

if __name__ == '__main__':
    num_of_iterations = 1  # The number of iterations to run run_ranker (the number of neural nets to create)
    num_of_net_epochs = 20  # The number of epochs for each network to run
    complete_test_history, complete_train_history = run_ranker('data/train.txt', 'data/test.txt', iterations=num_of_net_epochs)
    for iteration in range(num_of_iterations - 1):
        test_history, train_history = run_ranker('data/train.txt', 'data/test.txt', iterations=num_of_net_epochs)
        complete_test_history = list(map(lambda x, y: x + y, complete_test_history, test_history))
        complete_train_history = list(map(lambda x, y: x + y, complete_train_history, train_history))

    complete_test_history = list(map(lambda x: x / num_of_iterations, complete_test_history))
    complete_train_history = list(map(lambda x: x / num_of_iterations, complete_train_history))

    plot_history((complete_test_history, 'b-', 'Testing'), (complete_train_history, 'r--', 'Training'))

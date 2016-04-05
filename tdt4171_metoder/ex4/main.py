from operator import itemgetter
from collections import defaultdict
from math import log2
from load import get_data
from random import random
from tree import *

TRUTH_VALUE = 2  # Global value containing the considered truth value


def b(q):
    """
    Calculates the boolean entropy for the variable q
    :param q: The value to calculate true value for
    :return: The boolean entropy for q
    """
    if q == 0 or q == 1:
        return float(0.0)
    return -(q * log2(q) + (1 - q) * log2(1 - q))


def get_true_false_classifications(examples, attribute=None, k=None):
    """
    Calculates the number of examples where the classification is True.
    If attribute and k is provided it also calculates the number of examples True for
    the given example.
    :param examples: The set of examples
    :param attribute: The attribute in question (if provided)
    :param k: The value of the attribute in question (if provided)
    :return: The count of true examples
    """
    p, n, pk, nk = 0, 0, 0, 0

    for example_dict in examples:
        if example_dict['class'] == TRUTH_VALUE:
            p += 1
            if (attribute is not None and k is not None) and (example_dict['object'][attribute] == k):
                pk += 1
        else:
            n += 1
            if (attribute is not None and k is not None) and (example_dict['object'][attribute] == k):
                nk += 1

    return p, n, pk, nk


def remainder(attribute, examples):
    """
    Calculates the expected entropy for the attribute
    :param attribute: The attribute to calculate entropy for
    :param examples: The entire example set
    :return: The expected remaining entropy for the attribute
    """
    sum_ = float(0.0)
    pn = len(examples)

    available_values_for_attribute = defaultdict(list)
    for example_dict in examples:
        available_values_for_attribute[example_dict['object'][attribute]].append(example_dict)

    # For every attribute value possible, calculate remainder for all true/negative pk/nk
    for k in available_values_for_attribute.keys():
        p, n, pk, nk = get_true_false_classifications(available_values_for_attribute[k], attribute, k)
        b_ = b(pk / (pk + nk))
        sum_ += (((pk + nk) / pn) * b_)
    return sum_


def importance(attributes, examples, random=False):
    """
    Implementation of the importance function as described on page 704 in the text book.
    Calculates the information gain for all attributes passed as the parameter 'attributes'
    :param attributes: The attributes to calculate the informationg gain for
    :param examples: The examples in question
    :param random: A flag telling if a random importance should be used
    :return: The attribute with the largest information gain
    """
    argmax_a = defaultdict(int)
    # Calculates the following for every attribute: gain(a) = b(p/p+n) - remainder(a)
    for attribute in attributes:
        if random:
            argmax_a[attribute] = random_importance_function()
            continue

        # True/False count for entire set (p and n)
        p, n, pk, nk = get_true_false_classifications(examples)
        b_ = b((p / (p + n)))
        remainder_a = remainder(attribute, examples)
        argmax_a[attribute] = b_ - remainder_a
    return max(argmax_a.items(), key=itemgetter(1))[0]


def random_importance_function():
    """
    Simple function to return a random number between 0 and 1
    To use in importance() if the random flag is set to True
    :return: A float between 0 and 1
    """
    return random()


def plurality_value(examples):
    """
    Selects the most common output value among a set of examples
    TODO: breaking ties randomly
    :param examples: The examples to check
    :return: The most common output value
    """
    common = defaultdict(int)
    for example_dict in examples:
        common[example_dict['class']] += 1
    return max(common.items(), key=itemgetter(1))[0]


def same_classification(examples):
    """
    Returns True if all examples have the same classification, and False otherwise
    :param examples: The classification examples to check
    :return: Boolean telling if it is identical or not
    """
    first_classification = examples[0]['class']
    for example_dict in examples:
        if example_dict['class'] != first_classification:
            return False
    return True


def decision_tree_learning(examples, attributes, parent_examples, random=False):
    """
    Calculates and returns the decision tree for the examples. Is purely based
    on the pseudocode on page 702 in the text book
    :param examples: The set of examples
    :param attributes: The set of attributes
    :param parent_examples: The examples from a parent branch
    :param kwargs: All additional keyword arguments (e.g the random flag passed on to importance
    :return: The decision tree
    """
    if not len(examples):
        return TreeLeaf(plurality_value(parent_examples))
    elif same_classification(examples):
        return TreeLeaf(examples[0]['class'])
    elif not len(attributes):
        return TreeLeaf(plurality_value(examples))
    else:
        # Argmax of every attribute in attributes, with use of importance
        a = importance(attributes, examples, random=random)
        new_attributes = set(attributes).difference([a])  # Hack in order to fix call-by-reference bug

        tree = Tree(a)

        available_values_for_attribute = defaultdict(list)
        for example_dict in examples:
            available_values_for_attribute[example_dict['object'][a]].append(example_dict)

        for vk in available_values_for_attribute.keys():
            exs = available_values_for_attribute[vk]
            subtree = decision_tree_learning(exs, new_attributes, examples, random=random)
            tree.add_branch(vk, subtree)
    return tree


def test(tree, data, name, print_result=True):
    """
    Function to test the number of correct classifications for a given tree
    TODO: If time, there is a bug in the test, where there is raised a KeyError
    :param tree: The tree to test
    :param data: The test data
    :param name: The name of the test
    :return: None
    """
    correctness = 0

    for test_dict in data:
        current_tree = tree
        while type(current_tree) is not TreeLeaf:
            try:
                current_tree = current_tree.children[test_dict['object'][current_tree.root]]
            except KeyError as e:
                # print('The tree could not pass the test due to a key error:\n\t'
                #      'Tried to find key %s, but available keys where: %s ' % (e, current_tree.children.keys()))
                break

        if current_tree.root == test_dict['class']:
            correctness += 1

    if print_result:
        print('Test Result for "%s": %i of %i (%.2f %%) correct classifications' % (name, correctness, len(data), (correctness / float(len(data))) * 100))
    return correctness / float(len(data)) * 100


if __name__ == '__main__':
    training_data = get_data()
    test_data = get_data(file_type='test')

    num_of_attributes = len(training_data[0]['object'])
    attr = set([i for i in range(num_of_attributes)])

    # Gain Importance Tree
    gain_tree = decision_tree_learning(training_data, attr, None)
    # print(gain_tree)
    test(gain_tree, test_data, 'gain importance')

    # Random Tree
    # random_tree = decision_tree_learning(training_data, attr, None, random=True)
    # print('\n', random_tree)
    # test(random_tree, test_data, 'random importance')

    # Test run of 500 times
    # print(sum([test(decision_tree_learning(training_data, attr, None), test_data, 'gain', print_result=False) for i in range(100)]) / 100)
    # print(sum([test(decision_tree_learning(training_data, attr, None, random=True), test_data, 'random', print_result=False) for i in range(100)]) / 100)

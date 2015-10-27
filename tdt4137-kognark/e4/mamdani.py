from interface import *
from functools import partial as apply
from operator import itemgetter
import collections


class MamdaniReasoner(FuzzyReasoner):
    """
    A class object representing a Mamdani-reasoner for Fuzzy Reasoning
    """
    def __init__(self, *args, **kwargs):
        self.limits = args
        self.fuzzy_sets = kwargs
        self.range = range(-10, 11, 1)  # -10 to 10 with step 1
        self.rules = {k: None for k in kwargs['action_set'].keys()}
        self.rule_evaluation(*args)

    def rule_evaluation(self, crisp_x1, crisp_x2):
        dist = self.fuzzy_sets['distance_set']
        delta = self.fuzzy_sets['delta_set']
        rules = self.rules

        rules['ANone'] = self.AND(dist['Small'](crisp_x1), delta['Growing'](crisp_x2))  # Rule 1 None
        rules['SlowDown'] = self.AND(dist['Small'](crisp_x1), delta['Stable'](crisp_x2))  # Rule 2 SlowDown
        rules['SpeedUp'] = self.AND(dist['Perfect'](crisp_x1), delta['Growing'](crisp_x2))  # Rule 3 SpeedUp
        rules['FloorIt'] = self.AND(dist['VeryBig'](crisp_x1), self.OR(
            self.NOT(delta['Growing'](crisp_x1)), self.NOT(delta['GrowingFast'](crisp_x2))))  # Rule 4 FloorIt
        rules['BrakeHard'] = dist['VerySmall'](crisp_x1)

    def defuzzification(self):
        action_set = self.fuzzy_sets['action_set']

        upper_value, lower_value = 0, 0

        for index in self.range:
            value, action, r = 0.0, None, index
            for rule_function, aggregate_value in zip(action_set.keys(), self.rules.values()):
                new_value = action_set[rule_function](index)
                #  print("Value for action: %s is %f" % (rule_function, new_value))
                if new_value > value:
                    action = rule_function
                    value = new_value
                    r = index

            #  print("Highest for (%d): VALUE: %f, ACTION: %s" % (r, value, action))
            upper_value += (r * self.rules[action])
            lower_value += self.rules[action]

        cog_value = upper_value / lower_value
        return self.get_action_name(cog_value), cog_value

    def get_action_name(self, value):
        action_val = [(k, v(value)) for k, v in self.fuzzy_sets['action_set'].items()]
        return max(action_val, key=itemgetter(1))[0]

    @staticmethod
    def AND(x, y):
        return min(x, y)

    @staticmethod
    def OR(x, y):
        return max(x, y)

    @staticmethod
    def NOT(x):
        return 1. - x


if __name__ == '__main__':
    # The following code is partially step 1
    # Create distance set
    distance_set = {
        'VerySmall': apply(MamdaniReasoner.reverse_grade, 1., 2.5),
        'Small': apply(MamdaniReasoner.triangle, 1.5, 3., 4.5),
        'Perfect': apply(MamdaniReasoner.triangle, 3.5, 5., 6.5),
        'Big': apply(MamdaniReasoner.triangle, 5.5, 7., 8.5),
        'VeryBig': apply(MamdaniReasoner.grade, 7.5, 9.)
    }

    # Create delta set
    delta_set = {
        'ShrinkingFast': apply(MamdaniReasoner.reverse_grade, -4., -2.5),
        'Shrinking': apply(MamdaniReasoner.triangle, -3.5, -2., -.5),
        'Stable': apply(MamdaniReasoner.triangle, -1.5, 0., 1.5),
        'Growing': apply(MamdaniReasoner.triangle, .5, 2., 3.5),
        'GrowingFast': apply(MamdaniReasoner.grade, 2.5, 4.)
    }

    # Create action set
    actions = {
        'BrakeHard': apply(MamdaniReasoner.reverse_grade, -8., -5.),
        'SlowDown': apply(MamdaniReasoner.triangle, -7., -4., -1.),
        'ANone': apply(MamdaniReasoner.triangle, -3., 0., 3.),
        'SpeedUp': apply(MamdaniReasoner.triangle, 1., 4., 7.),
        'FloorIt': apply(MamdaniReasoner.grade, 5., 8.)
    }
    actions = collections.OrderedDict(sorted(actions.items()))

    mr = MamdaniReasoner(3.4, 1.4, distance_set=distance_set, delta_set=delta_set, action_set=actions)
    action_tuple = mr.defuzzification()
    print("The robot chooses %s with value %.2f" % action_tuple)



class FuzzyReasoner(object):
    """
    The FuzzyReasoner implements the interface methods that a Fuzzy reasoner
    must implement
    """
    @property
    def AND(x, y):
        raise NotImplementedError

    @property
    def OR(x, y):
        raise NotImplementedError

    @property
    def NOT(x):
        raise NotImplementedError

    @staticmethod
    def triangle(x0, x1, x2, position=None, clip=1.):
        value = 0.0
        if x0 <= position <= x1:
            value = (position - x0) / (x1 - x0)
        elif x1 <= position <= x2:
            value = (x2 - position) / (x1 - x0)
        if value > clip:
            value = clip
        return value

    @staticmethod
    def grade(x0, x1, position=None, clip=1.):
        if position >= x1:
            value = 1.0
        elif position <= x0:
            value = 0.0
        else:
            value = (position - x0) / (x1 - x0)
        if value > clip:
            value = clip
        return value

    @staticmethod
    def reverse_grade(x0, x1, position=None, clip=1.):
        if position <= x0:
            value = 1.0
        elif position >= x1:
            value = 0.0
        else:
            value = (x1 - position) / (x1 - x0)
        if value > clip:
            value = clip
        return value

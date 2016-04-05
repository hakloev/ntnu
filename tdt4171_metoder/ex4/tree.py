class Tree(object):
    """
    Object for holding Tree branches
    """

    def __init__(self, root):
        if root is not None:
            self.root = root
        self.children = {}

    def add_branch(self, label, branch):
        self.children[label] = branch

    def __str__(self, level=0):
        """
        Inspired by http://stevekrenzel.com/articles/printing-trees
        """
        ret = '|\t' * level + '+--: %s\n' % repr(self.root)
        for k, v in self.children.items():
            ret += self.children[k].__str__(level+1)
        return ret

    def __repr__(self):
        return '<Tree-object>'

    def tree_struct(self):
        """
        In order to output graph with http://mshang.ca/syntree/
        """
        if len(self.children) == 0:
            return "[" + str(self.root) + "]"
        else:
            temp = "[" + str(self.root) + " "
        for tree in self.children.keys():
            temp += self.children[tree].tree_struct()
        return temp + "]"


class TreeLeaf(object):
    """
    Object for holding tree leafs
    """

    def __init__(self, root):
        self.root = root

    def tree_struct(self):
        return "[" + str(self.root) + "]"

    def __str__(self, level=0):
        return '|\t' * level + '|-- %s\n' % repr(self.root)

    def __repr__(self):
        return '<TreeLeaf-object>'

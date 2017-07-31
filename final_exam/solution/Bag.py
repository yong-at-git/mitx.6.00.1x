class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}

    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i) + ":" + str(self.vals[i]) + "\n"
        return s


class Bag(Container):
    def __init__(self):
        Container.__init__(self)

    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except KeyError:
            return

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        try:
            return self.vals[e]
        except KeyError:
            return 0

    def __add__(self, other):
        if isinstance(other, Bag):
            union = Bag()
            for k, v in self.vals.items():
                union.vals[k] = v
            for k, v in other.vals.items():
                if k in union.vals.keys():
                    union.vals[k] += v
                else:
                    union.vals[k] = v
            return union
        else:
            return self


class ASet(Container):
    def __init__(self):
        Container.__init__(self)

    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        try:
            del self.vals[e]
        except KeyError:
            return

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        try:
            return self.vals[e] > 0
        except KeyError:
            return False

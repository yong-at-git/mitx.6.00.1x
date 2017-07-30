def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    def is_flat(ds):
        """
        Check if the input is a flat data structure with int elements, i.e. without nested structure
        :param ds: a collection of data
        :return: true if each element in the collection is an int number
        """
        for i in ds:
            if isinstance(i, int):
                continue
            else:
                return False

        return True

    if is_flat(t):
        return max(t)

    max_of_each_child = []
    for child in t:
        if isinstance(child, int):
            max_of_each_child.append(child)
        else:
            max_of_each_child.append(max_val(child))

    return max(max_of_each_child)

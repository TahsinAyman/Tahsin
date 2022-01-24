class MyList:
    multi_set = list()
    __doc__ = """This is a Next Version of Set Class.
Here you can take Multiple Inputs

function:
    add()
    insert()
    remove()
"""

    def __init__(self, multi_set=None):
        if multi_set is None:
            self.multi_set = []

    def add(self, value=None, index=None):
        if value is None:
            pass
        elif index is None:
            self.multi_set.append(value)
        else:
            self.multi_set.insert(index, value)

    def remove(self, value):
        self.multi_set.remove(value)

    def __str__(self):
        return str(self.multi_set)

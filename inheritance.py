

class SubClass(ParentClass):
    def __init__(self, subarg=20, *args, **kwargs):
        super(ParentClass, self).__init__(*args, **kwargs)
        self.subarg = subarg



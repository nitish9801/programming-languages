#Override class initialization
# docs : https://howto.lintel.in/python-__new__-magic-method-explained/


class Foo(object):
    def __new__(cls, name,  *args, **kwargs):
        print('creating instance')
        # Returns back if instance of same class passed
        if type(name) is cls:
            return name

        # print(cls._member_names)
        # instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        instance = object.__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, name):
        self.name='Foo Class'
        print("Inside __init__")


if __name__ == '__main__':
    Foo()

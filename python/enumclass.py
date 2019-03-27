import sys
from enum import IntEnum,  Enum, EnumMeta
from types import DynamicClassAttribute

#
# class EnumParent(metaclass=EnumMeta):
#     def __new__(cls, value):
#         # all enum instances are actually created during class construction
#         # without calling this method; this method is called by the metaclass'
#         # __call__ (i.e. Color(3) ), and by pickle
#         if type(value) is cls:
#             # For lookups like Color(Color.red)
#             return value
#         # by-value search for a matching enum member
#         # see if it's in the reverse mapping (for hashable values)
#         try:
#             if value in cls._value2member_map_:
#                 return cls._value2member_map_[value]
#         except TypeError:
#             # not there, now do long search -- O(n) behavior
#             for member in cls._member_map_.values():
#                 if member._value_ == value:
#                     return member
#         raise ValueError("%r is not a valid %s" % (value, cls.__name__))
#
#     def __repr__(self):
#         return "<%s.%s: %r>" % (
#                 self.__class__.__name__, self._name_, self._value_)
#
#     def __str__(self):
#         return "%s.%s" % (self.__class__.__name__, self._name_)
#
#     def __dir__(self):
#         added_behavior = [
#                 m
#                 for cls in self.__class__.mro()
#                 for m in cls.__dict__
#                 if m[0] != '_' and m not in self._member_map_
#                 ]
#         return (['__class__', '__doc__', '__module__'] + added_behavior)
#
#     def __format__(self, format_spec):
#         # mixed-in Enums should use the mixed-in type's __format__, otherwise
#         # we can get strange results with the Enum name showing up instead of
#         # the value
#
#         # pure Enum branch
#         if self._member_type_ is object:
#             cls = str
#             val = str(self)
#         # mix-in branch
#         else:
#             cls = self._member_type_
#             val = self._value_
#         return cls.__format__(val, format_spec)
#
#     def __hash__(self):
#         return hash(self._name_)
#
#     def __reduce_ex__(self, proto):
#         return self.__class__, (self._value_, )
#
#     # DynamicClassAttribute is used to provide access to the `name` and
#     # `value` properties of enum members while keeping some measure of
#     # protection from modification, while still allowing for an enumeration
#     # to have members named `name` and `value`.  This works because enumeration
#     # members are not set directly on the enum class -- __getattr__ is
#     # used to look them up.
#
#     @DynamicClassAttribute
#     def name(self):
#         """The name of the Enum member."""
#         return self._name_
#
#     @DynamicClassAttribute
#     def value(self):
#         """The value of the Enum member."""
#         return self._value_
#
#     @classmethod
#     def _convert(cls, name, module, filter, source=None):
#         """
#         Create a new Enum subclass that replaces a collection of global constants
#         """
#         # convert all constants from source (or module) that pass filter() to
#         # a new Enum called name, and export the enum and its members back to
#         # module;
#         # also, replace the __reduce_ex__ method so unpickling works in
#         # previous Python versions
#         module_globals = vars(sys.modules[module])
#         if source:
#             source = vars(source)
#         else:
#             source = module_globals
#         members = {name: value for name, value in source.items()
#                 if filter(name)}
#         cls = cls(name, members, module=module)
#         cls.__reduce_ex__ = _reduce_ex_by_name
#         module_globals.update(cls.__members__)
#         module_globals[name] = cls
#         return cls
#
#
# def _reduce_ex_by_name(self, proto):
#     return self.name

class HelloWorld(object):
    pass

class EnumClass(Enum):
    """
    create only objects if varibale is present
    """
    CONTINUE = 100
    # CONTINUE = 100
    OK = 200


if __name__ == '__main__':
    print('hello')
    a=EnumClass(100)
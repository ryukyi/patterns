from collections import defaultdict, deque

# Define a dictionary mapping type names to their mutability status
type_mutability = {
    
    # Mutable types
    "list": True,
    "dict": True,
    "set": True,
    "defaultdict": True,  # From collections
    "deque": True,  # From collections
    "Counter": True,  # From collections
    "OrderedDict": True,  # From collections
    "namedtuple": True,  # From collections
    "UserDict": True,  # From collections.abc
    "UserList": True,  # From collections.abc
    "UserString": True,  # From collections.abc

    # Immutable types
    "int": False,
    "float": False,
    "str": False,
    "tuple": False,
    "frozenset": False,  # For immutable set-like objects
    "NamedTuple": False,  # From collections
}

# Example usage
print(type_mutability["list"])  # Output: True
print(type_mutability["int"])  # Output: False
print(type_mutability["Counter"])  # Output: True

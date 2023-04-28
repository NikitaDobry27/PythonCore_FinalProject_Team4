from collections import UserDict
from abc import ABC


class _Field(ABC):
    def __init__(self):
        raise NotImplementedError


class _Name(_Field):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class _Phone(_Field):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class _Email(_Field):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class _Birthday(_Field):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class _Record(_Field):
    raise NotImplementedError


class AddressBook(UserDict):
    pass


if __name__ == '__main__':
    ...

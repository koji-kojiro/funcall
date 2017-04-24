# -*- coding: utf-8 -*-
from __future__ import print_function


class ChainableObject(object):
    def __init__(self, value, func=lambda x: x):
        self.__value = value
        self.__func = func

    def __call__(self, *args, **kwargs):
        return ChainableObject(self.__func(self.__value, *args, **kwargs))

    def __getattr__(self, name):
        try:
            func = eval(name)
            return ChainableObject(self.__func(self.__value), func)
        except NameError:
            member = getattr(self.__func(self.__value), name)
            if callable(member):
                return ChainableObject(
                    self.__func(self.__value),
                    lambda self, *args, **kwargs: member(*args, **kwargs))
            else:
                return ChainableObject(member)

    def _(self, func):
        return ChainableObject(
            self(),
            lambda _, *args, **kwargs: func(self.__func(self.__value),
                                            *args, **kwargs))

    def map(self, func):
        return ChainableObject(self(),
                               lambda _: map(func, self.__func(self.__value)))

    def filter(self, func):
        return ChainableObject(
            self(), lambda _: filter(func, self.__func(self.__value)))

    def reduce(self, func):
        return ChainableObject(
            self(), lambda _: reduce(func, self.__func(self.__value)))

    @property
    def puts(self):
        print(self.__func(self.__value))
        return self

    def __dir__(self, *args, **kwargs):
        return dir(self.__func(self.__value))

    def __repr__(self, *args, **kwargs):
        return self.__func(self.__value).__repr__(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return self.__func(self.__value).__str__(*args, **kwargs)

    def __format__(self, *args, **kwargs):
        return self.__func(self.__value).__format__(*args, **kwargs)

    def __add__(self, *args, **kwargs):
        return self.__func(self.__value).__add__(*args, **kwargs)

    def __sub__(self, *args, **kwargs):
        return self.__func(self.__value).__sub__(*args, **kwargs)

    def __div__(self, *args, **kwargs):
        return self.__func(self.__value).__div__(*args, **kwargs)

    def __truediv__(self, *args, **kwargs):
        return self.__func(self.__value).__truediv__(*args, **kwargs)

    def __floordiv__(self, *args, **kwargs):
        return self.__func(self.__value).__floordiv__(*args, **kwargs)

    def __mod__(self, *args, **kwargs):
        return self.__func(self.__value).__mod__(*args, **kwargs)

    def __pow__(self, *args, **kwargs):
        return self.__func(self.__value).__pow__(*args, **kwargs)

    def __lshift__(self, *args, **kwargs):
        return self.__func(self.__value).__lshift__(*args, **kwargs)

    def __rshift__(self, *args, **kwargs):
        return self.__func(self.__value).__rshift__(*args, **kwargs)

    def __and__(self, *args, **kwargs):
        return self.__func(self.__value).__and__(*args, **kwargs)

    def __or__(self, *args, **kwargs):
        return self.__func(self.__value).__or__(*args, **kwargs)

    def __xor__(self, *args, **kwargs):
        return self.__func(self.__value).__xor__(*args, **kwargs)

    def __radd__(self, *args, **kwargs):
        return self.__func(self.__value).__radd__(*args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        return self.__func(self.__value).__rsub__(*args, **kwargs)

    def __rdiv__(self, *args, **kwargs):
        return self.__func(self.__value).__rdiv__(*args, **kwargs)

    def __rtruediv__(self, *args, **kwargs):
        return self.__func(self.__value).__rtruediv__(*args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        return self.__func(self.__value).__rfloordiv__(*args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        return self.__func(self.__value).__rmod__(*args, **kwargs)

    def __rpow__(self, *args, **kwargs):
        return self.__func(self.__value).__rpow__(*args, **kwargs)

    def __rlshift__(self, *args, **kwargs):
        return self.__func(self.__value).__rlshift__(*args, **kwargs)

    def __rrshift__(self, *args, **kwargs):
        return self.__func(self.__value).__rrshift__(*args, **kwargs)

    def __rand__(self, *args, **kwargs):
        return self.__func(self.__value).__rand__(*args, **kwargs)

    def __ror__(self, *args, **kwargs):
        return self.__func(self.__value).__ror__(*args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        return self.__func(self.__value).__rxor__(*args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        return self.__func(self.__value).__iadd__(*args, **kwargs)

    def __isub__(self, *args, **kwargs):
        return self.__func(self.__value).__isub__(*args, **kwargs)

    def __idiv__(self, *args, **kwargs):
        return self.__func(self.__value).__idiv__(*args, **kwargs)

    def __itruediv__(self, *args, **kwargs):
        return self.__func(self.__value).__itruediv__(*args, **kwargs)

    def __ifloordiv__(self, *args, **kwargs):
        return self.__func(self.__value).__ifloordiv__(*args, **kwargs)

    def __imod__(self, *args, **kwargs):
        return self.__func(self.__value).__imod__(*args, **kwargs)

    def __ipow__(self, *args, **kwargs):
        return self.__func(self.__value).__ipow__(*args, **kwargs)

    def __ilshift__(self, *args, **kwargs):
        return self.__func(self.__value).__ilshift__(*args, **kwargs)

    def __irshift__(self, *args, **kwargs):
        return self.__func(self.__value).__irshift__(*args, **kwargs)

    def __iand__(self, *args, **kwargs):
        return self.__func(self.__value).__iand__(*args, **kwargs)

    def __ior__(self, *args, **kwargs):
        return self.__func(self.__value).__ior__(*args, **kwargs)

    def __ixor__(self, *args, **kwargs):
        return self.__func(self.__value).__ixor__(*args, **kwargs)

    def __divmod__(self, *args, **kwargs):
        return self.__func(self.__value).__divmod__(*args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):
        return self.__func(self.__value).__rdivmod__(*args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        return self.__func(self.__value).__getitem__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        return self.__func(self.__value).__setitem__(*args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        return self.__func(self.__value).__delitem__(*args, **kwargs)

    def __missing__(self, *args, **kwargs):
        return self.__func(self.__value).__missing__(*args, **kwargs)

    def __len__(self, *args, **kwargs):
        return self.__func(self.__value).__len__(*args, **kwargs)

    def __contains__(self, *args, **kwargs):
        return self.__func(self.__value).__contains__(*args, **kwargs)

    def __iter__(self, *args, **kwargs):
        return self.__func(self.__value).__iter__(*args, **kwargs)

    def __next__(self, *args, **kwargs):
        return self.__func(self.__value).__next__(*args, **kwargs)

    def __neg__(self, *args, **kwargs):
        return self.__func(self.__value).__neg__(*args, **kwargs)

    def __pos__(self, *args, **kwargs):
        return self.__func(self.__value).__pos__(*args, **kwargs)

    def __abs__(self, *args, **kwargs):
        return self.__func(self.__value).__abs__(*args, **kwargs)

    def __invert__(self, *args, **kwargs):
        return self.__func(self.__value).__invert__(*args, **kwargs)

    def __complex__(self, *args, **kwargs):
        return self.__func(self.__value).__complex__(*args, **kwargs)

    def __int__(self, *args, **kwargs):
        return self.__func(self.__value).__int__(*args, **kwargs)

    def __float__(self, *args, **kwargs):
        return self.__func(self.__value).__float__(*args, **kwargs)

    def __round__(self, *args, **kwargs):
        return self.__func(self.__value).__round__(*args, **kwargs)

    def __ceil__(self, *args, **kwargs):
        return self.__func(self.__value).__ceil__(*args, **kwargs)

    def __floor__(self, *args, **kwargs):
        return self.__func(self.__value).__floor__(*args, **kwargs)

    def __trunc__(self, *args, **kwargs):
        return self.__func(self.__value).__trunc__(*args, **kwargs)

    def __index__(self, *args, **kwargs):
        return self.__func(self.__value).__index__(*args, **kwargs)

    def __cmp__(self, *args, **kwargs):
        return self.__func(self.__value).__cmp__(*args, **kwargs)

    def __bool__(self, *args, **kwargs):
        return self.__func(self.__value).__bool__(*args, **kwargs)

    def __copy__(self, *args, **kwargs):
        return self.__func(self.__value).__copy__(*args, **kwargs)

    def __deepcopy__(self, *args, **kwargs):
        return self.__func(self.__value).__deepcopy__(*args, **kwargs)

    def __getstate__(self, *args, **kwargs):
        return self.__func(self.__value).__getstate__(*args, **kwargs)

    def __reduce__(self, *args, **kwargs):
        return self.__func(self.__value).__reduce__(*args, **kwargs)

    def __reduce_ex__(self, *args, **kwargs):
        return self.__func(self.__value).__reduce_ex__(*args, **kwargs)

    def __enter__(self, *args, **kwargs):
        return self.__func(self.__value).__enter__(*args, **kwargs)

    def __exit__(self, *args, **kwargs):
        return self.__func(self.__value).__exit__(*args, **kwargs)


def obj(x):
    '''obj(x) -> chainable object

    Convert an object to a chainable object.

    Example
    -------
    >>> obj(10).range.filter(lambda x: x > 2).map(float).puts
    [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    This is equivelent to;
    >>> print(map(float, filter(lambda x: x > 2, range(10))))
    [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    '''
    return ChainableObject(x)

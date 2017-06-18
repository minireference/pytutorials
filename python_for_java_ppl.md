Python for experienced programmers
==================================

Part of what makes python readable is the absence of type information,
the indentation-based block structure for code, and a few Python idioms,
also known as "syntax sugar" if you will.

This tutorial assumes the reader is familiar with other programming
languages like Java and shows some examples of Python coolness.


Basic data types
----------------
The `bool`ean constants are `True` and `False`.

Strings are strings (can use both single or double quotes to denote),
floats are `float`s, and integers are `int`s (but are not fixed size).

    s = 'le string'   # can also use "le string"
    f = 1.2
    i = 3

There is also a native complex number type, should a need arise.

The `None` type is the equivalent in `null` in Java.
You can check if the variable `x`'s "null"-ness using `x is None` or `x == None`.



Tuples
------
Python syntax sometimes uses `tuple`-syntax which is any expression
separated by commas. Here is an assignment of 3 to `i` and 4 to `j` using tuple notation:

    i, j = 3, 4

A `tuple` is a fixed-length immutable structure of things separated by commas.
Tuples are denoted with brackets:

    (i, j) = (3, 4)

Lists
-----
Lists are denoted with square brackets `[3,4]` and can contain a mix of different
objects types `mylist = ['le string', 3, 4.0]`.

We use 0-based-indexing and square brackets to access tuple and list elements,
e.g. `mylist[2]` will return `4.0`.

Note: Python is forgiving about extra trailing commas in lists and tuples `[3,4,]==[3,4]`.



Dicts
-----
The main workhorse in Python is the associative array, which is called a `dict`ionary in Python.

    d = {'key1':'value1',  'key2':'value2' }
    d['key1']
    # = 'value1'

Keys are usually ints or strings, but can in fact be anything that is "hashable".


List comprehension
------------------

    nums = [1, 2, 3, 4]
    nums_doubled = [ 2*x for x in nums ]      # == [2, 4, 6, 8]

Also useful in for loops:

    for x in nums:
        print 2*x

To obtain a standard for-loop construction like in other programming languages,
with an index `i` varying over a range of values you must use the `range` function:

    for i in range(0,10):             # ==   for( int i=0; i<10; i++ )
        print i



Dict comprehension
------------------
In order to iterate over all the contents of a dictionary,
use the dictionary's `items` method:

    for key, value in d.items():
        print key
        print value

Note, that `dict` objects are not ordered. Items will come out in the order of they hash
value and may not correspond to the order in which they were inserted into the dict.
If ordering is important consider using an `OrderedDict` which can be `import`ed from `collections`.


Classes and instances
---------------------
In Python class names are usually capital letters `Person`, while instances are
lowercase `person = Person(name='Alice')`. Note there is no need to say "new";
just call the class directly.


Magic methods
-------------
Every python object conforms to some standard protocols defined in terms of
"magic methods" defined for the object.  Magic methods usually have short names,
surrounded by double underscores. For example, the `__init__` method is called
each time a new instance is created. Here is an example of a `Person` class that
takes a name as argument:

    class Person(object):
        def __init__(self, name):
            self.name = name
        def greet(self):
            return 'Hi ' + self.name

    jane = Person(name='Jane')
    jane.greet()                # 'Hi Jane'

    john = Person(name='John')
    john.greet()                # 'Hi John'


The `__str__` method is called every time the object is converted to string,
like in a print function.

Another useful double underscrore method is `__dict__` which forces the object to
represent itself as a dictionary: the objects attributes, and methods become the keys,
and the values are the values of the attributes or the output of `__repr__`.
For people used to "looking around" in objects as in JavaScript,
the `__dict__` method will prove to be invaluable.


Class inheritance
-----------------
The class `object` is the basic class for all Python objects. Suppose our application
has a base class `A` inherited from object, and `A` has two subclasses of `B` and `C`.
Suppose that class `D` extends both classes `B` and `C`.

    class A(object):
        x = 'a'

    class B(A):
        pass

    class C(A):
        x = 'c'

    class D(B, C):
        pass

Whenever we access a property of call a method for the class `D`, Python follows
the "Method Resolution Order (MRO)" to determine which class or subclass will be
called. You can view the MRO for any object using its `__mro__` method:

    D.__mro__   #  (__main__.D, __main__.B, __main__.C, __main__.A, object)

This is the order in which the class definitions will be search whenever accessing
an attribute or a method of the class `D` and its instances. Looking up the attribute `x`
of the class `D` we get the value from class `C` since it comes before class `A`:

    D.x         # 'c'


When creating a subclass, it is your responsibility to call the parent classes
methods if needed. For example, here how to define a special person subclass
with a custom `__init__` method:

    class SpecialPerson(Person):
        def __init__(self, *args, **kwargs):
            self.special = True
            super().__init__(*args, **kwargs)

    you = SpecialPerson(name='You')
    you.greet()             # 'Hi You'  comes from Person
    you.special             # True      comes from SpecialPerson
    you.__class__.__mro__   # (__main__.SpecialPerson, __main__.Person, object)

The special un-packing format for lists `*` and dictionaries `**` is used to handle
all possible input combinations of positional arguments and keyword arguments, and the  same arguments are pass to `Person.__init__`.

The call `super().__init__(*args, **kwargs)` is the short form for the longer and
more precise command `super(SpecialPerson, self).__init__(*args, **kwargs)`, which
will cause the lookup of the first method `__init__` that it finds on the classes
from the list `self.__class__.__mro__`, starting the search at `SpecialPerson` (i.e., from the beginning).


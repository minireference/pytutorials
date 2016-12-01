Python for experienced programmers
==================================

Part of what makes python readable is the absence of type information,
the indentation-based block structure for code, and a few Python idioms,
also known as "syntax sugar" if you will.

This tutorial assumes the reader is familiar with other programming 
languages like Java and shows some examples of Python coolness.

The `bool`ean constants are `True` and `False`.
Strings are strings (can use both single or double quotes to denote),
flaots are `float`s, and `int`s (grow as needed).

    s = 'le string'   # can also use "le string"
    f = 1.2
    i = 3

There is also a native complex number type, should a need arise.


Tuples and Lists
----------------
Python syntax sometimes uses `tuple`-syntax which is any expression
separated by commas. Here is an assigment of 3 to `i` and 4 to `j` using tuple notation:

    i, j = 3, 4

A `tuple` is a fixed-length immutable structure of things separated by commas.
Tuples are denoted with brackets:

    (i, j) = (3, 4)

Lists are denoted with square brackets `[3,4]` and can contain a mix of different objects `mylist = ['le string', 3, 4]`.

We use 0-based-indexing and square brackets to access tupel and list elements, e.g. `mylist[0]` will return `'le string'`.

Note: Python is forgiving about extra trailing commas in lists and tuples `[3,4,]==[3,4]` and `(3,4,)==(3,4)`.


Dicts
-----
The main workhorse in Python is the associative array, which is called a `dict`ionary in Python.

    d = {'key1':'value1',   'key2':'value2' }
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
use the dictionary's `iteritems` method:

    for key, value in d.iteritems():
        print key
        print value

Note, that `dict` objects are not ordered. Items will come out in the order of they hash
value and may not correspond to the order in which they were inserted into the dict.
If ordering is important consider using an `OrderedDict` which can be `import`ed from `collections`.



Magic methods
-------------
Every python object has some important "magin methods",
which by convention are denoted surrounded by double underscores.
The most useful of these is the `__dict__` method which forces the
object to represent itself as a dictionary: the obects attributes,
and methods become the keys, and the values are the values of the 
attributes or the output of `repr`.

For people used to "looking around" in objects as in JavaScript,
the `__dict__` method wil prove to be invaluable.

Debuggin example, say you're learning how to use a django generic `ListView`,
and after some error pages you've got a template in place and now you need
to figure out how what you can work with. The API says `get_queryset` cannot
take any arguments, but what do we have on self?  Know thyself they say:

    class SupportTaskList(ListView):
        template_name = 'support/support_task_list.html'
        def get_queryset(self):
            print self.__dict__   # looking around in completely unknown land...

Apparently `taskclass = self.kwargs['taskclass']` which means we can
find the task-specific queryset using `taskclass.model.objects.all()`.






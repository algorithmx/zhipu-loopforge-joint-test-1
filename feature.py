"""Implementation phase deliverable.

Provides the greet() function per the design interface spec.
"""


def greet(name):
    """Return a greeting for *name*.

    >>> greet("world")
    'hello world'
    """
    return "hello " + name


if __name__ == "__main__":
    print(greet("world"))

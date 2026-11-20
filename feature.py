"""feature.py — minimal greeting function for the pipeline smoke test.

Interface:
    greet(name) -> str
        Returns ``'hello ' + name``.
"""


def greet(name):
    """Return the greeting string ``'hello ' + name``."""
    return 'hello ' + name


if __name__ == '__main__':
    print(greet('world'))

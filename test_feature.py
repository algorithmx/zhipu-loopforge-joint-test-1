"""Tests for feature.greet (stdlib unittest, run via: python3 test_feature.py)."""
import unittest

from feature import greet


class TestGreet(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(greet('world'), 'hello world')

    def test_returns_exact_format(self):
        self.assertEqual(greet('managed agent'), 'hello managed agent')

    def test_concatenation_semantics(self):
        # greet must be exactly 'hello ' + name (single space, no trailing space)
        for name in ('a', 'loopforge', '设计', 'x y z'):
            self.assertEqual(greet(name), 'hello ' + name)


if __name__ == '__main__':
    unittest.main(verbosity=2)

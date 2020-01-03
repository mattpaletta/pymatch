from unittest import TestCase

from pymatch import match, pattern, Regex, etc

class TestPyMatch(TestCase):
    def test_no_patterns(self):
        result = match([], "Hello World")
        assert result is None

    def test_no_patterns_pattern(self):
        match = pattern()
        result = match("Hello World")
        assert result is None

    def test_does_not_match(self):
        result = match([
            (int, lambda i: i + 1)
            ], "Hello World")
        assert result is None

    def test_does_not_match_pattern(self):
        match = pattern((int, lambda i: i + 1))
        result = match("Hello World")
        assert result is None

    def test_match_basic_str(self):
        match = pattern((str, lambda i: "goodbye"))
        result = match("Hello World")
        assert result == "goodbye"

    def test_match_basic_int(self):
        match = pattern((int, lambda i: i + 1))
        result = match(0)
        assert result == 1

    def test_match_basic_float(self):
        match = pattern((float, lambda i: i + 1))
        result = match(0.0)
        assert result == 1.0

    def test_match_basic_bool(self):
        match = pattern((bool, lambda i: False))
        result = match(True)
        assert not result

    def test_match_regex(self):
        result = match([
            (Regex("^abc[a-z]*"), lambda i: True)
            ], "abcdefg")
        assert result

    def test_match_tuple_values(self):
        result = match([
            ((1, 2, 3), lambda i, j, k: True)
            ], (1, 2, 3))
        assert result

    def test_match_partial_tuple_values(self):
        result = match([
            ((1, 2, 3), lambda i, j, k: True)
            ], (1, 2, 4))
        assert result is None

    def test_match_no_tuple_values(self):
        result = match([
            ((1, 2, 3), lambda i: True)
            ], (4, 5, 6))
        assert result is None

    def test_match_partial_tuple_values_etc(self):
        result = match([
            ((1, 2, etc), lambda i, j, k, l, m: True)
            ], (1, 2, 6, 7, 8))
        assert result

    def test_match_tuple_types(self):
        result = match([
            ((int, int, int), lambda i, j, k: True)
            ], (1, 2, 3))
        assert result

    def test_match_partial_tuple_types(self):
        result = match([
            ((int, int, bool), lambda i, j, k: True)
            ], (1, 2, 4))
        assert result is None

    def test_match_no_tuple_types(self):
        result = match([
            ((bool, bool, bool), lambda i: True)
            ], (4, 5, 6))
        assert result is None

    def test_match_partial_tuple_types_etc(self):
        result = match([
            ((int, int, etc), lambda i, j, k, l, m: True)
            ], (1, 2, 6, 7, 8))
        assert result

    def test_first_match(self):
        result = match([
            (int, lambda i: True),
            (int, lambda i: False)
            ], 1)
        assert result

    def test_first_match(self):
        result = match([
            (int, lambda i: True),
            (any, lambda i: False)
            ], "hello")
        assert not result

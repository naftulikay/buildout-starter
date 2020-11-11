import unittest


def test_like_nose_does():
    assert 1 + 1 == 2


class TraditionalTestCases(unittest.TestCase):

    def test_traditional(self):
        self.assertEqual(1 + 1, 2)

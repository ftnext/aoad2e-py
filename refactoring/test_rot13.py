from unittest import TestCase

import rot13


class Rot13TestCase(TestCase):
    def test_does_nothing_when_input_is_empty(self):
        self.assertEqual(rot13.transform(""), "")

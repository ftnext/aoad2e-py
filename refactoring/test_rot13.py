from unittest import TestCase

import rot13


class Rot13TestCase(TestCase):
    def assertNoTransform(self, input_):
        self.assertEqual(rot13.transform(input_), input_)


class Rot13TransformTestCase(Rot13TestCase):
    def test_does_nothing_when_input_is_empty(self):
        self.assertEqual(rot13.transform(""), "")

    def test_transforms_lower_case_letters(self):
        self.assertEqual(
            rot13.transform("abcdefghijklmnopqrstuvwxyz"),
            "nopqrstuvwxyzabcdefghijklm",
        )

    def test_transforms_upper_case_letters(self):
        self.assertEqual(
            rot13.transform("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            "NOPQRSTUVWXYZABCDEFGHIJKLM",
        )

    def test_does_not_transform_symbols(self):
        self.assertNoTransform("`{@[")

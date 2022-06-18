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

    def test_does_not_transform_numbers(self):
        self.assertNoTransform("1234567890")

    def test_does_not_transform_non_english_letters(self):
        self.assertNoTransform("åéîøüçñあ")

    def test_does_not_break_when_given_emojis(self):
        self.assertNoTransform("✅🚫🙋")

    # パラメタを渡さない(JavaScriptではundefinedとなる)はPythonでは起こらないので写経しない

    def test_fails_fast_when_wrong_parameter_type_provided(self):
        # 型チェックを使うことで、このテストは不要にできるかもしれない
        with self.assertRaises(TypeError) as cm:
            rot13.transform(123)
        self.assertEqual(str(cm.exception), "Expected string parameter")

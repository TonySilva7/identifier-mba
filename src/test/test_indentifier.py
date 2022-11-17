import unittest

from src.identifier import Identifier


class IdentifierTest(unittest.TestCase):
    identifier: Identifier

    def setUp(self):
        self.identifier = Identifier()

    def test_shouldStartLetter(self):
        isTrue: bool = self.identifier.validateIdentifier("aaa")
        self.assertEqual(isTrue, True)

        isFalse: bool = self.identifier.validateIdentifier("12as")
        self.assertEqual(isFalse, False)

    def test_shouldHaveLetterOrNumber(self):
        isTrue: bool = self.identifier.validateIdentifier("a2a3")
        self.assertEqual(isTrue, True)

        isFalse: bool = self.identifier.validateIdentifier("!@#")
        self.assertEqual(isFalse, False)

    def test_shouldHaveLeastOneCharacter(self):
        isTrue: bool = self.identifier.validateIdentifier("a")
        self.assertEqual(isTrue, True)

        isFalse: bool = self.identifier.validateIdentifier("")
        self.assertEqual(isFalse, False)

    def test_shouldHaveAtMostSixCharacters(self):
        isTrue: bool = self.identifier.validateIdentifier("abc123")
        self.assertEqual(isTrue, True)

        isFalse: bool = self.identifier.validateIdentifier("adc1234")
        self.assertEqual(isFalse, False)

    def tearDown(self):
        Identifier()


if __name__ == "__main__":
    unittest.main()

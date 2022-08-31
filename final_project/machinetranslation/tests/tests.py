from . import frenchToEnglish, englishToFrench
import unittest

class TestEnglishToFrech(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),'Bonjour')
        self.assertEqual(englishToFrench(None), "null value entered")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),'Hello')
        self.assertEqual(frenchToEnglish(None), "null value entered")

unittest.main()
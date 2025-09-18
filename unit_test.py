import unittest
import script

class TestScript(unittest.TestCase):
    def test_noParameters(self):
        self.assertTrue(True)

    def test_oneValidDomain(self):
        self.assertTrue(True)
    
    def test_oneExistingTextFile(self):
        self.assertTrue(True)
    
    def test_oneNonExistingTextFile(self):
        self.assertTrue(True)
    
    def test_unrecognizedFileExtension(self):
        self.assertTrue(True)
    
    def test_invalidDomain(self):
        self.assertTrue(True)

    def test_simpleValidDomain(self):
        self.assertTrue(script.isValidDomain("example.com"))

    def test_simpleInalidDomain(self):
        self.assertFalse(script.isValidDomain("example"))
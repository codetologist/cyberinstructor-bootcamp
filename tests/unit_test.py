import unittest
import os

import script
from utils.utils import isValidDomain, fileExtensionIsSupported

class TestScriptParameters(unittest.TestCase):
    def setup(self):
        pass
    
    def test_noParameters(self):
        self.assertTrue(True)

    def test_oneValidDomain(self):
        self.assertTrue(True)
    
    def tearDown(self):
        pass

class TestDomainValidation(unittest.TestCase):
    def setup(self):
        pass

    def test_simpleValidDomain(self):
        self.assertTrue(isValidDomain("example.com"))

    def test_simpleInvalidDomain(self):
        self.assertFalse(isValidDomain("example"))
    
    def test_emptyString(self):
        self.assertFalse(isValidDomain(""))
    
    def tearDown(self):
        pass

class TestFileValidation(unittest.TestCase):
    def setup(self):
        pass

    def test_oneExistingTextFile(self):
        self.assertTrue(len(script.extractValidDomainsFromUserInput(["files/input.txt"])) == 17)
    
    def test_fullFilepath(self):
        current_directory = os.getcwd()
        print(f'Current Directory: {current_directory}')
        filepath = os.path.abspath("files/input.txt")
        print(f'Filepath: {filepath}, type: {type(filepath)}', filepath)
        filename = "input.txt"
        self.assertTrue(len(script.extractValidDomainsFromUserInput([filepath])) == 17)

    def test_oneExistingTextFileWithOneInvalidDomain(self):
        self.assertTrue(len(script.extractValidDomainsFromUserInput(["files/input4.txt"])) == 0)

    def test_oneNonExistingTextFile(self):
        self.assertTrue(len(script.extractValidDomainsFromUserInput(["files/input1.txt"])) == 0)
    
    def test_unrecognizedFileExtension(self):
        self.assertFalse(fileExtensionIsSupported("file.pdf"))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
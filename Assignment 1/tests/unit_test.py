import unittest
import os

import script
from utils.utils import isValidDomain, fileExtensionIsSupported

class TestScriptParameters(unittest.TestCase):
    @unittest.skip("Not implemented")
    def test_noParameters(self):
       #self.assertWarnsRegex(UserWarning,"Invalid command-line argument/s.", os.system("python script.py"),None)
       #self.assertWarns(UserWarning,os.system("python script.py"))
       pass

    def test_noParametersAtAll(self):
        with self.assertWarns(UserWarning) as warning_record:
            script.assingment1(["test"])
        self.assertEqual(len(warning_record.warnings), 1)
        self.assertIn("Invalid command-line argument/s.", warning_record.warnings[0].message.args[0])

    @unittest.skip("Not implemented")
    def test_oneValidDomain(self):
        self.assertTrue(True)
    


class TestDomainValidation(unittest.TestCase):

    def test_simpleValidDomain(self):
        self.assertTrue(isValidDomain("example.com"))

    def test_simpleInvalidDomain(self):
        self.assertFalse(isValidDomain("example"))
    
    def test_emptyString(self):
        self.assertFalse(isValidDomain(""))


class TestFileValidation(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
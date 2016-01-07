import unittest

from app.translator.translator import Translator


class TranslatorTests(unittest.TestCase):

    def testSetFieldnames(self):
    	fieldnames = ('COL1')
    	translator = Translator()
    	translator.setFieldnames(fieldnames)
        self.assertEqual(translator.getFieldnames(), fieldnames)

    def testSetDictionaries(self):
    	foo_dict = {"FOO": "BAR"}
    	dictionaries = {'COL1': foo_dict}
    	translator = Translator()
    	translator.setDictionaries(dictionaries)
        self.assertEqual(translator.getDictionaries(), dictionaries)

    def testTranslate(self):
    	fieldnames = ("COL1", "COL2")
    	foo_dict = {"FOO": "BAR"}
    	dictionaries = {"COL1": foo_dict}
    	expected = {'COL1': 'BAR', 'COL2': 'BAR'}
    	row = {'COL1': 'FOO', 'COL2': 'BAR'}
    	translator = Translator()
    	translator.setFieldnames(fieldnames)
    	translator.setDictionaries(dictionaries) 
    	self.assertEqual(translator.translate(row), expected)

    def runTest(self):
    	self.testSetFieldnames().run()
    	self.testSetDictionaries().run()
    	self.testTranslate().run()

def main():
    unittest.main()

if __name__ == '__main__':
    main()
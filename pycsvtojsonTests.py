import unittest
from pycsvtojson import Pycsvtojson

class PycsvtojsonTests(unittest.TestCase):

	def testExecute(self):
		oCsv = Pycsvtojson()
		oCsv.execute(['testinput.csv'])

	def runTest(self):
		self.testExecute().run()

def main():
    unittest.main()

if __name__ == '__main__':
    main()		
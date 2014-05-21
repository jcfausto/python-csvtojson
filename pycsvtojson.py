#python 3.x compatibility
from __future__ import print_function
# regular imports
import sys
import traceback
import gc
import csv
import json
from resources import FIELDNAMES, DICTIONARIES
from translator import Translator

class Pycsvtojson:

	def execute(self, argv):
		try: 
			collected = gc.collect()
			print("GCINIT:: Garbage collector: collected %d objects." % (collected))

			verbose = False

			if len(argv) > 1:
				if argv[1] == '-v':
					verbose = True

			if verbose: print("Creating translator")

			translator = Translator()
			
			if verbose: print("Translator created")

			if verbose: print("Adding dictionaries")
			translator.setDictionaries(DICTIONARIES)
			if verbose: print("Dictionaries added")	

			if verbose: print("Adding fieldnames")

			translator.setFieldnames(FIELDNAMES)
			if verbose: print("Fieldnames added")	

			inputfile = argv[0]
			if verbose: print("Input file to be readed: " + inputfile)

			if verbose: print("Openning input file")
			csvfile = open(inputfile, 'r')
			if verbose: print("Input file successfully opened")

			if verbose: print("Creating CSV reader")
			reader = csv.reader(csvfile)
			if verbose: print("CSV reader created successfully")

			if verbose: print("Creating output file")
			jsonfile = open('output.json', 'w')
			if verbose: print("Output file created")

			if verbose: print("Generating output")
			reader = csv.DictReader(csvfile, FIELDNAMES)
			for row in reader:
				translator.translate(row)
				json.dump(row, jsonfile)
				jsonfile.write('\n')
			if verbose: print("Output generated")

			if verbose: print("SUCCESS!")
			
		except KeyboardInterrupt:
			print("OK! As you wish. KeyboardInterrupt signal detected.")
		except Exception:			
			print("Unexpected error: " + traceback.format_exc())
		finally:
			collected = gc.collect()
			print("GCEND :: Garbage collector: collected %d objects." % (collected))		

# main thread
if __name__ == "__main__":
	result = Pycsvtojson().execute(sys.argv[1:])    
	sys.exit(result)

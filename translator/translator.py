class Translator:

	internalDicts = {}
	internalFieldNames = []

	def setDictionaries(self, dictionaries):		
		self.internalDicts = dictionaries

	def getDictionaries(self):
		return self.internalDicts		

	def setFieldnames(self, fieldnames):
		self.internalFieldNames = fieldnames

	def getFieldnames(self):
		return self.internalFieldNames

	def translate(self, row):
		for field in self.internalFieldNames:
			if field in self.internalDicts:
				row[field] = self.internalDicts[field][row[field]]		
		return row

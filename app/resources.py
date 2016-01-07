"""
Define here the fieldnames for each column of your CSV that will be processed
Exemple: FIELDNAMES = ("TASKID", "STATUS", "DESCRIPTION")
"""
#FIELDNAMES = ("YEAR", "MONTH", "WEEK", "BUILDID", "FAILURETYPE", "OFFENDER", "RESPONSIBLETEAM", "BUILDCATEGORY", "BUILDTYPE", "OBS")
FIELDNAMES = ("USER", "VERSION", "SYSTEM", "FULLBUILD", "STARTTIME", "ENDTIME", "DURATION", "STATUS")

"""
Create your dictionaries here.
The dictionaries will feed the translator. 
Each dictionary is a Python Dictionary that must be named with any sufix you choose
followed by the prefix "_DICT". 
Examples:
FAILURE_DICT = {"Indefinido": 0, "Mudanca RN PG5": 1, 
  "Erro Codificacao PG5": 2, "Instabilidade (VM)": 3, "Instabilidade (Rede)": 4, "Falha Metricas": 5,
  "Faltou Script BD": 6, "Erro Codificacao Testes": 7, "Erro Codificacao SG5": 8, "Estrutura": 9}
"""
TESTS_DICT = {"True": 1, "False": 0}

"""
Include your dictionaries in this collection. 
You must provide the information on a key/value style where the key must be the name of 
the column that you would like to translate and the value must be the dictionary that
contains the meanings for column values. 
Example: DICTIONARIES = {"STATUS": SOME_DICT}
"""
DICTIONARIES = {"FULLBUILD": TESTS_DICT}
=======
python-csvtojson
================

Python V2.6

Given a CSV file, it converts each row into a json formated row and outputs each row intto an output file.

Supose you have a CSV file called **input.csv** and with content like this:

"foo.bar","1.5.22","system","True",2014-05-12 16:55:18,2014-05-12 16:59:21,1800-01-01 00:00:01,0

The columns for this CSV are:
"USER", "VERSION", "SYSTEM", "FULLBUILD", "STARTTIME", "ENDTIME", "DURATION", "STATUS"

So, all you need to do is to edit "resources.py" and:

1. Add to "FIELDNAMES" this columns.

You are ready to go. 

Go to your command prompt/terminal and type: Python pycsvtojson.py input.csv

You will notice that a file called **output.json** was created with the parsed data.

** Translate CSV column values when creating the json record **

Supose you want to replace the values in "FULLBUILD" to other values in your json record.

All you need to to is to edit "resources.py" and:

1. Create a dictionary containning your key/value pairs, where key is the "value" in "FULLBUILD" column to be replaced with "value"
2. Add this dictionary to "DICTIONARIES" linked with the column that it represents. i.e: DICTIONARIES = {"FULLBUILD": FULLBUILD_DICT}

Run the script again and you should get your desired results. 

+++++++
Tests
+++++++

You should run the test before using the script. 

Python pycsvtojsonTests.py
Python translatorTests.py

Feel free to contribute (look at the TO-DO below), comment or to open issues.

+++++++
TO-DO
+++++++

1. Organize the tests
2. Improve the main method in order to add more robustness
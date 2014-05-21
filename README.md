=======
python-csvtojson
================

### Status
[![Build Status](https://travis-ci.org/jcfausto/python-csvtojson.svg?branch=master)](https://travis-ci.org/jcfausto/python-csvtojson)

Given a CSV file, this module converts each row into a row with json format and outputs them to an output file

Supose you have a CSV file called **input.csv** with content like this:

```
"foo.bar","1.5.22","system","True",2014-05-12 16:55:18,2014-05-12 16:59:21,1800-01-01 00:00:01,0
```

The columns for this CSV are:

```
"USER", "VERSION", "SYSTEM", "FULLBUILD", "STARTTIME", "ENDTIME", "DURATION", "STATUS"
```

So, all you need to do is to edit **resources.py** and add this columns to ***FIELDNAMES*** dictionary.

At this point you are ready to go. 

Go to your command prompt/terminal and type: 

```
Python pycsvtojson.py input.csv
```

You will notice that a file called **output.json** will be created with the parsed data.

### Translate CSV column values when creating the json record

Supose you want to replace the values that the "FULLBUILD" column have by other values in your json parsed record.

All you need to to is to edit **resources.py** and do the following:

1. Create a dictionary containning your *key/value* pairs, where *key* is the "value" in "FULLBUILD" column that you want to translate to a value.

2. Add this dictionary to **DICTIONARIES** linked with the column that it represents and for wich it will be the base for translation. Example: DICTIONARIES = {"FULLBUILD": FULLBUILD_DICT}

Run the script again and you should get your desired results in the output file.


### Tests

You could run the tests locally before using the script by typing: 

- Python pycsvtojsonTests.py

- Python translatorTests.py

If you have *nose* you just need to type *nosetests* and all tests will run.

### License

Feel free to use all the code here as you like.

Would you like to contribute? Feel free too! :-) 

Any questions drop me a line!

### TO-DO

1. Organize the tests
2. Improve the main method in order to add more robustness

#### References

- Garbage Collection: http://www.digi.com/wiki/developer/index.php/Python_Garbage_Collection

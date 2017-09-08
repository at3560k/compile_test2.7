#!/bin/bash

#pyinstaller compiletest/compiletest.py
#pyinstaller compile_test.spec

# the below, res('resource', 'resource.txt') works
#pyinstaller --add-data 'compile_test/resource.txt:.' compile_test/compile_test.py


# the below, res('resource', 'fubar/resource.txt') works
pyinstaller --add-data 'compile_test/resource.txt:fubar' compile_test/compile_test.py

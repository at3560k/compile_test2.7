#!/bin/bash

#pyinstaller compiletest/compiletest.py
#pyinstaller compile_test.spec
pyinstaller --add-data 'compile_test/resource.txt:.' compile_test/compile_test.py

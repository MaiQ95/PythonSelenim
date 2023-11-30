# PythonSelenim
## Automate Website operations with Selenium Framework


## Folder description:
```
Page objects:
Web.py - write site elements location (by: id, XPATH, name, CSSselector)

TestData:
WebData.py - add every data to check for or print on website

tests:
conftest.py - set default browser and browser service
test_Web.py - example project

utilities:
BaseClass.py - add your functions here
```

## CMD commands:
```
For all test files:
cd C:\Users\...\Selenium
py.test -v -s

For single test:
cd C:\Users\...\tests
py.test test_Web.py -v -s
```

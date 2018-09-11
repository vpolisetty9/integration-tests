# cardinal-qa-tests

# Cardinal Hire QA Automation Repository

## Python Setup
1. Install python 3.7.0 version
2. pip3.7 install --user pipenv
installs pip and virtualenv under $HOME/Library/Python/3.7/bin
3. create python virtual env: virtualenv venv
4. source venv/bin/activate
5. Install the following python modules:
```pip install requests
pip install selenium
pip install sauceclient
pip install Appium-Python-Client
pip install pytest
```

## IDE Setup
1. Install Pycharm or intellj IDE (need to install Python plugin from marketplace)
2. Select the python from your venv as your python interpreter

## Automation Framework
1. Framework Directory Structure:

```
src
    framework : Framework  / config related classes
    pages : Page classes that define page elements
    helpers : Reusable helper classes that perform actions on page elements
    tests : Test classes that define test methods for each use cases
```

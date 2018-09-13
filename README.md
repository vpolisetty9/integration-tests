# cardinal-qa-tests

# Cardinal Hire QA Automation Repository

## Python Setup
1. Install python 3.7.0 version from 
https://www.python.org/downloads/release/python-370/
https://www.python.org/downloads/windows/
2. `pip3.7 install --user pipenv`
installs pip and virtualenv under $HOME/Library/Python/3.7/bin
3. create python virtual env: `python3 -m virtualenv venv`
4. Activate the virtual env: `source venv/bin/activate`
5. Install the following python modules in the virtual env:
```pip install requests
pip install selenium
pip install sauceclient
pip install Appium-Python-Client
pip install pytest
```
## Chromedriver setup
1. Download chromedriver compatible version equivalent with selenium driver.
https://chromedriver.storage.googleapis.com/index.html

## IDE Setup
1. Install Pycharm (http://www.jetbrains.com/pycharm/) or intellj IDE (need to install Python plugin from marketplace)
2. Select the python from your venv as your python interpreter

## How to run tests
In progress

## Automation Framework
1. Framework Directory Structure:

```
src
    framework : Framework  / config related classes
    pages : Page classes that define page elements
    helpers : Reusable helper classes that perform actions on page elements
    tests : Test classes that define test methods for each use cases
```

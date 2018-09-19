# cardinal-qa-tests

# Cardinal Hire QA Automation Repository

## Python Setup
1. Install python 3.7.0 version from 
https://www.python.org/downloads/release/python-370/
https://www.python.org/downloads/windows/
2. `pip3.7 install --user pipenv`
Installs pip and virtualenv under $HOME/Library/Python/3.7/bin
3. Create python virtual env: `python3 -m virtualenv venv`
4. Activate the virtual env: `source venv/bin/activate`
5. Install the following python modules in the virtual env `venv`:
```
pip install requests
pip install selenium
pip install sauceclient
pip install Appium-Python-Client
pip install pytest
pip install allure-pytest
```
Note:`pip list` will give the list of installed modules 

## Chromedriver setup
1. Download chromedriver compatible version equivalent with selenium driver.
https://chromedriver.storage.googleapis.com/index.html
2. Set the chromedriver in system path -- Download chromedriver and paste in to usr/local/bin

Note: https://sites.google.com/a/chromium.org/chromedriver/downloads

## IDE Setup
1. Install Pycharm (http://www.jetbrains.com/pycharm/) or intellj IDE (need to install Python plugin from marketplace)
2. Select the python from your venv as your python interpreter

## How to run tests
1. Run from commandline: 
    - Activate the virtual env: `source venv/bin/activate`
    - pytest <test_name>
2. Run from IDE

## Reporting
Allure Reporting -- https://docs.qameta.io/allure/#_python
1. Install Allure on the local machine : `https://docs.qameta.io/allure/#_installing_a_commandline`
2. Run tests with Allure in venv : 
    - Activate the virtual env: `source venv/bin/activate`
    - `pytest --alluredir=<results_dir> src/tests/search_test.py`
    Eg: `pytest --alluredir=ch_results src/tests/search_test.py`
3. Generate Local Allure report in `venv`: 
    - `allure serve <results_dir>`
    Eg: `allure serve ch_results`

## Automation Framework
1. Framework Directory Structure:

```
src
    framework : Framework  / config related classes
    pages : Page classes that define page elements
    helpers : Reusable helper classes that perform actions on page elements
    tests : Test classes that define test methods for each use cases
```

## WIP
1. Screenshots
2. Multi browser support 
3. Logging 
4. Mobile browser support


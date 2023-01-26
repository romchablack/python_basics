# interactive window - do not close after execution
python -i

# Create virtual environment
python.exe -m venv d:\Projects\venvs\demoenv310

# Open venv
C:\Users\romch>cd d:\Projects\venvs\demoenv310

# Check Python version
python.exe --version


# Check list of modules installed
pip list

# Install library
pip install selenium

# Add chromedriver to PATH (user variable)
%USERPROFILE%\projects\drivers


>>> from selenium import webdriver
>>> browser = webdriver.Chrome()

"""
FIND ELEMENET
""" 

$$("input[id='ipt1']")

$$("") - CSS selector
$x("//button") - XPATH

$x("//p[contains(text(), 'Edit Profile')]")

# Find by ID
div[@id='id1']
div#id1 # the same as above

"//button[text()='Import']"
"//p[text()='Edit Profile']"
$x("//label[contains(text(),'Total Wealth')]")[0]

Go UP 1 level: ".."
$x("//b[text()='Product 1']/..")

### ALert ###

from selenium.webdriver.common.alert import Alert

alert = Alert(browser)
print(alert.text)
alert.accept()

### Tabs ###

# define how many tabs are opened

browser.window_handles 
# switch between opened tabs
handels = browser.window_handles
browser.swith_to.window(handels[0])

# Frame

browser.switch_to.frame(iframe)
iframe = browser.find_element(By.CSS_SELECTOR, 'iframe')
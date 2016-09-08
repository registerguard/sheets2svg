import re
import lxml.etree as etree
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set vars
url = raw_input("Please paste URL of interactive chart after it's been published: ")
#url = "https://docs.google.com/spreadsheets/d/1codr6C_jxrXkcRmCIb2ao6XVG5qzdu_vYw3ObTWh2mo/pubchart?oid=1723669337&format=interactive"
filename = raw_input("Desired file name (make sure extenstion is '.svg'): ")
#filename = "example.svg"

# Set up selenium
# See: http://selenium-python.readthedocs.io/api.html?highlight=chrome#module-selenium.webdriver.chrome.webdriver
driver = webdriver.Chrome('/Applications/chromedriver')  # Optional argument, if not specified will search path.
driver.get(url)
sleep(5) # Pause and allow Google JS to render
svg = driver.find_element_by_tag_name('svg').get_attribute('outerHTML') # Get SVG
driver.quit()

# Get rid of Google bits that dork AI
# See: https://docs.python.org/2/library/re.html#re.sub
svg = re.sub(r'\s?clip-path="url\(https:\/\/docs.google.com\/spreadsheets\/d\/[a-zA-Z0-9_]+\/pubchart\?oid=[0-9]+&amp;format=interactive#_ABSTRACT_RENDERER_ID_0\)"', r'', svg)

# Parse using lxml
# See: http://stackoverflow.com/a/749839
# See: http://lxml.de/tutorial.html
svg = etree.fromstring(svg)
# Format using lxml
svg = etree.tostring(svg, pretty_print = True) 

# Write to a file
# See: https://learnpythonthehardway.org/book/ex16.html
target = open(filename, 'w')
target.write(svg)
target.close()

# Load the packages
import requests
from bs4 import BeautifulSoup

# Defining the url of the site
base_site = "https://en.wikipedia.org/wiki/Music"

# Making a get request
response = requests.get(base_site)
response.status_code

# Extracting the HTML
html = response.content

# Checking that the reply is indeed an HTML code by inspecting the first 100 symbols
#html[:100]

# Convert HTML to a BeautifulSoup object. This will allow us to parse out content from the HTML more easily.
# Using the default parser as it is included in Python
soup = BeautifulSoup(html, "html.parser")

# It is extremely useful to be able to check this file when searching where some info is located
# or to see how was the document parsed

# Exporting the HTML to a file
with open('Wiki_response.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))


# the 'with' statement is shorthand for a 'try-finally' block
# open is function for opening/creating a file to edit
# the 'wb' argument signifies the mode in which to edit the file - Writing in Bytes format
# .prettify() modifies the HTML code with additional indentations for better readability
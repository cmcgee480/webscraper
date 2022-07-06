# webscraper1

This is the web scraper project I was tasked with completing as part of my application for the Software Engineer role at Travelnest.

I decided to tackle this problem using Python3, as the company uses this language in their day to day workflows.
I was tasked with web scraping the property title, property type, number of bedrooms, bathrooms and the list of amenities from 3 AirBnB properties listed on 3 webpages.
One of the links wasn't working correctly and didn't bring me to a specific listing, so I continued on with the other 2 urls.

I am very new to the Python language so I decided it would be a new and rewarding challenge to quickly research how to accomplish this task using a language not quite as fiamiliar to me. 

Firstly I created a Python virtual environment and project to store the script files and project dependencies, which can be viewed in the requirements.txt file in the venv folder.
Next I researched the best method to employ when web scraping with Python. This is where I came across Beautiful Soup 4. I realised rather quickly the key to scraping a web page
was to do so by parsing the web pages' html code.

Learning this, I moved onto importing Requests and Beautiful Soup 4 into the Python project. Requests is a Python library used to send HTTP transfer requests to specific URLS.
Using a HTTP GET request it retrieves the HTML data that the server sends back and stores that data in a Python object.
The next step to take was to scan over the resulting HTML code from each of the AirBNB pages and pinpoint the specific HTML tags and elements that contained the data I was requested to gather.

By creating a Beautiful Soup object with the variable name soup I could then use the objects methods to pull text from various div classes, headers, ids and list elements and display
them in the terminal by simply printing the output.


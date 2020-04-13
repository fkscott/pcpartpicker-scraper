## pcpartpicker-scraper
converts pcpartpicker lists into csv files
you will need bs4 (beautifulsoup) to run `testscraping.py`
    - to install using pip: `pip install bs4`

# whats working
`testscraping.py` parses the contents of `pcpartpicker-test-page.html` into plain text creating a csv with columns for the component type, component name, and price of the component

# whats not working
1. pull links to merchants from `pcpartpicker-test-page.html`
2. request data from live webpages

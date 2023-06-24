# Text called JavaScript Object Notation that allows Python to work with JavaScript data
import json

# An HTTP library that allows the user to send HTTP requests to Python
import requests

# A package that allows the user to parse HTML and XML documents to assist in web scraping
from bs4 import BeautifulSoup

# A function that provides access to gain data from Google News
def get_nbanews_data():

    # HTTP headers allow the client and server to pass information with a request or response
    headers = {
        
        # The "User-Agent" header is included within the "requests" package
        "User-Agent":

        # A user agent string that belongs to the Google Widget Server, a library used to perform HTTP requests
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }

    # The "requests" package obtains a URL with a response from the headers with the "get" method
    # The URL leads to the news section of the web search for "nba news"
    response = requests.get(
        "https://www.google.com/search?q=nba+news&rlz=1C5CHFA_enUS919US919&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjw6sK3hdj_AhU5lWoFHSQjBXQQ_AUoAXoECAQQAw&biw=1440&bih=789&dpr=2", headers=headers
    )

    # A variable is created as BeautifulSoup parses HTML documents along with information from the requests package
    soup = BeautifulSoup(response.content, "html.parser")

    # Creates a variable for the news list
    news_results = []

    # A for loop with the variable "info" allows "soup" to select a section with the division tag on the webpage that encompasses all of the news articles
    for info in soup.select("div.SoaBEf"):
        
        # A detailed list with web scraping methods for various article information
        news_results.append(

            # The inspect element on webpages allowed the division tags to be easily located and pasted in code
            # The "find" method allows for a hypertext (href) to be located while the "select_one" method takes all of the listed information from each article
            {
                "link": info.find("a")["href"],
                "title": info.select_one("div.MBeuO").get_text(),
                "description": info.select_one("div.GI74Re.nDgy9d").get_text(),
                "date": info.select_one("div.LfVVr").get_text(),
                "source": info.select_one("div.MgUUmf.NUnG9d").get_text()
            }
        )
 
    # Prints in the order of the variable "news_results" with an indent for aesthetic
    print(json.dumps(news_results, indent=2))
 
# Call the main function at the end in order to allow the program to execute
get_nbanews_data()
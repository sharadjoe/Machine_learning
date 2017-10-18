from bs4 import BeautifulSoup
import urllib2
 
quote_page = 'http://www.foodnetwork.co.uk/recipes/easy-pan-roasted-chicken-and-shallots.html'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
instructions = soup.find("div", itemprop="recipeInstructions")
print(instructions.get_text(strip=True))
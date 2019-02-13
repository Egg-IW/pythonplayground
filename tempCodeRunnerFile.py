from bs4 import BeautifulSoup
import requests

word = input("What word would you like to search on the dictionary?")

source = requests.get(
    'https://www.vocabulary.com/dictionary/{}'.format(word)).text
thing = BeautifulSoup(source, "html.parser")
defintion = thing.find('div', class_="ordinal first").div.h3.a

print(defintion.prettify())

from bs4 import BeautifulSoup
import requests

while True:
    try:
        word = input("What word would you like to search on the dictionary?")
        break
    except AttributeError:
        print("Try again, you may have entered a word that doesn't exist..")
        word = input("What word would you like to search on the dictionary?")

source = requests.get(
    'https://www.vocabulary.com/dictionary/{}'.format(word)).text
thing = BeautifulSoup(source, "html.parser")
definition = thing.find('div', class_="ordinal first").div.h3.text
#definition2 = thing.find('div', id_="s24648").div.h3.text
definition = ' '.join(definition.split())
#definition2 = ' '.join(definition2.split())


print(definition.strip())
# print(definition2.strip())

import bs4 as bs
import nltk
from nltk.corpus import stopwords
import requests
import re


scrapped_data = requests.get('https://en.wikipedia.org/wiki/Natural_language_processing')
article = scrapped_data.text
parsed_article = bs.BeautifulSoup(article, 'html.parser')

paragraphs = parsed_article.find_all('p')
#print(paragraphs)

article_text = ''

for p in paragraphs:
    article_text += p.text

article_text = re.sub(r'\[[0-9]]*\]' , ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
#print(formatted_article_text)

stop_words = set(stopwords.words('english'))
word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stop_words:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = [word_frequencies[word] / maximum_frequency]

print(max(word_frequencies.values()))

import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

response=urllib.request.urlopen('https://en.wikipedia.org/wiki/Tata_Group')
html=response.read()
# print(html)

soup=BeautifulSoup(html,'html5lib')
text=soup.get_text(strip=True)
# print(text)

tokens=[t for t in text.split()]
# print('TOKENS',tokens)

sr=stopwords.words('english')
clean_tokens=tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
# print('Cleaned Tokens',clean_tokens)

import matplotlib.pyplot as plt
freq=nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key)+':'+str(val)) 
freq.plot(20,cumulative=False)
plt.show()   


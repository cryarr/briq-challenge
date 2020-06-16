import urllib.request
import spacy 
import json
import numpy as np
import random

random.random()

nlp = spacy.load("en_core_web_lg")
print("Loaded NLP")


##loads all quotes into a json object, extracts the quote only so it can be appended to a list
## that way we can easily iterate over the quotes
def getQuotes():
    page = urllib.request.urlopen('https://programming-quotes-api.herokuapp.com/quotes')
    data = json.load(page)
    datalist = []
    for quote in data:
        datalist.append(quote['en'])
        
    return datalist

#random quote analysis with the nlp package from spacy
## prints the quote with the highest similarity value to the selected random quote
## uses nlp tokenizer to get the words into vectors and compare the similarity with similarity() 
def randomQuoteAnalysis(quotelist):
    num = random.randrange(len(quotelist))
    randQuote = quotelist[num]
    print("Random quote that was selected: " + randQuote)
    randQuoteTokens = nlp(randQuote)
    simscore = 0
    current = 0
    prev = 0
    highestSimilarityQuote = ""
    for quote in quotelist:
        current=0
        compareQuoteTokens = nlp(quote)
        for randtokens in randQuoteTokens:
            for comptokens in compareQuoteTokens:
                current += randtokens.similarity(comptokens)
        if prev < current:
            highestSimilarityQuote = quote
            print("highest was found with similarity of " + str(current))
            simscore = current
        prev = current
   
    print("Highest quote similarity to:\n " + randQuote + " is \n " + highestSimilarityQuote)



####main
quotelist = getQuotes()
randomQuoteAnalysis(quotelist)

import urllib.request
import spacy 
import json
import numpy as np
import random

random.random()

nlp = spacy.load("en_core_web_lg")
print("Loaded NLP")

def getQuotes():
    page = urllib.request.urlopen('https://programming-quotes-api.herokuapp.com/quotes')
    data = json.load(page)
    datalist = []
    for quote in data:
        datalist.append(quote['en'])
        
    return datalist


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

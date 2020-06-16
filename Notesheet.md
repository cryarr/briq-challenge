# Notesheet

# 1st iteration
- Vue.js  
    - found that everything is related by a .vue file that acts similarly to a html file, with a little bit of handlebars mixed in
    - For some reason custom components won’t work when doing <template> and new vue
    - Vuetify does a star rating, can use the event that it fires to call the analysis function
    <v-rating v-model="rating" @input="getAnalysis(event, rating.id)"/>
    - defined in rating.vue, however has an error in the overall App.vue. Installed dev tools but even that wont work
    - Chrome might be the issue here
    - Custom components still not working. Rating is showing up and looks like it is firing the event but the input is not seeing the actual 
- tensorflow.js
    - Only worked in TS for some reason? tried to get it in js but couldn’t find any resources
    - Cosine distance seems to be a way to deal with semantic similarity
    - Theres also leven distance
    - Dont think i need a distance functions as they may not calculate the sentiment of the word/string but only the distance between the two as far as how similar they may be in characters. 
# 2nd iteration
- React.js
    - too large to understand at first 
    - Tried to clone from previous project, But several packages broke. Could not continue due to too much time lost trying to fix redundancies
    - Think that react was overall the best way to go but there was just too much of a time sink
    - Had the best overall plan but there was not a really nice way to do a star rating system. Felt like vue had that really easily implemented. Just couldn’t get the components to communicate with each other
# 3rd iteration
- Angular
    - Found tutorial for doing sentiment in tensorflow js with angular
    - It is in typescript and found that it doesn’t actually have anything to do with semantic similarity. I dont actually know if that is the problem i am trying to discover either
- Angular js
    - Packages could not be found?? way too many package errors and issues found 
    - again not enough time to fully understand and get a product out
- Think this is not the way to goo.


# 4th iteration
- I think i am going to try to get a working analysis in python as that is the best way i feel i can get something done and outputted and also show my skills
- NLP packages to explore
    - Spacy
        - Have used spacy before in ML, seems like the best NLP package. want to at least try this way because I want to gain better experience overall. I feel like this is the best way to learn from this.
    - sklearn 
    - semmatch?
- implementation
    - Spacy has a NLP() that tokenizes the string up into its specific words (check on this to verify it is correct)
    - iterate over each token matching it to the other token. doing token.similarity() on each word
    for token in randomQuote:
      for compareToken in compareQuote:
        similarityscore += token.similarity(compareToken)
    - think this will work? Similarity looks to output the exact similarity. Add up the similarity score, take the quote with the highest similarity score
    - Ran a few tests. looks like the random quote with the chosen quote seems to output a similar quote 
- More time?
    - really want to run a full classification algorithm on this. Like split the dataset up into specific classifications based on the quote. Run a support vector machine on it, transform it into a hyperplane and do a full sentiment analysis. 
    - Could also do a random forest, generate bag of words to get a basic classifier
    - Maybe train a NN with BERTA, want to look more at the tensorflow packages as they may have better analysis, but due to lack of time and due to lack of knowledge I could not explore more. 
    - What is the NLP problem of matching string similarity. What is the math behind it, because lots of the distance functions don’t seem to account for sentiment. 
        - I think maybe another way to cache sentiment for specific words might be to match words that have 


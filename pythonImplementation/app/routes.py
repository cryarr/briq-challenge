from app import app
from flask import render_template, flash, redirect
from app import spacyver
import random
from app import starform

random.random()
##setup quick routing to index page
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'] )

def index():
    quotelist = spacyver.getQuotes()
    num = random.randrange(len(quotelist))
    randquote=quotelist[num]
    form = starform.rating()
    #have form done and random quote selected

    ## for some reason the submission is always false, not sure why
    print(form.validate_on_submit())
    if form.validate_on_submit():
        ##this should be getting a new value AFTER POST. But i think it might be happeneing too fast?
        print('GETTING NEW QUOTE')
        flash('getting new quote')
        if (int(form.rating.data) >=4 ):
            simquote = spacyver.randomQuoteAnalysis(randquote, quotelist)
            return render_template('index.html', quote=simquote, form=form, randorSim='Similar')
        else:
            return render_template('index.html', quote=randquote, form=form, randorSim='random')
    return render_template('index.html', quote=randquote, form=form, randorSim='random')

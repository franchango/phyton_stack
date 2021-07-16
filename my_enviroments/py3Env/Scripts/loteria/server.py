import os
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'kljasldjlaskjdlkasjdlkjasdlkj'
def getrandomnum():
    import random
    return random.randint(1, 100)

@app.route('/')
def gamesetup():
    #new game always starts with tiles hidden.
    startdisplay = "block"
    errordisplay = "none"
    windisplay = "none"
    lowdisplay = "none"
    highdisplay = "none"
    currandom = 0
    session['gameon'] = False
    return render_template('index.html', startdisplay=startdisplay,
                           errordisplay=errordisplay, windisplay=windisplay,
                           lowdisplay=lowdisplay, highdisplay=highdisplay,
                           currandom=currandom)

@app.route('/checknumbers', methods=['post'])
def checknumbers():
    if session['gameon'] is True:
        print ("29 for gameon = ", session['gameon'])
        currandom = int(session['random'])
        print ("31 currrandom is ", currandom)
        print ("32 got post: gameon was: ", session['gameon'])
        print (request.form)
    elif session['gameon'] is False:
        print ("35 got post: gameon was: ", session['gameon'])
        print (request.form)
        session['gameon'] = True
        print ("38 set gameon to", session['gameon'])
        session['random'] = int(getrandomnum())
        currandom = int(session['random'])
        print ("41 === CurRandom was just reset ===", currandom)

    #get the guess from the user input
    print ("44 === got request form ===: ", request.form)
    try: 
        guess = int(request.form['guess'])
        if currandom == guess:
            print ("48 --- currandom = ", currandom, " and guess = ", guess, " ---")
            startdisplay = "none"
            print ("50 ---startdisplay = ", startdisplay)
            errordisplay = "none"
            print ("52---errordisplay = ", errordisplay)
            windisplay = "block"
            print ("54---windisplay = ", windisplay)
            lowdisplay = "none"
            print ("56---lowdisplay = ", lowdisplay)
            highdisplay = "none"
            print ("58---highdisplay = ", highdisplay)
            session['gameon'] = False
            return render_template('index.html', startdisplay=startdisplay,
                                   errordisplay=errordisplay, windisplay=windisplay,
                                   lowdisplay=lowdisplay, highdisplay=highdisplay,
                                   currandom=currandom)
        elif currandom > guess:
            print ("64--- currandom = ", currandom, " and guess = ", guess, " ---")
            startdisplay = "none"
            print ("66---startdisplay = ", startdisplay)
            errordisplay = "none"
            print ("68---errordisplay = ", errordisplay)
            windisplay = "none"
            print ("70---windisplay = ", windisplay)
            lowdisplay = "block"
            print ("72---lowdisplay = ", lowdisplay)
            highdisplay = "none"
            print ("74---highdisplay = ", highdisplay)
            session['gameon'] = True
            print ("76 session gameon = ", session['gameon'])
            return render_template('index.html', startdisplay=startdisplay,
                                   errordisplay=errordisplay, windisplay=windisplay,
                                   lowdisplay=lowdisplay, highdisplay=highdisplay,
                                   currandom=currandom)
        elif currandom < guess:
            print ("81 --- currandom = ", currandom, " and guess = ", guess, " ---")
            startdisplay = "none"
            print ("83 ---startdisplay = ", startdisplay)
            errordisplay = "none"
            print ("85---errordisplay = ", errordisplay)
            windisplay = "none"
            print ("87---windisplay = ", windisplay)
            lowdisplay = "none"
            print ("89---lowdisplay = ", lowdisplay)
            highdisplay = "block"
            print ("91---highdisplay = ", highdisplay)
            session['gameon'] = True
            print ("93 session game on is ", session['gameon'])
            return render_template('index.html', startdisplay=startdisplay,
                                   errordisplay=errordisplay, windisplay=windisplay,
                                   lowdisplay=lowdisplay, highdisplay=highdisplay,
                                   currandom=currandom)
    except:
        startdisplay = "none"
        errordisplay = "block"
        windisplay = "none"
        lowdisplay = "none"
        highdisplay = "none"
        session['gameon'] = True
        session['random'] = currandom
        return render_template('index.html', startdisplay=startdisplay,
                               errordisplay=errordisplay, windisplay=windisplay,
                               lowdisplay=lowdisplay, highdisplay=highdisplay,
                               currandom=currandom)

@app.route('/reset', methods=['post'])
def reset(): 
    startdisplay = "block"
    errordisplay = "none"
    windisplay = "none"
    lowdisplay = "none"
    highdisplay = "none"
    session['gameon'] = False
    return render_template('index.html', startdisplay=startdisplay,
                           errordisplay=errordisplay, windisplay=windisplay,
                           lowdisplay=lowdisplay, highdisplay=highdisplay)


app.run(debug=True)
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    print('*'*100)
    print('counter working')
    if 'count' in session:
        session['count'] += 1
    else:    
        session['count'] = 0
    
    return render_template('index.html')

@app.route('/reset', methods = ['POST'])
def reset():
    print('*'*100)
    print('resetting counter to 0')
    session['count']= -1
    return redirect('/')

@app.route('/add_2', methods = ['POST'])
def add_2():
    print('*'*100)
    print('adding 2')
    session['count']+=1
    return redirect('/')

@app.route('/destroy', methods = ['POST'])
def destroy():
    print('*'*100)
    print('sessions destroyed')
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
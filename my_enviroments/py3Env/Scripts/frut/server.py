from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    blackberry = int(request.form['blackberry'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    amount = strawberry + raspberry + apple + blackberry
    student_id = request.form['student_id']
    return render_template("checkout.html",strawberry = strawberry, raspberry = raspberry,
     apple = apple, blackberry = blackberry, first_name = first_name, last_name = last_name, student_id = student_id,amount = amount)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
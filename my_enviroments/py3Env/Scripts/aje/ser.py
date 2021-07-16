from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def checkerboard():
    print('*'*100)
    print("root route good!")
    return render_template("checkerboard.html")

@app.route("/<x>")
def checkerboard2(x):
    print('*'*100)
    print("num route good!")
    return render_template("checkerboard.html", x = int(x), y = 8)

@app.route("/<x>/<y>")
def checkerboard3(x, y):
    print('*'*100)
    print("num route good!")
    return render_template("checkerboard.html", x = int(x), y = int(y))

if __name__=="__main__":
    app.run(debug = True)
from flask import Flask, render_template,request
from process import lang_pro
app = Flask(__name__)
@app.route('/')
def home():
  return render_template("index.html")

@app.route('/',methods=["POST",'GET'])
def home1():
  if request.method=="POST":
    text=request.form["text"]
    get=request.form["get"]
    sentence=lang_pro(text,get)
    return render_template("index.html",sentence=sentence)

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")

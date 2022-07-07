from flask import Flask, render_template

app=Flask(__name__,template_folder='template')

@app.route('/')

def index():
    k="iheb"
    t=["a","b","c"]
    stuff ="this a Bold "
    return render_template("index.html",f=k,stuff1=stuff,t=t)
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",name1=name)
@app.errorhandler(404)
def pager(e):
    return render_template("404.html"),404
@app.errorhandler(500)
def pager(e):
    return render_template("500.html"),500
if __name__ =="__main__":
    app.run(debug=True)

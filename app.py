from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"


@app.route("/about")
def about():
    return "This is about page"


########## dynamic route

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/employee/<name>/<department>")
def employee(name,department):
    return f"Hello {name} {department}"




if __name__ =="__main__":
    app.run(debug=True)
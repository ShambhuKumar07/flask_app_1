from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"



############ URL converter ############

@app.route("/user/<id>") ## except all data type
def user(id):
    return f"Hello {id}"

@app.route("/user_int/<int:id>") ## except only integer data type
def user_int(id):
    return f"Hello {id}"



if __name__ =="__main__":
    app.run(debug=True)
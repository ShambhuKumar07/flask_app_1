from flask import Flask,request

app=Flask(__name__)

@app.route("/search")
def search():
    # name=request.args.get("name")
    name=request.args.get("name","Guest") # defaul value
    dep=request.args.get("dep","Unknown") # defaul value
    return f"Hello {name} your department is {dep}"

if __name__ =="__main__":
    app.run(debug=True)
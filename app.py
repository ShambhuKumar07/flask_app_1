from flask import Flask,request,render_template

app=Flask(__name__)

############ single data pass

# @app.route("/")
# def home():
#     name="Shambhu"
#     return render_template("index.html",name=name)

################## multiple data pass

@app.route("/")
def home():
    courses=["python","Flask","Django","NumPy","Pandas"]
    
    
    return render_template("index.html",courses=courses)

if __name__ =="__main__":
    app.run(debug=True)
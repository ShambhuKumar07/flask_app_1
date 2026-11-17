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
    # is_loged_in=True
    is_loged_in=False
    return render_template("index.html",is_loged_in=is_loged_in)

if __name__ =="__main__":
    app.run(debug=True)
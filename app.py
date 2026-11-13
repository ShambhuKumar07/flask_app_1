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
    name="Shambhu"
    age=27
    city="New Delhi"

    return render_template("index.html",
                           name=name,
                           age=age,
                           city=city)


if __name__ =="__main__":
    app.run(debug=True)
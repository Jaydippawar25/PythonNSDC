from flask import Flask ,request, render_template ,jsonify
app= Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data",methods=["POST"])
def data():

    name = request.form.get("name")
    age = request.form.get("age")

    result =f"Hello {name}, your age is {age}"
    return render_template("index.html",result=result)
if __name__ == "__main__":
    app.run(debug=True)
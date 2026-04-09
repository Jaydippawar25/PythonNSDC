from flask import Flask ,request,jsonify
app= Flask(__name__)
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    response ={
        "message":f"Hello {name} , your age is : {age}"
    }
    return jsonify(response)
if __name__ == "__main__":
    app.run(debug=True)
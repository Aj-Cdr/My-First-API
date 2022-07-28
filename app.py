from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
{
    "Id":1, 
    "Contact": "9495432755",
    "Name": "Raju",
    "Done": False
}, 
{
    "Id":2,
    "Contact": "9495727612",
    "Name": "Ben",
    "done": False
},
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json: 
        return jsonify({
            "Status": "Error", 
            "Message": "Please provide the data"
        }, 400)
    task={
    "Id": tasks[-1]["id"]+1, 
    "Name": request.json["Name"],
    "Contact": request.json.get("Contact", ""),
    "done": False
    }
    tasks.append(task)
    return jsonify({
        "Status": "Success",
        "Message" : "Task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

if __name__ == "__main__":
    app.run(debug = True)
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label" : "My first task", "done" : False},
]

allowed_keys = ["label", "done"]

@app.route('/todos', methods=['GET'])
def get_todos():
    print("Holaaa")
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    if "label" not in request_body or "done" not in request_body:
        return jsonify({"error": "Incorrect body format"}), 400

    # Me quedo solo con las keys que necesito para mantener el formato del JSON
    filtered_data = {key: request_body[key] for key in allowed_keys if key in request_body}
    todos.append(filtered_data)

    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=["DELETE"])
def delete_todo(position):
    if position >= len(todos):
        return jsonify({"error" : "Index out of range"}), 400
    
    del todos[position]
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
from flask import Flask, request, jsonify

app = Flask("server")
fruits = ['peach', 'banana', 'ananas']


@app.route("/fruits")
def get_fruits():
    return jsonify(fruits)


@app.route("/fruits", methods=['POST'])
def add_fruit():
    body = dict(request.json)
    fruit = body["fruit"]
    if fruit in fruits:
        return jsonify({
            "success": False,
            "error": "we have such fruit already"
        })

    fruits.append(fruit)
    return jsonify({"success": True})


@app.route("/fruits", methods=['DELETE'])
def delete_fruit():
    body = dict(request.json)
    fruit = body["fruit"]

    if fruit in fruits:
        fruits.remove(fruit)
        return jsonify({"succes": True})

    return jsonify({"success": False, "error": "no such fruit in a list"})

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

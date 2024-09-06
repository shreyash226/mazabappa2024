from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received alert: {data}")

    if 'Buy' in data['message']:
        print("Buy")
    elif 'Sell' in data['message']:
        print("Sell")

    return jsonify({"message": "Alert received"}), 200


if __name__ == '__main__':
    app.run(debug=True)

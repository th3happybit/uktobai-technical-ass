from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to calculate the sum of the numbers
@app.route('/sum', methods=['POST'])
def sum_numbers():
    try:
        data = request.get_json()
        numbers = data['numbers']

        if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
            return jsonify({"error": "Invalid input. Please provide a list of numbers."}), 400

        result = sum(numbers)
        return jsonify({"sum": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to concatenate the strings
@app.route('/concatenate', methods=['POST'])
def concatenate_strings():
    try:
        data = request.get_json()
        string1 = data['string1']
        string2 = data['string2']

        if not isinstance(string1, str) or not isinstance(string2, str):
            return jsonify({"error": "Invalid input. Please provide two strings."}), 400

        result = string1 + string2
        return jsonify({"concatenated": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

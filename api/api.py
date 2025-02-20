#
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run_function', methods=['POST'])
def run_function():
    data = request.json
    input_value = data.get('input_value')
    # Your function logic here
    result = your_function(input_value)
    return jsonify({'result': result})

def your_function(input_value):
    # Replace this with your actual function logic
    return f"Processed {input_value}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
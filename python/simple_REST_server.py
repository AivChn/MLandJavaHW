from flask import Flask, jsonify, Response

# Amishav Cohen

app = Flask(__name__)

data = [{
    'People': [
        {'Name': 'Amishav', 'Age': 19, 'ID': 123456789},
        {'Name': 'Ron', 'Age': 290, 'ID': 999999999}
    ]
}]

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({'Greet': f'Hi, {name}!'})

@app.route('/data/<idx>', methods=['GET'])
def get_data(idx: int):
    if int(idx) > len(data[0]['People']):
        return Response('Index Out Of Bounds', status=400)
    return jsonify({'data': data[0]['People'][int(idx)]})

if __name__ == '__main__':
    app.run(debug=True)

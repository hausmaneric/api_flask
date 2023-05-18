from flask import Flask, jsonify
import pandas as pd

data = pd.read_json('caminho/para/o/arquivo.json')

app = Flask(__name__)

@app.route('/dados', methods=['GET'])
def get_dados():
    return jsonify(data.to_dict())

if __name__ == '__main__':
    app.run()

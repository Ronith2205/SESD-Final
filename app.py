from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Default route
@app.route('/')
def home():
    return jsonify({"message": "Backend is running successfully!"})

# Example expense API
@app.route('/api/add-expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    print("Received Expense:", data)
    return jsonify({"status": "success", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




@app.route('/healthz')
def health():
    return jsonify({"status": "ok"})
return jsonify({"message": "Backend is LIVE and auto-deploy working!"})



from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Backend is LIVE and auto-deploy working!"})

@app.route('/healthz')
def health_check():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


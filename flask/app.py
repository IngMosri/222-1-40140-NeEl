from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def mensaje():
    return "flask server running"

@app.route("/api/message")
def api():
    return 'Vue JS running with flask :D'

if __name__ == "__main__":
    app.run(debug=True)
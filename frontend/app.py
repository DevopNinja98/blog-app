from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Blog Frontend - DevOps Portfolio</h1><p>Built by CloudNinja98</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my first applicatio, Hello amma"

@app.route('/api/hello')
def hello():
    return {"message": "Hello, Docker!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask App"

@app.route('/about')
def about():
    return "About Page"

# 🌟 NEW FEATURE
@app.route('/version')
def version():
    return "Version 3 - Feature branch added (version info page)"

if __name__ == "__main__":
    app.run(debug=True)
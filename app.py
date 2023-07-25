from flask import Flask, render_template

app = Flask(__name__)

students = []

@app.route("/")
def index():
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True, port=8888)
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)

@app.route('/<title>')
def main(title):
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def index(prof):
    status = False
    if 'инженер' in prof or 'строитель' in prof:
        status = True
    print(status)
    return render_template('index.html', status=status)

@app.route('/<title>')
def main(title):
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

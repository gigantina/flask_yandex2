from flask import Flask, request, render_template

app = Flask(__name__)
prof_list = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
             'климатолог', 'специалист по радиационной защите',
             'астеоролог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
             'штурман', 'пилот дронов']


@app.route('/list_prof/<list_>')
def index(list_):
    if list_ == 'ol':
        li = 0
    elif list_ == 'ul':
        li = 1
    else:
        li = -1
    return render_template('index.html', status=li, prof_list=prof_list)


@app.route('/<title>')
def main(title):
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

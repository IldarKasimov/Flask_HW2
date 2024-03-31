# Задание №9
# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя и
# произведено перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)
app.secret_key = b'5f2143e98128e3f549546221265e4'


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return redirect(url_for('logout'))
    if 'username' in session:
        context = {'name': session['username']}
        return render_template('hello.html', **context)
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['email'] = request.form.get('email')
        return redirect(url_for('hello'))
    return render_template('form_task_9.html')


@app.route('/logout/')
def logout():
    session.pop('username')
    session.pop('email')
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run(debug=True)

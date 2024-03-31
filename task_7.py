# Задание №7
# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом,
# где будет выведено введенное число и его квадрат.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_num():
    if request.method == 'POST':
        number = request.form.get('number')
        return redirect(url_for('result', number=number))   # перенаправление на страницу с результатом
    return render_template('form_number.html')


@app.route('/result/<number>')
def result(number):
    return f'Результат выражения: {number}² = {int(number) ** 2}'


if __name__ == '__main__':
    app.run()
from django.shortcuts import render
from flask import Flask, render_template
from random import sample

app = Flask(__name__)  # app 이라는 이름을 가진 Flask 클래스의 객체 생성


# @app.route('/')
# def hello_world():
#     return 'Hello, Pearl! Enjoy!'

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/hello')
def hello_hello():
    return 'HELLO HELLO BABE!!'


@app.route('/greeting/<string:name>')
def greeting(name):
    return f'Nice to meet you. {name}!'


@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'The cube of {num} is {result}'


@app.route('/dinner/<int:people>')
def dinner(people):
    menu = ['steak', 'chicken', 'pizza', 'hamburger', 'Jaeyuk-bokkeum', 'pasta',
            'pork belly', 'K-BBQ', 'pork ribs', 'black noodles', 'ramen', 'salmon', 'stew', 'HUs', 'clamchawder']
    return f'{sample(menu, people)}'


@app.route('/show')
def show():
    menu = ['steak.jpg', 'chicken.jpg', 'pizza.jpg', 'hamburger.jpg', 'Jaeyuk-bokkeum.jpg', 'pasta.jpg',
            'pork-belly.jpg', 'K-BBQ.jpg', 'pork-ribs.jpg', 'black-noodles.jpg', 'ramen.jpg', 'salmon.jpg', 'stew.jpg', 'HUs.jpg', 'clamchawder.jpg']
    pickme = ''.join(sample(menu, 1))
    return render_template('index.html', food_img=pickme)


if __name__ == "__main__":
    app.run(debug=1)  # 객체의 run함수를 이용하여 로컬 서버에서 앱 실행

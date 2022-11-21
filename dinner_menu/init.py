from django.shortcuts import render
from flask import Flask, render_template
from random import sample
import math

app = Flask(__name__)  # create an object 'app' of Flask class


# @app.route('/')
# def hello_world():
#     return 'Hello, Pearl! Enjoy!'

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/hello')
def hello_hello():
    return 'HELLO HELLO This is for you to choose your dinner menu! Enjoy!'


@app.route('/greeting/<string:name>')
def greeting(name):
    return f'Nice to meet you. {name}!'


@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'The cube of {num} is {result}'


@app.route('/trigonometric/cos/<string:num>')
def cosine(num):
    result = math.cos(int(num))
    return f'The cos({num}) is {result}'


@app.route('/trigonometric/sin/<string:num>')
def sine(num):
    result = math.sin(int(num))
    return f'The sin({num}) is {result}'


@app.route('/trigonometric/tan/<string:num>')
def tangent(num):
    result = math.tan(int(num))
    return f'The tan({num}) is {result}'


@app.route('/dinner/<int:ran>')
def dinner(ran):
    menu = ['steak', 'baked chicken', 'pizza', 'hamburger', 'Jaeyuk-bokkeum', 'pasta',
            'pork belly', 'K-BBQ', 'pork ribs', 'black noodles', 'ramen', 'salmon', 'stew', 'HUs', 'clamchawder']
    return f'{sample(menu, ran)}'


@app.route('/dinner/show')
def show():
    menu = ['steak.jpeg', 'baked-chicken.webp', 'pizza.webp', 'hamburger.webp', 'Jaeyuk-bokkeum.jpeg', 'pasta.jpeg',
            'pork-belly.jpeg', 'k-bbq.jpeg', 'pork-ribs.webp', 'black-noodles.jpeg', 'ramen.jpeg', 'salmon.jpeg', 'stew.webp', 'hus.webp', 'clamchawder.jpeg']
    pickone = ''.join(sample(menu, 1))
    return render_template('dinner.html', food_img=pickone)


if __name__ == "__main__":
    app.run(debug=1)  # 객체의 run함수를 이용하여 로컬 서버에서 앱 실행

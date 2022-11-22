from django.shortcuts import render
from flask import Flask, render_template, request
from random import sample
import math

app = Flask(__name__)  # create an object 'app' of Flask class


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


@app.route('/trigonometric/cos', methods=['post'])
def cosine():
    cosval = request.form['cosval']
    cosres = math.cos(int(cosval))
    return render_template('calculator.html', name="cos", value=cosval, result=cosres)


@app.route('/trigonometric/sin', methods=['post'])
def sine():
    sinval = request.form['sinval']
    sinres = math.sin(int(sinval))
    return render_template('calculator.html', name="sin", value=sinval, result=sinres)


@app.route('/trigonometric/tan', methods=['post'])
def tangent():
    tanval = request.form['tanval']
    tanres = math.tan(int(tanval))
    return render_template('calculator.html', name="tan", value=tanval, result=tanres)


@app.route('/dinner/<int:ran>')
def dinner(ran):
    menu = ['steak', 'baked chicken', 'pizza', 'hamburger', 'Jaeyuk-bokkeum', 'pasta',
            'pork belly', 'K-BBQ', 'pork ribs', 'black noodles', 'ramen', 'salmon', 'stew', 'HUs', 'clamchawder']
    return f'{sample(menu, ran)}'


@app.route('/dinner/show')
def show():
    menu = ['steak.jpeg', 'baked-chicken.webp', 'pizza.webp', 'hamburger.webp', 'Jaeyuk-bokkeum.jpeg', 'pasta.jpeg',
            'pork-belly.jpeg', 'k-bbq.jpeg', 'pork-ribs.webp', 'black-noodles.jpeg', 'ramen.jpeg', 'salmon.jpeg', 'stew.webp', 'hus.webp', 'clamchawder.jpeg']
    picked_menu = ''.join(sample(menu, 1))
    return render_template('dinner.html', food_img=picked_menu)


if __name__ == "__main__":
    app.run(debug=1)

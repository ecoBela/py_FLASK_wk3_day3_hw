from app import app
from modules import calculator

@app.route('/')
def index():
    return "Hello, World! Are we ready?!"

@app.route('/add/<num1>/<num2>')
def add_my_numbers(num1, num2):
    add(num1, num2)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')

        if operation == 'sumar':
            result = num1 + num2
        elif operation == 'restar':
            result = num1 - num2
        elif operation == 'multiplicar':
            result = num1 * num2
        elif operation == 'dividir':
            result = num1 / num2 if num2 != 0 else 'Error: División por cero'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

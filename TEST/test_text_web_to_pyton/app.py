from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    input_text = request.form['input_text']
    # Do something with the input text
    print("Input text:", input_text)
    # You can store it in a variable, database, or perform any other operation.
    return " "


if __name__ == '__main__':
    app.run(debug=True)

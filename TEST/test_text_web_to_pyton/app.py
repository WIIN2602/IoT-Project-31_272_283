# from flask import Flask, request, jsonify

# app = Flask(__name__)


# @app.route('/process_text', methods=['POST'])
# def process_text():
#     data = request.get_json()
#     text = data.get('text', '')

#     # Process the text (for example, you can print it)
#     print("Received text:", text)

#     # You can do some processing here and return a response
#     processed_text = text.upper()  # Example: Convert text to uppercase
#     return jsonify({'result': processed_text})


# if __name__ == '__main__':
#     app.run(debug=True)  # Run the Flask app


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    input_text = request.form['input_text']
    # Do something with the input text
    print("Input text:", input_text)
    # You can store it in a variable, database, or perform any other operation.
    return "Text received: " + input_text


if __name__ == '__main__':
    app.run(debug=True)

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


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # Pass data to the template if needed
    message = "Hello, World!"
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('checkin/index.html')

# @app.route('/checkin')
# def checkin():
#     return render_template('checkin.html', rooms=available_rooms)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        DateCheckIn = request.form['DateCheckIn']
        DateCheckOut = request.form['DateCheckOut']
        Adult = request.form['adult']
        children = request.form['child']
    #     result = f'Check-In date is {DateCheckIn} check-Out date is {DateCheckOut} \nHave adult {Adult} and child {children}'
    # return result


if __name__ == '__main__':
    app.run(debug=True)

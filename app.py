from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask says Hello World'


@app.route('/test')
def test():
    return 'This is just a test case'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask import Flask
import re

app = Flask(__name__)
regex = re.compile(
        r'^((http|https|)?://)?'
        r'(([0-9]{1,3}\.){3}[0-9]{1-3})|'
        r'(((www\.)?[0-9a-z][0-9a-z-]{0,61})?[0-9a-z]\.'
        r'[a-z]{2,6})(:[0-9]{1,4})?'
        r'((/?)|(/[0-9a-z_!~*\'().:?;@&=+$,%#-]+)+/?)$',
        re.IGNORECASE)



@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/new/<path:url>')
def validate(url):
    if re.search(regex, url) is not None:
        return url
    else:
        return "Invalid URL"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/Blog/')
def Blog():
    return render_template('Blog.html')                
@app.route('/About Us/')
def About_Us():
    return render_template('About_us.html')
@app.route('/Contact us/')
def Contact():
    return render_template('Contact.html')

if __name__ == "__main__":
    app.run(debug=True)
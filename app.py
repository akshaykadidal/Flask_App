from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/product')
def products():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(debug=True)
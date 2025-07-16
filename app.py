from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f'New message from {name} ({email}): {message}')
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

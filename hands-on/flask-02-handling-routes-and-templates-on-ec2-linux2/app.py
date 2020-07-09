from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
@app.route ('/')
def home():
    return 'this is home page, <h1> WELCOME HOME</h1>'
@app.route ('/about')
def about():
    return '<h1> This is my "about page" </h1>'
@app.route('/error')
def error():
    return '<h1> you got error</h1>'
@app.route('/hello')
def hello():
    return '<h1> HELLO WORLD</h1>'
@app.route('/admin')
def admin():
    return redirect(url_for('error'))
# @app.route('/<name>')
# def greet(name):
#    greet_format= f"""
# # <!DOCTYPE html>
# # <html>
# # <head>
# #     <title>Greeting Page</title>
# # </head>
# # <body>
# #     <h1>Hello, { name }!</h1>
# #     <h1>Welcome to my Greeting Page</h1>
# # </body>
# # </html>
# #    """
#    return greet_format
    
@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name='Master Admin!'))
@app.route('/<username>')
def greet(username):
    return render_template('greet.html', name=username)
@app.route('/list10')
def list10():
    return render_template('list10.html')
@app.route('/evens')
def evens():
    return render_template('evens.html')
if __name__ == '__main__':
    #app.run(debug=True)
    app.run('0.0.0.0', port = 80)

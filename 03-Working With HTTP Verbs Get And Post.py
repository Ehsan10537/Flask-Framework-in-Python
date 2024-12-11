# overall, there are 4 types of HTTP verbs, GET, POST, PUT, and DELETE
# in the route() functions we have another parameter called 'methods' which is set to 'GET' by default.
# therefore, we have been using the 'GET' methods so far. we hit the url, and get the content back from the server.

from flask import Flask, render_template, request

# request is a Flask object provided by the framework to represent the current HTTP request being processed. 
# When a user interacts with your website (e.g., submits a form, clicks a link, or sends a request),
# Flask creates a request object containing all the relevant information.

app = Flask(__name__)
"""
it creates an instance of the Flask class,
which will be your WSGI application
"""

@app.route('/')
def welcome():
    if request.method == 'GET':
        return "<html><H1>Welcome to this Flask course Ehsan. Have fun bro</H1><html>"
    # as you can see you can even use this condition which is by default being used because the default method would be 'GET'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=["GET", 'POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f"Hi dear {name} Welcome to the form page honey!!!"
    if request.method == 'GET':
        return render_template('form.html')

# render_template() searchs for a folder called "templates" in the directory and redirects to the html file we have provide
# so we have to create our html pages inside the 'templates' folder in the directory.
# it uses the Jinja 2 protocol to do this

if __name__ == '__main__':
    app.run(debug=True)

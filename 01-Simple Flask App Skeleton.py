from flask import Flask

app = Flask(__name__)
"""
it creates an instance of the Flask class,
which will be your WSGI application
"""

@app.route('/')
def welcome():
    return "Welcome to this Flask course. This is the home page."

@app.route('/index')
def index():
    return "This is the index page."

if __name__ == '__main__':
    app.run(debug=True)



# READ THESE FIRST:

# Flask Framework
"""
It's a lightweight and popular web framework for Python that allows you to build web applications quickly and easily.
"""
# What is WSGI?
"""
WSGI stands for Web Server Gateway Interface, 
and it is a specification that acts as a bridge between a web server and your web application
"""
# Why is WSGI needed?
"""
* Web browsers make requests (e.g., when you open a webpage), and web servers (like Nginx or Apache) receive these requests. 
* The web server doesn't know how to run Python applications directly, so it uses WSGI to communicate with your Python application.
"""
#### How WSGI works in Flask?
"""
Flask includes a built-in WSGI server called Werkzeug for development purposes.
When a request comes in:
1) The web server hands over the request details to WSGI.
2) WSGI passes these details to your Flask application.
3) Your Flask app processes the request and sends a response (like an HTML page) back to WSGI.
4) WSGI gives the response back to the web server, which then delivers it to the user's browser.

Think of WSGI as a translator ensuring that the web server and your Python code understand each other.
"""


# What is Jinja2?
"""Jinja2 is a templating engine used in Flask to create dynamic web pages."""

# Why is Jinja2 needed?
"""
* A regular HTML page is static, meaning it shows the same content every time.
* With Jinja2, you can insert dynamic data into your HTML, making it more interactive.
"""

# How Jinja2 works?
"""
* You create an HTML template file and use Jinja2's syntax to add placeholders for dynamic content.
* Flask uses Jinja2 to replace those placeholders with real data before sending the page to the user's browser.

SO, Jinja2 is a tool for making dynamic HTML pages by mixing static HTML with dynamic Python data.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>Welcome to this Flask course. This is the home page</H1><html>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# render_template() searchs for a folder called "templates" in the directory and redirects to the html file we have provide
# so we have to create our html pages inside the 'templates' folder in the directory.
# it uses the Jinja 2 protocol to do this

if __name__ == '__main__':
    app.run(debug=True)


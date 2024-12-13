from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def welcome():
    if request.method == 'GET':
        return "<html><H1>Welcome to this Flask course Ehsan. Have fun bro</H1><html>"

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
        return render_template('form2.html')
    
@app.route('/submit', methods=['GET','POST'])
def submit():  # This function is triggered when the form is submitted to /submit
    if request.method == 'POST':
        name = request.form['name']
        return f"Hi {name} welcome"
    return render_template('form2.html')  

    """ this last line is not even required. because the submitted data will be sent to the /submit url on the server side using POST method.
    BUT, note that if this line is omitted, you can't directly go to the /submit url
    WHY? because you have ommited the GET method for this url. if you enter the /submit url directly, it sends a GET request
    to the server, but our application would not be able to handle it.
    """

if __name__ == '__main__':
    app.run(debug=True)



# In this module we are working with the form2.html file

# we have added a parameter to the form tag, called : action
# The action parameter in the <form> tag specifies the URL or path to which the form data will be sent when the form is submitted. 
# Essentially, it tells the browser where to send the collected data for processing.
# action="/submit" in the form tag Specifies that when the form is submitted, the data will be sent to the /submit URL on the server.
# Clicking the "Submit" button sends the form data to the server (to the /submit endpoint) using the specified HTTP method (POST).

# in the form tag If no action is specified, the form will submit to the current page by default.

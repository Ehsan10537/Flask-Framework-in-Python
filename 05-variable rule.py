### Variable rule

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    if request.method == 'GET':
        return "<html><H1>Welcome to this Flask course Ehsan. Have fun bro</H1><html>"

### This about Variable rule
@app.route('/success/<score>')                # now you can add parameter, which will be concedered as a string value by default.
def success(score):                           # as you can see you can use the argument here as an input to your application function
    return f"The score you got is {score}. The datatype of your score is String" 

# Now if you go to forexample /success/74 url, it returns: The mark you got is 74
# you can specify the data type of the variable as below:


@app.route('/success2/<int:score>')           # now you have to give it an integer value. so you can assign a rule to the variable.
def success2(score):
    return f"The score you got is {score}. The datatype of your score is Integer"

if __name__ == '__main__':
    app.run(debug=True)

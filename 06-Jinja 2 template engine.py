
### Building url dynamically 
### Jinja 2 template engine

'''
In Jinja2 template engine, you can use the following syntaxes to make your app dynamic.
So they are not native to HTML itself but is part of template engines like Jinja2, 
which is commonly used in Python web frameworks such as Flask.
In template engines like Jinja2, the symbols {# #}, {{ }}, and {% %} serve different purposes. Here's what each of them does:

{{ ... }}    Expression/Variable Output. To output dynamic data or evaluate expressions directly into the HTML.
{% ... %}    Control Structures. To write logic and conditions or control statements in the template.
{# ... #}    Comments. To add comments in a template file that are ignored by the template engine and do not appear in the final output.

'''

"""
On the whole with the help of Jinja 2 template engine you can integrate any back end data source with your html 
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    if request.method == 'GET':
        return "<html><H1>Welcome to this Flask course Ehsan. Have fun bro</H1><html>"


@app.route('/success/<int:score>')              
def success(score):
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    return render_template('result.html', result=res)  # here we have defined a variable called result and assigned it to res
    # here we are redirecting the res variable to result.html file
    # and there we are going to read it as result variable and use it. 


@app.route('/success2/<int:score>')
def success2(score):
    if score >= 50:
        res = 'PASSED'
    else:
        res = 'FAILED'

    exp = {'score':score, 'result':res}  

    return render_template('result2.html', result=exp)


@app.route('/success3/<int:score>')
def success3(score):
    return render_template('result3.html', result=score)


if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for

"""
The redirect() function is used to send the user to a different URL (route) in your Flask application or an external link.

The url_for() function is used to generate URLs dynamically for your routes. Instead of hardcoding URLs in your application,
 you reference them by their function names.

"""

"""
Here in this example, if you go the /submit url, it sends a GET request to the server,
 so the app returns the form in result_form.html file. after submitting the form, the form data will be sent to the same /submit url as
 a POST request.
 and as you see, when this POST request comes to the server, the saluesvcores will be captured and a mean will be calculated.
 then, the rest of the process will be redirected to the /success/score url as a GET request providing the score parameter value being the
 mean value calculated.

 after receiving this GET request by the server, the app redirects to the html file with respect to the score value, and
 eventually returns it.
"""

app = Flask(__name__)

@app.route('/')
def welcome():
    if request.method == 'GET':
        return "<html><H1>Welcome to this Flask course Ehsan. Have fun bro</H1><html>"


@app.route('/success/<int:score>')              
def success(score):
    return render_template('result3.html', result=score)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        
        mean_score = (science+maths+c+datascience)/4

        return redirect(url_for('success', score=mean_score)) 

    else:
        return render_template('result_form.html')



if __name__ == '__main__':
    app.run(debug=True)
    
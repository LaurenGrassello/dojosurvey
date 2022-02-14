from flask import Flask, redirect, render_template, session, request


app = Flask(__name__)
app.secret_key = 'bloopbleepbloopbopbleepblopboop'

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/process", methods=["POST", "GET"])
def user_info(): 
    if request.method == 'POST':
        session['u_name'] = request.form['name']
        session['u_location'] = request.form['location']
        session['u_favlang'] = request.form['favlang']
        session['u_comments'] = request.form['comments']
    print(request.form)
    return redirect('/result' )


@app.route("/result")
def survey_complete():
    return render_template('index2.html')
    



if __name__=="__main__":
    app.run(debug=True)
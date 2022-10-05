from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')



@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success',name=user))
    else:
        user = request.form['user']
        return  redirect(url_for('success',name = user))


if __name__ ==  "__main__":
    app.run(debug=True)
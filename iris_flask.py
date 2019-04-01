from flask import Flask,render_template, request
import day0401.func

app = Flask (__name__)

@app.route('/iris.do')
def iris():
    return render_template('iris.html')

@app.route('/irisOK.do', methods =['POST'])
def irisOK():
    a = request.form['aa']
    b = request.form['bb']
    c = request.form['cc']
    d = request.form['dd']
    data = day0401.func.iris(a,b,c,d)
    for i in data:
        print(i)
    return render_template('iris.html',i=i)

if __name__=='__main__':
    app.run(debug=True,host='203.236.209.95')

from flask import Flask, render_template, request
import numpy as np
import requests
import pickle
app= Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        gender = int(request.form['gender'])
        ssc_p = float(request.form['ssc_p'])
        ssc_b_Central = int(request.form['ssc_b'])
        hsc_p = float(request.form['hsc_p'])
        hsc_b_Central = int(request.form['hsc_b'])
        hsc_s = request.form['hsc_s']
        if hsc_s == "Commerce":
            commerce = 1
            science = 0
        elif hsc_s == "Science":
            commerce = 0
            science = 1
        else:
            commerce = 0
            science = 0
        degree_p = float(request.form['degree_p'])
        degree_t = request.form['degree_t']
        if degree_t == "Sci&Tech":
            other = 0
            scitech = 1
        elif degree_t == "Comm&Mgmt":
            other = 0
            scitech = 0
        else:
            other = 1
            scitech = 0
        workex = int(request.form['workex'])
        etest_p = float(request.form['etest_p'])
        specialisation = int(request.form['specialisation'])
        mba_p = float(request.form['mba_p'])
        status = int(request.form['status'])

        scaled = scaler.transform(np.array([commerce,science,other,scitech,gender,ssc_p,hsc_p,degree_p,workex,etest_p,mba_p,status,ssc_b_Central,hsc_b_Central,specialisation]).reshape(1, -1))
        prediction = round(model.predict(scaled)[0],2)
        if prediction < 0:
            prediction = 0
    return render_template('prediction.html',result=prediction)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)

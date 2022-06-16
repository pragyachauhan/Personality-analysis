from flask import Flask , jsonify , request, render_template, escape
import pickle
import numpy as np


app = Flask(__name__)
model= pickle.load(open('model.pkl','rb'))

@app.route('/home')
def home():
   return render_template("home.html")

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
       # name=request.form['name']
        #gender =request.form['gender']
        #age =request.form['age']
        o =request.form['opn']
        n =request.form['nrm']
        c =request.form['con']
        a =request.form['agr']
        e =request.form['ext']

        int_input=[int(x) for x in request.form.values()]
        input =np.array([int_input])
   
        prediction= model.predict(input)
        return render_template("prediction.html", prediction_text='Your Personality is:{}'.format(prediction))
   
    else:
        return render_template("prediction.html")



if __name__=="__main__":
    app.run(debug=True)

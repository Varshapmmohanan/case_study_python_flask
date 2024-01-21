from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        PL = request.form['PL']
        PW = request.form['PW']
        print(PL,PW)
        pickled_model = pickle.load(open('model.pkl','rb'))
        Classification = pickled_model.predict([[float(PL,PW)]])
        print(Classification)
    
    return render_template('prediction.html', Classification=Classification)


if __name__ == '__main__':
    app.run()
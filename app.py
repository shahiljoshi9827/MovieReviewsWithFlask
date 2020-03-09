from flask import Flask,render_template,request
import requests
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/data',methods = ['POST', 'GET'])
def fun():
      if request.method == 'POST':
        result = request.form['abc']

        data1 = requests.get(f'https://api.nytimes.com/svc/movies/v2/reviews/search.json?query={result}&api-key=uMDGxu67Vj5S1NXA1GCj3HXbmC6QM0Jp')
        data1=data1.json()
        data1=data1['results'][0]
        return render_template("index.html",data1=data1)

if __name__ == '__main__':
    app.run(host='localhost',port='80',debug=True)

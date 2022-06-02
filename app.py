import numpy as np
import os
from flask import Flask, request, jsonify, render_template
from keras.models import load_model

os.chdir(os.path.dirname(os.path.abspath(__file__))) # sets current directory

app = Flask(__name__)
model = load_model("Baseball.h5")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        pitch_type = request.form.get('Pitches')
        print(pitch_type)
        if pitch_type == "pitch_typeab":
            X = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typech":
            X = [[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typecu":
            X = [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typeep":
            X = [[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typefa":
            X = [[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typefc":
            X = [[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typeff":
            X = [[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typefo":
            X = [[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typefs":
            X = [[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typeft":
            X = [[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typein":
            X = [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typekc":
            X = [[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]]
        elif pitch_type == "pitch_typekn":
            X = [[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]]
        elif pitch_type == "pitch_typepo":
            X = [[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]]
        elif pitch_type == "pitch_typesc":
            X = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]]
        elif pitch_type == "pitch_typesi":
            X = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]]
        elif pitch_type == "pitch_typesl":
            X = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]]
        elif pitch_type == "pitch_typeun":
            X = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
    print(X)
    prediction = model.predict(X)
    print(prediction)
    return render_template('index.html', prediction_text=f'The chance of hitting a Single is {round(prediction[0][0] * 100, 2)}%, The chance of hitting a Double is {round(prediction[0][1] * 100, 2)}%, The chance of hitting a Triple is {round(prediction[0][2] * 100, 2)}%, The chance of hitting a Home Run is {round(prediction[0][3] * 100, 2)}%')

@app.route('/data')
def data():
    render_template('data.html')

@app.route('/visualizations')
def visualizations():
    render_template('vizualizations.html')

if __name__ == "__main__":
    app.run(debug=True)
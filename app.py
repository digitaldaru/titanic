from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model (update the filename if necessary)
with open(r'C:\Users\ajaym\OneDrive\Desktop\Kunal\code\kunal\Titanic\Titanic Prediction.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Mapping Age and Fare selections to numeric values according to encoding logic
    age_mapping = {
        "0-17": 0.0,
        "18-32": 1.0,
        "33-48": 2.0,
        "49-64": 3.0,
        "65-80": 4.0
    }

    fare_mapping = {
        "0-7": 0.0,
        "8-14": 1.0,
        "15-42": 2.0,
        "43+": 3.0
    }

    # Retrieve form inputs and map Age and Fare
    features = [
        float(request.form['Pclass']),
        float(request.form['Sex']),
        float(request.form['Embarked']),
        age_mapping[request.form['Age']],
        fare_mapping[request.form['Fare']],
        float(request.form['Fam_type']),
        float(request.form['Title'])
    ]

    # Predict
    prediction = model.predict([features])[0]
    result = 'Survived' if prediction == 1 else 'Did Not Survive'

    return render_template('index.html', prediction_text=f'Prediction: {result}')


if __name__ == "__main__":
    app.run(debug=True)

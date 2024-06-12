from flask import Flask, request, jsonify, render_template
import pickle

# Load the model and vectorizer
with open('rf_model.sav', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Initialize Flask app
app = Flask(__name__)

# Define a function to make predictions
def predict_spam_ham(message):
    message_features = vectorizer.transform([message])
    prediction = model.predict(message_features)[0]
    return 'ham' if prediction == 1 else 'spam'

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    prediction = predict_spam_ham(message)
    return render_template('index.html', prediction_text=f'The message is classified as: {prediction}')

if __name__ == '__main__':
    app.run(debug=True)

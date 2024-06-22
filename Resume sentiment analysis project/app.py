from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Function to clean and preprocess resume text
def cleanResume(resume_text):
    # Your cleaning/preprocessing code here
    cleaned_text = resume_text  # Placeholder, replace with your actual cleaning logic
    return cleaned_text

# Load the trained model
model_path = 'model_rfc.pkl'
model = pickle.load(open(model_path, 'rb'))

# TF-IDF vectorizer (assuming you used it for training)
tfidf_path = 'tfidf_rfc.pkl' 
tfidf = pickle.load(open(tfidf_path, 'rb'))

# Mapping of prediction IDs to category names
category_mapping = {
    8: "DevOps Engineer",
    23: "Testing",
    15: "Data Analyst",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    13: "Hadoop",
    3: "Blockchain",
    10: "ETL Developer",
    18: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer",
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and fitness",
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate"
}

# Index/home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        resume_text = request.form['resume_text']

        if resume_text:
            # Clean and preprocess the input resume
            cleaned_resume = cleanResume(resume_text)
            input_features = tfidf.transform([cleaned_resume])

            # Make prediction
            prediction_id = model.predict(input_features)[0]
            category_name = category_mapping.get(prediction_id, "Unknown")

            return render_template('index.html', prediction_text=f'The resume belongs to the category of {category_name}')
        else:
            return render_template('index.html', prediction_text='Please enter a resume to predict.')

if __name__ == '__main__':
    app.run(debug=True)

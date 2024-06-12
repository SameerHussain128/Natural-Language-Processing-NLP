import streamlit as st
import pickle

# Load the model and vectorizer
with open('rf_model.sav', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define a function to make predictions
def predict_spam_ham(message):
    message_features = vectorizer.transform([message])
    prediction = model.predict(message_features)[0]
    return 'ham' if prediction == 1 else 'spam'

# Streamlit app
st.title("Spam-Ham Classification")
st.write("Enter a message to classify it as Spam or Ham")

# Text input
user_input = st.text_area("Message")

if st.button("Classify"):
    if user_input:
        result = predict_spam_ham(user_input)
        st.write(f"The message is classified as : **{result}**")
    else:
        st.write("Please enter a message to classify.")
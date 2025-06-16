import streamlit as st
import joblib

st.title("📩 Spam Message Detector")

vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("spam_classifier.pkl")

message = st.text_area("Enter a message:")

if st.button("Check"):
    input_vec = vectorizer.transform([message])
    prediction = model.predict(input_vec)[0]

    if prediction == 1:
        st.error("🚫 This message is SPAM!")
    else:
        st.success("✅ This message is NOT spam.")

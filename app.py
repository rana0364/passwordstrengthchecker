import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import streamlit as st

st.title("🔐 Password Strength Checker")

@st.cache_data
def load_data():
    return pd.read_csv("password_dataset.csv")

df = load_data()

le = LabelEncoder()
df['strength_encoded'] = le.fit_transform(df['strength'])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['password'])
y = df['strength_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

user_input = st.text_input("Enter a password to check strength:")

if user_input:
    vec_input = vectorizer.transform([user_input])
    pred = model.predict(vec_input)
    label = le.inverse_transform(pred)
    st.subheader(f"Strength: {label[0]}")







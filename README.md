# 🔐 Password Strength Checker

A simple web app to check if a password is Weak, Medium, or Strong using a basic Machine Learning model.

Built with Python, Streamlit, Pandas, and Scikit-learn.

## Demo

*[Watch the Demo Video](https://streamable.com/mxdbir)*

(Link: https://streamable.com/mxdbir)

## How it Works

The app uses a pre-trained Logistic Regression model. When you enter a password, the model predicts its strength based on patterns learned from a sample dataset (password_dataset.csv).

## Setup & Run

1.  *Clone the repository:*
    bash
    git clone https://github.com/rana0364/passwordstrengthchecker.git
    cd passwordstrengthchecker
    
2.  *Install dependencies:*
    bash
    pip install streamlit pandas scikit-learn
    
3.  *Run the app:*
    Make sure password_dataset.csv is in the same folder.
    bash
    streamlit run app.py
    

The app will open in your browser. Enter a password to see its predicted strength.

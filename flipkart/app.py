from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("sentiment.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    if request.method == 'POST':
        user_name = request.form['name']
        user_review = request.form['review']
        
        review_text = pd.Series(user_review)
        model = joblib.load("Best_models1/Logistic Regression.pkl")
        prediction = model.predict(review_text)

        return render_template("output.html", prediction=prediction, name=user_name, review=user_review)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

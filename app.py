# coding: utf-8

import os
import pandas as pd
from flask import Flask, request, render_template
import pickle
import webbrowser
import threading

# --- Debugging template paths ---
print("Current working directory:", os.getcwd())
print("Templates folder exists:", os.path.isdir(os.path.join(os.getcwd(), "templates")))
print("Home.html exists:", os.path.isfile(os.path.join(os.getcwd(), "templates", "home.html")))

# --- Flask app ---
app = Flask(__name__, template_folder="template")

# Load dataset and model
df_1 = pd.read_csv("first_telc.csv")
model = pickle.load(open("model.sav", "rb"))

@app.route("/")
def loadPage():
    return render_template('home.html', query1="", query2="", query3="", query4="", query5="",
                           query6="", query7="", query8="", query9="", query10="", query11="", query12="",
                           query13="", query14="", query15="", query16="", query17="", query18="", query19="")

@app.route("/", methods=['POST'])
def predict():
    input_data = [request.form[f'query{i}'] for i in range(1, 20)]
    new_df = pd.DataFrame([input_data], columns=[
        'SeniorCitizen','MonthlyCharges','TotalCharges','gender','Partner','Dependents','PhoneService',
        'MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport',
        'StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','tenure'
    ])
    df_2 = pd.concat([df_1, new_df], ignore_index=True)

    labels = ["{0} - {1}".format(i,i+11) for i in range(1,72,12)]
    df_2['tenure_group'] = pd.cut(df_2.tenure.astype(int), range(1,80,12), right=False, labels=labels)
    df_2.drop(columns=['tenure'], inplace=True)

    new_df_dummies = pd.get_dummies(df_2[['gender','SeniorCitizen','Partner','Dependents','PhoneService',
        'MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport',
        'StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','tenure_group']])

    prediction = model.predict(new_df_dummies.tail(1))[0]
    probability = model.predict_proba(new_df_dummies.tail(1))[:,1][0]

    o1 = "This customer is likely to be churned!!" if prediction==1 else "This customer is likely to continue!!"
    o2 = f"Confidence: {probability*100:.2f}%"

    return render_template('home.html', output1=o1, output2=o2,
                           **{f'query{i}': input_data[i-1] for i in range(1, 20)})

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)

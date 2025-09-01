# Customer-churn-Prediction-and-Analysis-
An end-to-end project that combines Machine Learning, Data Visualization, and Web Deployment to predict and analyze customer churn. The system helps businesses identify customers likely to leave and provides insights to improve retention strategies.

🔍 **Project Overview**
The project covers the complete lifecycle of a data-driven application:

--Exploratory Data Analysis (EDA) – Using Python and Power BI for churn patterns, feature correlations, and business insights.

--Data Preprocessing & Feature Engineering – Handling missing values, encoding categorical variables, scaling features, and balancing data.

--Model Building (ML) – Training multiple models (Logistic Regression, Random Forest, Gradient Boosting, XGBoost) and selecting the best performer.

--Churn Prediction API (Flask) – Serving the ML model through a REST API for real-time predictions.

--Interactive Dashboard (Power BI) – Visualizing KPIs such as churn rate, customer demographics, service usage, and prediction outcomes.

--Web-based UI – Built with HTML, CSS, and JavaScript to provide a clean interface where users can input customer details and view churn prediction results.

**Tech Stack**
Machine Learning & Analysis: Python, Pandas, Scikit-learn, XGBoost
Visualization: Power BI (interactive dashboards)
Backend: Flask (REST API for predictions)
Frontend: HTML, CSS, JavaScript (customer input form + results display)
Deployment: Localhost / Cloud-ready (Heroku, AWS, or Azure)

**Screenshot**
<img width="437" height="428" alt="s" src="https://github.com/user-attachments/assets/c945dcd5-2748-48a8-9c67-aedf1183c0ec" />

📂 Repository Structure
├── data/                 # Raw and processed datasets  
├── notebooks/            # Jupyter notebooks for EDA & model building  
├── models/               # Saved ML models (pickle files)  
├── powerbi/              # Power BI dashboards (.pbix file)  
├── static/               # CSS, JS, images for UI  
├── templates/            # HTML pages for Flask app  
├── app.py                # Flask backend script  
├── requirements.txt      # Python dependencies  
└── README.md             # Project description (this file)  
🚀 How to Run

Clone the repo:

git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction


**Install dependencies:**
pip install -r requirements.txt
**Run Flask app:**
python app.py

--Open your browser at http://127.0.0.1:5000/ to access the UI.
--Open Power BI and load the .pbix file for interactive analysis.




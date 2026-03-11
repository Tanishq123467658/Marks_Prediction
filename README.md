# 📊 Marks Prediction App

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-green)

A **machine learning web application** that predicts **student exam scores** based on various academic and personal factors. The application uses a **tuned XGBoost regression model** and is deployed using **Streamlit** for an interactive interface.

---

# 📌 Project Description

Predicting student performance can help educators understand the impact of different study habits and external factors on academic results. This project demonstrates how machine learning can analyze student-related data and predict exam scores.

The model was trained using a dataset containing student-related attributes. After training, the model was integrated into a **Streamlit web application** that allows users to input student details and receive predicted marks instantly.

### Technologies used

• **XGBoost** – for high performance regression modeling
• **Label Encoding** – to convert categorical variables into numerical values
• **Streamlit** – to build and deploy the web interface
• **Pandas & NumPy** – for data processing

### Challenges faced

* Handling categorical variables during prediction
* Ensuring the same encoders used during training are applied during inference
* Deploying the model with correct dependency versions

### Future improvements

* Add batch predictions using CSV upload
* Show model evaluation metrics
* Add feature importance visualization
* Improve UI styling

---

# 📚 Table of Contents

* Project Description
* Installation
* Running the Project
* How to Use
* Project Structure
* Technologies Used
* Credits
* License

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Tanishq123467658/Marks_Prediction.git
```

Navigate to the project directory

```bash
cd Marks_Prediction
```

Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Mac / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Run the Streamlit application

```bash
streamlit run main.py
```

After running the command, open the browser and go to:

```
http://localhost:8501
```

---

# 🧑💻 How to Use

1. Open the application in your browser.
2. Enter the required student information.
3. Click the **Predict Score** button.
4. The trained **XGBoost model** will estimate the student's exam score.

The application automatically processes categorical features using the saved **label encoders** before passing the data to the trained model.

---

# 📂 Project Structure

```
Marks_Prediction
│
├── Exam_Score_Prediction.csv    # Dataset used for training
├── label_encoders.pkl           # Saved label encoders
├── xgboost_tuned_model.pkl      # Trained XGBoost model
├── main.py                      # Streamlit application
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

---

# 🛠 Technologies Used

Python
Streamlit
Pandas
NumPy
Scikit-learn
XGBoost

---

# 🙌 Credits

Developed by **Tanishq Battul**

Student at **Vidyalankar Institute of Technology**
Interested in **Machine Learning, Data Science, and AI systems**

---

# 📄 License

This project is licensed under the **MIT License**.

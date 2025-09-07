# InsuranceML Web App

A full-stack web application to predict health insurance charges using Machine Learning.
Built with XGBoost for the backend and HTML, JavaScript, Tailwind CSS for a responsive, interactive frontend.

Deployed using Amazon EC2 with Elastic Beanstalk container for scalable and reliable cloud hosting.

---

## Features

- Predict insurance charges based on Age, Sex, BMI, Children, Smoker, and Region  
- Fast predictions with a trained XGBoost regression model  
- Modern and responsive UI with Tailwind CSS  
- Interactive frontend with real-time prediction display  
- Optional future extension: graphs comparing predicted charges with averages  
- Session-based prediction history table  

---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/CodeRockstar24/insuranceML-webapp.git
cd insuranceML-webapp
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the backend server

```bash
python backend/app.py
```

### 4️⃣ Open the frontend

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 🛠️ Tech Stack

* **Backend:** Python (`pandas`, `xgboost`, `flask`)
* **Frontend:** `HTML5`, `JavaScript`, `Tailwind CSS`
* **Model:** XGBoost regression saved as a pickle file

---

## 👨‍💻 Author

**CodeRockstar24**


## 📄 License

MIT License


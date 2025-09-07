# InsuranceML Web App

A full-stack web application to predict health insurance charges using Machine Learning.
Built with XGBoost for the backend and HTML, JavaScript, Tailwind CSS for a responsive, interactive frontend.

Deployed using Amazon EC2 with Elastic Beanstalk container for scalable and reliable cloud hosting.

<img width="1200" height="800" alt="image" src="https://github.com/user-attachments/assets/26e39b5e-a35e-4cab-a924-ea713db8a3f6" />   <img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/ffe8d688-062e-4d09-b699-3f9a88a2107a" /> <img width="1200" height="630" alt="image" src="https://github.com/user-attachments/assets/fd9e18c5-b80a-4055-bb39-35019bc79b3d" />



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


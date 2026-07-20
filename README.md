# 🚀 Retail Intelligence Analytics Platform

An end-to-end **Retail Intelligence & Sales Analytics Platform** built using **FastAPI, React, MySQL, SQLAlchemy, and Machine Learning**.

This project enables businesses to upload sales data, perform automated data cleaning, generate interactive dashboards, analyze key business metrics, and forecast future sales using machine learning models.

---

## 📌 Project Overview

The platform is designed to help retail businesses transform raw sales data into actionable business insights.

Users can:

- Upload retail sales datasets (CSV)
- Clean and preprocess data automatically
- Analyze business KPIs
- Visualize sales trends
- Forecast future sales
- Generate downloadable reports

---

# ✨ Features

## 🔐 Authentication
- User Registration
- Secure Login
- JWT Authentication
- Password Hashing (bcrypt)

---

## 📂 Dataset Management

- Upload CSV datasets
- Dataset validation
- Automatic preprocessing
- Missing value handling
- Duplicate removal

---

## 📊 Analytics Dashboard

- Total Revenue
- Total Profit
- Orders Analysis
- Customer Analysis
- Product Analysis
- Regional Sales
- Monthly Sales Trend
- Interactive Charts

---

## 🤖 Machine Learning

- Sales Forecasting
- Customer Segmentation
- Business Insights
- Predictive Analytics

---

## 📄 Reports

- PDF Report Generation
- Export Analytics
- Download Clean Dataset

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- JWT Authentication
- Passlib (bcrypt)

---

## Frontend

- React
- Tailwind CSS
- Axios
- Chart.js

---

## Data Analysis

- Pandas
- NumPy

---

## Machine Learning

- Scikit-learn

---

## DevOps

- Docker
- Git
- GitHub

---

# 📁 Project Structure

```text
Retail-Intelligence-Analytics-Platform/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── config/
│   │   ├── database/
│   │   ├── data_processing/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   ├── tests/
│   ├── .env.example
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── database/
│
├── docker/
│
├── docs/
│
├── screenshots/
│
├── docker-compose.yml
├── LICENSE
├── README.md
└── .gitignore
```

---

# 🗄 Database

- MySQL 8.0
- SQLAlchemy ORM

Main Tables:

- Users
- Uploads
- Products
- Customers
- Sales
- Forecasts
- Reports

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Akashbera28/Retail-Intelligence-Analytics-Platform.git
```

## Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 📅 Development Roadmap

- [x] Project Setup
- [x] GitHub Repository
- [x] FastAPI Backend
- [x] MySQL Configuration
- [ ] SQLAlchemy Models
- [ ] JWT Authentication
- [ ] CSV Upload
- [ ] Data Cleaning
- [ ] Dashboard APIs
- [ ] React Frontend
- [ ] Sales Forecasting
- [ ] Customer Segmentation
- [ ] Docker Deployment

---

# 📸 Screenshots

Screenshots will be added as development progresses.

---

# 📖 API Documentation

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

---

# 👨‍💻 Author

**Akash Bera**

GitHub: https://github.com/Akashbera28

---

# ⭐ License

This project is licensed under the MIT License.
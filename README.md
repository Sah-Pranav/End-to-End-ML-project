# 🏡 End-to-End ML Project: King County House Price Prediction

A regression project to predict the sale price of houses using the **King County House Sales dataset** from Kaggle.

---

## 📖 About the Data

The dataset includes 21 features related to physical, locational, and structural house attributes.  
**Target variable:** `price` (house sale price)
 

**Dataset Source:**  
👉 [Kaggle - King County House Sales](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)

---

## 📊 Exploratory Data Analysis Notebook

📒 [EDA Notebook](https://github.com/Sah-Pranav/End-to-End-ML-project/blob/main/notebook/EDA.ipynb)

---

## 🏗️ Model Training Approach Notebook

📒 [Model Training Notebook](https://github.com/Sah-Pranav/End-to-End-ML-project/blob/main/notebook/MODEL_TRAINING.ipynb)

---

## 📂 Screenshots Directory

You can find all project-related screenshots in the [`/screenshots`](https://github.com/Sah-Pranav/End-to-End-ML-project/tree/main/screenshots) directory of this repository.

---

## 📌 Project Workflow

1. **Data Ingestion**
   - Load CSV dataset.
   - Split into training and test datasets.
   - Save locally as separate files.

2. **Data Transformation**
   - Numeric columns: Median imputation ➝ StandardScaler.
   - Categorical columns (if any): Most frequent imputation ➝ Encoding ➝ StandardScaler.
   - Save the transformation pipeline as a `.pkl` file.

3. **Model Training**
   - Test multiple regression algorithms:
     - Linear Regression  
     - KNeighborsRegressor  
     - DecisionTreeRegressor  
     - RandomForestRegressor  
     - AdaBoostRegressor  
     - GradientBoostingRegressor  
     - CatBoostRegressor  
   - Perform hyperparameter tuning.
   - Save the best-performing model as `model.pkl`.

4. **Prediction Pipeline**
   - Create a pipeline that loads the trained model and preprocessor.
   - Transforms incoming data and returns predictions.

5. **Flask Web Application**
   - Build a simple, interactive user interface using Flask for live predictions.
   - Integrate the prediction pipeline for real-time results.

---

## 🌐 Microsoft AZURE Deployment Link
🏠 [House Price Prediction App](https://housepriceprediction-f8cce5ahgwh5ghaq.germanywestcentral-01.azurewebsites.net/)

> **Note:** Deployment link may not be active if the Azure service has been deprovisioned. You can follow the project locally.

---

## ✨ Author

**PRANAV KUMAR SAH**

---

# 🏡 End-to-End ML Project: King County House Price Prediction

A regression project to predict the sale price of houses using the **King County House Sales dataset** from Kaggle.

---

## 📖 Introduction About the Data

The goal is to predict the `price` of a given house using various physical, locational, and structural parameters.

**The dataset contains 21 independent variables (including `id`):**

| Variable         | Description                                                   |
|:----------------|:--------------------------------------------------------------|
| `id`             | Unique identifier for each house sale                         |
| `date`           | Date of the house sale                                         |
| `price`          | Sale price of the house (target variable)                      |
| `bedrooms`       | Number of bedrooms                                             |
| `bathrooms`      | Number of bathrooms (where .5 accounts for a half bath)        |
| `sqft_living`    | Interior living space in square feet                          |
| `sqft_lot`       | Total lot size in square feet                                  |
| `floors`         | Number of floors                                               |
| `waterfront`     | 1 if waterfront view; 0 otherwise                              |
| `view`           | Index from 0 to 4 indicating view quality                      |
| `condition`      | Condition of the house (numerical scale)                       |
| `grade`          | Overall grade based on construction and design                 |
| `sqft_above`     | Square footage excluding basement                              |
| `sqft_basement`  | Square footage of the basement                                 |
| `yr_built`       | Year the house was built                                       |
| `yr_renovated`   | Year the house was renovated (0 if never)                      |
| `zipcode`        | Location zip code                                              |
| `lat`            | Latitude coordinate                                            |
| `long`           | Longitude coordinate                                           |
| `sqft_living15`  | Average living area of 15 nearest neighbors                    |
| `sqft_lot15`     | Average lot size of 15 nearest neighbors                       |

**Target variable:**

- `price` : Sale price of the house  

**Dataset Source:**  
👉 [Kaggle - King County House Sales](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)

---

## 📊 Exploratory Data Analysis Notebook

📒 [EDA Notebook](https://github.com/Sah-Pranav/End-to-End-ML-project/blob/main/notebook/EDA.ipynb)

---

## 🏗️ Model Training Approach Notebook

📒 [Model Training Notebook](https://github.com/Sah-Pranav/End-to-End-ML-project/blob/main/notebook/MODEL_TRAINING.ipynb)

---

## 📸 Screenshot of UI

*(Add your image link here)*  
`![](path/to/screenshot.png)`

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

## ✨ Author

**PRANAV KUMAR SAH**

---

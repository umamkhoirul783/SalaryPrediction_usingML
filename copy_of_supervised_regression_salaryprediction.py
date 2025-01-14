# -*- coding: utf-8 -*-
"""Copy of Supervised_Regression_SalaryPrediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZYvcOiStRHqzKs653xT1M3W2BaptTuvS

# Supervised - Salary Prediction - Regression
"""

# import all the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""### Data Ingestion"""

# Read the dataset using pandas
data = pd.read_csv('salary_data.csv')

# This displays the top 5 rows of the data
# We usually do this to check data structure and if data is being loaded properly
data.head()

"""### Exploratory Data Analysis"""

# Provides some information regarding the columns in the data
data.info()

# Display data description
data.describe()

# Set seaborn theme
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['experience_years'], y=data['salary'],
                color="dodgerblue", s=100, edgecolor="black")

# Add titles and labels
plt.title('Relationship Between Experience and Salary', fontsize=16, fontweight='bold')
plt.xlabel('Years of Experience', fontsize=12)
plt.ylabel('Salary', fontsize=12)

# Enhance plot aesthetics
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Show the plot
plt.show()

"""### Data Preparation
1. Check Duplicated Data
2. Check Missing Value Handling
3. Encoding categorical : change string (categorical) into numerical -> in this dataset, there is no categorical column.
"""

df = data.copy()

#Check Duplicated Data
print("Data Sebelum Pemeriksaan Duplikat:")
print(df.shape)

duplicated_rows = df[df.duplicated(keep=False)]
duplicated_rows

df = df.drop_duplicates()

print("\nData Setelah Pemeriksaan Duplikat:")
print(df.shape)

#Check missing value
df.isna().sum()

"""There is no missing value

We have done data preprocessing, next we are doing machine learning modelling and splitting data into X_train, X_test -> Predictor, y_train, y_test -> target variables

### Splitting the data
"""

# Experience of Years data
X = df['experience_years']
X.head()

# Salary data
y = df['salary']
y.head()

# Import machine learning data from scikit learn
from sklearn.model_selection import train_test_split

# Split the data for train and test
# train : test = 75 : 25 atau 80 : 20 atau 70:30 atau 85:15 , size train > test
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.75,random_state=42)

X_train.shape

X_test.shape

# Reshape because we only have single features.
# This is not needed if our features is 2 or more
X_train_reshape = X_train.values.reshape(-1, 1)
X_test_reshape = X_test.values.reshape(-1, 1)

"""### Linear Regression"""

# Importing Linear Regression model from scikit learn
from sklearn.linear_model import LinearRegression

model_lr = LinearRegression()
model_lr.fit(X_train_reshape, y_train)

y_test_pred = model_lr.predict(X_test_reshape)
y_test_pred

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_test_pred, color='red', label='Predicted')
plt.plot(X_test, y_test_pred, color='green', label='Regression Line', linewidth=2)  # Line for predicted values
plt.title('Linear Regression: Test Data vs Test Prediction')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.grid(True)
plt.show()

# Check error rate between train_data prediction and test_data prediction
from sklearn.metrics import mean_squared_error, r2_score

y_test_pred = model_lr.predict(X_test_reshape)
y_train_pred = model_lr.predict(X_train_reshape)

mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)

print(f"""
Mean Squared Error:
  Train: {mse_train:.2f}
  Test : {mse_test:.2f}
  Gap  : {abs(mse_train - mse_test):.2f}
R^2 Score:
  Train: {r2_train:.2f}
  Test : {r2_test:.2f}
      """)

# Intercept and coeff of the line
print('Intercept of the Linear Regression model:',model_lr.intercept_)
print('Coefficient of the line Linear Regression:',model_lr.coef_)

"""### Then the linear regression model is

# y = 1641.366 + 103.197 x

### Decision Tree Model
"""

from sklearn.tree import DecisionTreeRegressor

model_dt = DecisionTreeRegressor(random_state=42)
model_dt.fit(X_train_reshape, y_train)
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
X_reshape = X.values.reshape(-1, 1)  # Mengubah Series X menjadi array 2D

regr_1.fit(X_reshape, y)
regr_2.fit(X_reshape, y)

y_pred_dt = model_dt.predict(X_test_reshape)

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred_dt, color='red', label='Predicted (Decision Tree)')
plt.title('Decision Tree: Test Data vs Test Prediction')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.grid(True)
plt.show()

# Check error rate between train_data prediction and test_data prediction
from sklearn.metrics import mean_squared_error, r2_score

y_test_pred = model_dt.predict(X_test_reshape)
y_train_pred = model_dt.predict(X_train_reshape)

mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)

print(f"""
Mean Squared Error:
  Train: {mse_train:.2f}
  Test : {mse_test:.2f}
  Gap  : {abs(mse_train - mse_test):.2f}
R^2 Score:
  Train: {r2_train:.2f}
  Test : {r2_test:.2f}
      """)

# Saving the model
import joblib
joblib.dump(model_dt, 'decision_tree_model.pkl')

# Reading the model
loaded_model = joblib.load('decision_tree_model.pkl')

# Testing the model
y_pred_load = loaded_model.predict(X_test_reshape)

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred_load, color='red', label='Predicted (Decision Tree)')
plt.legend()
plt.show()

"""### Using Random Forest"""

from sklearn.ensemble import RandomForestRegressor
model_rf = RandomForestRegressor()
model_rf.fit(X_train_reshape, y_train)

y_pred_rf = model_rf.predict(X_test_reshape)
plt.figure(figsize=(10,6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
# plt.plot(X_test, y_pred_rf, color="cornflowerblue", label="max_depth=2", linewidth=2)
# plt.plot(X_test, y_test, color="yellowgreen", label="max_depth=20", linewidth=2)
plt.scatter(X_test, y_pred_rf, color='red', label='Predicted (Random Forest)')
plt.title('Random Forest: Test Data vs Test Prediction')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.grid(True)
plt.show()

# Membuat model Random Forest dengan max_depth berbeda
regr_1 = RandomForestRegressor(max_depth=2, random_state=42)
regr_2 = RandomForestRegressor(max_depth=20, random_state=42)

# Melatih model
regr_1.fit(X_train_reshape, y_train)
regr_2.fit(X_train_reshape, y_train)

# Membuat rentang nilai X untuk prediksi
X_range = np.arange(X.min(), X.max(), 0.1).reshape(-1, 1)

# Melakukan prediksi dengan kedua model
y_1 = regr_1.predict(X_range)
y_2 = regr_2.predict(X_range)

# Membuat plot
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred_rf, color='red', label='Predicted (Random Forest)')
plt.plot(X_range, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_range, y_2, color="yellowgreen", label="max_depth=20", linewidth=2)
plt.title('Random Forest: Pengaruh Max Depth')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.grid(True)
plt.show()

# Check error rate between train_data prediction and test_data prediction
from sklearn.metrics import mean_squared_error, r2_score

y_test_pred = model_rf.predict(X_test_reshape)
y_train_pred = model_rf.predict(X_train_reshape)

mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)

print(f"""
Mean Squared Error:
  Train: {mse_train:.2f}
  Test : {mse_test:.2f}
  Gap  : {abs(mse_train - mse_test):.2f}
R^2 Score:
  Train: {r2_train:.2f}
  Test : {r2_test:.2f}
      """)

"""you can doing modelling using RandomForest Regressor with the same flow like Decision Tree or LinearRegression above :)"""
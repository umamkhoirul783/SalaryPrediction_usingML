# SalaryPrediction_usingML
# Salary Prediction

## Overview

This project aims to predict salary based on years of experience using machine learning models. We explore three different models: Linear Regression, Decision Tree, and Random Forest. The project involves data preprocessing, model training, evaluation, and visualization.

## Dataset

The dataset used for this project contains information about employee salaries and their corresponding years of experience. It is a CSV file named 'salary_data.csv'.

## Models

Three machine learning models were implemented and evaluated:

1. **Linear Regression:** A simple linear model that assumes a linear relationship between experience and salary.
2. **Decision Tree:** A tree-based model that makes predictions based on a series of decision rules.
3. **Random Forest:** An ensemble model that combines multiple decision trees to improve prediction accuracy.

## Evaluation

Model performance was evaluated using the following metrics:

- **Mean Squared Error (MSE):** Measures the average squared difference between predicted and actual values.
- **R-squared:** Represents the proportion of variance in the dependent variable explained by the independent variable.

## Results

Based on the evaluation metrics, the Decision Tree model showed the best performance on the test data, achieving the lowest MSE and highest R-squared. However, it's important to note that the Decision Tree model has a higher tendency to overfit, so further validation and hyperparameter tuning might be necessary.

## Usage

1. Clone this repository: `git clone <repository_url>`
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the Jupyter Notebook: `jupyter notebook Salary_Prediction.ipynb`

## Requirements

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

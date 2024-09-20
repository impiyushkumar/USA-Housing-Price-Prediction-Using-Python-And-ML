# USA Housing Price Prediction Using Python And ML

## Overview
This project focuses on predicting housing prices in the USA based on various features using linear regression. The dataset used, `USA_Housing.csv`, contains information such as average area income, house age, number of rooms, number of bedrooms, and area population.

## Data Exploration
The project involves extensive data exploration and visualization using libraries like `seaborn` and `matplotlib`. Key visualizations include:
- **Pairplot**: To visualize relationships between features.
- **Violin Plot**: To show the distribution of house prices.
- **Displot**: To understand the distribution of a specific feature.

## Linear Regression Model
The project implements a linear regression model to predict house prices. Key coefficients from the model include:
- **Avg. Area Income**: 21.53
- **Avg. Area House Age**: 164,883.28
- **Avg. Area Number of Rooms**: 122,368.68
- **Avg. Area Number of Bedrooms**: 2,233.80
- **Area Population**: 15.15

### Model Evaluation
Predictions are made using the test dataset, and the results are visualized with a scatter plot comparing actual vs. predicted prices.

## Requirements
- Python 3.x
- Libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`


USA_Housing_Price_Prediction/
│
├── data/
│   └── USA_Housing.csv           # Dataset
│
├── notebooks/
│   └── housing_price_analysis.ipynb  # Jupyter notebook for analysis and modeling
│
├── src/
│   └── model.py                  # Python script for running the linear regression model
│   └── visualize.py              # Python script for creating visualizations (pairplot, violin plot,displot)
│
├── README.md                     # Project description and instructions
├── requirements.txt              # Required libraries for the project
└── results/
    └── visualizations/           # Folder to store generated plots (pairplot, violin plot, etc.)
    └── model_output.csv          # Model predictions

## How to Run
1. Clone the repository.
2. Install the required libraries.
3. Load the dataset and run the script to generate visualizations and predictions.

## Conclusion
This project demonstrates the use of data analysis and machine learning techniques to predict housing prices, providing valuable insights for stakeholders in the real estate market.

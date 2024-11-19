# Car Price Prediction App  

### Author: Antony Nzau  

---

## Overview  
The **Car Price Prediction App** is a robust application that leverages machine learning to predict the prices of cars based on their features. This project includes:  

1. **A Dataset**: Curated and preprocessed data containing key attributes of cars like make, model, year, mileage, engine size, and more.  
2. **A Machine Learning Model**: A trained regression model that predicts car prices with high accuracy.  
3. **A User Interface**: An intuitive frontend for users to input car details and get instant price predictions.  

---

## Features  
- **Prediction Accuracy**: The app is powered by a machine learning model trained on a diverse dataset of car features and prices.  
- **User-Friendly Design**: Enter car details into simple input fields and get immediate price predictions.  
- **Customizable**: Easily extend the app to include more features or refine the prediction algorithm.  

---

## Components  

### 1. Dataset  
The dataset contains car records with attributes such as:  
- **Make and Model**  
- **Year of Manufacture**  
- **Mileage**  
- **Fuel Type**  
- **Engine Size**  
- **Transmission**  
- **Location**  
- **Previous Owners**  
- **Car Condition**  
- **Listed Price**  

The data has been cleaned and normalized for accurate predictions, with outliers removed and missing values imputed.  

---

### 2. Model  
The predictive model is built using **Python** and **Scikit-learn**. It employs the **Random Forest Regressor**, which is robust and handles both linear and non-linear relationships.  

#### Key Details:  
- **Input Features**:  
  - Make/Model  
  - Year  
  - Mileage  
  - Fuel Type  
  - Engine Size  
- **Output**: Predicted car price  
- **Evaluation Metrics**:  
  - Mean Absolute Error (MAE): ~2,000 (on validation set)  
  - R-squared Score (R²): 0.92 (on validation set)  

The model has been hyperparameter-tuned using GridSearchCV to optimize performance.  

---

### 3. Application  
The app is built using **Streamlit**, a Python-based framework for creating web applications.  

#### Key Features:  
- Input fields for all necessary car features.  
- A "Predict" button to generate results.  
- An interactive display of the prediction output.  
- Option to visualize the dataset and model performance through plots.  

---

## Installation  

### Requirements  
- Python 3.8 or later  
- Libraries:  
  - Streamlit  
  - Pandas  
  - Numpy  
  - Scikit-learn  
  - Matplotlib  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/AntonyNzau/CarPricePredictionApp.git  
   cd CarPricePredictionApp  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run the app:  
   ```bash  
   streamlit run app.py  
   ```  

---

## Usage  
1. Launch the app.  
2. Fill in the car details on the homepage.  
3. Click the "Predict" button.  
4. View the predicted price on the screen.  

---

## Dataset Details  
The dataset is included in the repository as `car_data.csv`. It contains approximately 10,000 records of car sales with the following schema:  

| Column Name        | Description                              |  
|--------------------|------------------------------------------|  
| Make              | Manufacturer of the car                  |  
| Model             | Specific model of the car                |  
| Year              | Year of manufacture                      |  
| Mileage           | Total distance traveled by the car       |  
| Engine Size       | Size of the car engine in liters         |  
| Transmission      | Type of transmission (Manual/Automatic)  |  
| Fuel Type         | Type of fuel used (Petrol/Diesel/Electric)|  
| Price             | Sale price of the car                    |  

---

## Contributions  
Feel free to contribute to this project! You can:  
- Improve the model's accuracy by using a different algorithm or tuning the parameters.  
- Add more features to the dataset or app interface.  
- Enhance the app's UI/UX.  

To contribute:  
1. Fork the repository.  
2. Make your changes.  
3. Submit a pull request with detailed explanations.  

---

## License  
This project is open-source under the MIT License.  

---

## Contact  
For inquiries or collaboration, please reach out to Antony Nzau at:  
- **Email**: nzauanthony7@gmail.com  
- **GitHub**: Nzau1

---  

Happy Coding! 🚗✨  

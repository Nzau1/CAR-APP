import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder
import os

# Step 1: Load Model and Encoder
# Define the path to the MODELS folder relative to the script's location
models_folder = os.path.join(os.path.dirname(__file__), 'MODELS')
model_path = os.path.join(models_folder, 'car_price_model_1000.pkl')
data_sample_path = os.path.join(models_folder, 'car_specs_1000.csv')

# Load the model
model = joblib.load(model_path)

# Load the sample data to initialize encoder
data_sample = pd.read_csv(data_sample_path)

# Define categorical columns
categorical_cols = ['Brand', 'Color']

# Initialize the encoder
encoder = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
encoder.fit(data_sample[categorical_cols])

# Streamlit App Title
st.title("Car Price Prediction App")
st.write("Fill in the details below to get an estimate of the car's price.")

# Function to process input and make predictions
def predict_car_price(brand, color, seat_capacity, year, horsepower, mileage):
    # Create input DataFrame
    input_data = pd.DataFrame([[brand, color, year, seat_capacity, horsepower, mileage]],
                              columns=['Brand', 'Color', 'year', 'Seat Capacity', 'Horsepower', 'Mileage'])
    try:
        # Encode categorical variables
        encoded_input = encoder.transform(input_data[categorical_cols])
        encoded_df = pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out(categorical_cols))

        # Combine with numerical data
        input_data_processed = pd.concat([input_data.drop(categorical_cols, axis=1), encoded_df], axis=1)

        # Ensure all columns match the trained model input format
        input_data_processed = input_data_processed.reindex(columns=model.feature_names_in_, fill_value=0)

        # Predict using the loaded model
        prediction = model.predict(input_data_processed)

        return f"Estimated Car Price: Kes{prediction[0]:,.2f}"
    except Exception as e:
        return "Error: Unable to make prediction. Please check your inputs."

# Streamlit Input Fields
brand = st.text_input("Car Brand (e.g., Toyota, Ford):")
color = st.text_input("Car Color (e.g., Red, Blue):")
seat_capacity = st.number_input("Seat Capacity (e.g., 2, 5):", min_value=1, max_value=8, step=1)
year = st.number_input("Manufacturing Year (e.g., 2015):", min_value=1900, max_value=2024, step=1)
horsepower = st.number_input("Horsepower (e.g., 150):", min_value=50.0, max_value=1000.0, step=1.0)
mileage = st.number_input("Mileage (e.g., 50000):", min_value=0.0, step=100.0)

# Predict Button
if st.button("Predict Price"):
    if brand and color and seat_capacity and year and horsepower and mileage:
        result = predict_car_price(brand, color, seat_capacity, year, horsepower, mileage)
        st.success(result)
    else:
        st.error("Please fill in all the fields.")

# Footer
st.write("Thank you for using the car price prediction app!")
import streamlit as st
# from pred_backend import predict # for doing predictions using backend without pipelining feature
from pred_backend_with_pipeline import predict # for doing predictions using backend with pipelining feature

# Set layout to wide
st.set_page_config(layout="wide")

# Title for the app
st.title("Passenger Information Input")

# Input fields
st.header("Enter Passenger Details")

with st.form("passenger_form"):
    # Pclass input (integer, options: 1, 2, or 3)
    Pclass = st.selectbox("Pclass (Passenger Class)", [1, 2, 3])

    # Gender input (string: male or female)
    gender = st.radio("Gender", ["male", "female"])

    # Age input (integer between 1 and 100)
    age = st.slider("Age", min_value=1, max_value=100)

    # SibSp input (integer)
    SibSp = st.number_input("SibSp (Number of Siblings/Spouses)", min_value=0, step=1)

    # Parch input (integer)
    Parch = st.number_input("Parch (Number of Parents/Children)", min_value=0, step=1)

    # Fare input (float)
    Fare = st.number_input("Fare (Ticket Fare)", min_value=0.0, format="%.2f")

    # Embarked input (string: S, C, or Q)
    Embarked = st.selectbox("Embarked (Port of Embarkation)", ["S", "C", "Q"])

    # Submit button
    submit = st.form_submit_button("Submit")

# Check if all fields are filled
if submit:
    if Pclass and gender and age and SibSp is not None and Parch is not None and Fare and Embarked:
        # Here is where the backend code for prediction can be executed.
        # For now, we just display the inputs.
        st.success("All fields are filled.")
        st.text(f"Prediction to be done on: Pclass: {Pclass}, Gender: {gender}, Age: {age}, SibSp: {SibSp}, Parch: {Parch}, Fare: {Fare}, Embarked: {Embarked}")
        prediction = predict(Pclass, gender, age, SibSp, Parch, Fare, Embarked)
        st.text(f"Prediction: {prediction}")
    else:
        st.error("Please fill in all the required fields.")

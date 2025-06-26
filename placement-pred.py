import numpy as np
import pickle
import streamlit as st

# Load the trained salary prediction model
loaded_model = pickle.load(open("salary_model.sav", "rb"))

# Define the prediction function
def salary_prediction(input_data):
    input_data_as_numpy_array = np.array(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return round(prediction[0], 2)

# Streamlit app UI
def main():
    gender = {'Male': 1, 'Female': 0}
    ssc_b = {'Central': 1, 'Others': 0}
    hsc_b = {'Central': 1, 'Others': 0}
    hsc_s = {'Commerce': 0, 'Science': 1, 'Arts': 2}
    degree_t = {'Sci&Tech': 0, 'Comm&Mgmt': 1, 'Others': 2}
    workex = {'Yes': 1, 'No': 0}
    specialisation = {'Mkt&HR': 0, 'Mkt&Fin': 1}

    st.title('Placement Salary Prediction Web App')  

    gender_input = st.selectbox("Select Gender", gender)
    ssc_p = st.text_input("Enter SSC Percentage")
    ssc_b_input = st.selectbox("Select SSC Board", ssc_b)
    hsc_p = st.text_input("Enter HSC Percentage")
    hsc_b_input = st.selectbox("Select HSC Board", hsc_b)
    hsc_s_input = st.selectbox("Select HSC Stream", hsc_s)
    degree_p = st.text_input("Enter Degree Percentage")
    degree_t_input = st.selectbox("Select Degree Type", degree_t)
    workex_input = st.selectbox("Work Experience", workex)
    etest_p = st.text_input("Enter E-Test Percentage")
    specialisation_input = st.selectbox("MBA Specialisation", specialisation)
    mba_p = st.text_input("Enter MBA Percentage")

    prediction_result = ''

    if st.button("Predict Salary"):
        try:
            input_data = [
                gender[gender_input],
                float(ssc_p),
                ssc_b[ssc_b_input],
                float(hsc_p),
                hsc_b[hsc_b_input],
                hsc_s[hsc_s_input],
                float(degree_p),
                degree_t[degree_t_input],
                workex[workex_input],
                float(etest_p),
                specialisation[specialisation_input],
                float(mba_p)
            ]
            prediction = salary_prediction(input_data)
            st.success(f'Predicted Salary: ₹ {prediction}')
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")

if __name__ == '__main__':
    main()

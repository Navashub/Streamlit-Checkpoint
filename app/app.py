import streamlit as st
import joblib
import numpy as np 

#load the model 
model = joblib.load('model.pkl')

#Streamlit app

st.title('Customer Churn prediction APP')

# Create input fields for each feature
REGULARITY = st.number_input('REGULARITY')
REGION = st.selectbox('REGION', [0,1,2,3,4,5,6,7,8,9,10,11,12,13])
ON_NET = st.number_input('ON_NET')
DATA_VOLUME = st.number_input('DATA_VOLUME')
ORANGE = st.number_input('ORANGE')
REVENUE = st.number_input('REVENUE')
ARPU_SEGMENT = st.number_input('ARPU_SEGMENT')
MONTANT = st.number_input('MONTANT')
FREQ_TOP_PACK = st.number_input('FREQ_TOP_PACK')
FREQUENCE = st.number_input('FREQUENCE')



# Get inputs as a list and reshape it for prediction
inputs = np.array([[REGULARITY, REGION, ON_NET, DATA_VOLUME, ORANGE, REVENUE, ARPU_SEGMENT, MONTANT, FREQ_TOP_PACK, FREQUENCE]])

# Button for making prediction
if st.button('Predict Churn'):
    prediction = model.predict(inputs)
    if prediction[0] == 1:
        st.write('The customer is likely to churn.')
    else:
        st.write('The customer is not likely to churn.')

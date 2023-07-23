import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pickle
import json

#df = pd.read_csv('mumbai_clean.csv')

pipe = pickle.load(open('pipe3.pkl','rb'))

#Station = '{"Ambernath": 0, "Andheri": 1 , "Bandra": 2, "Bhandup": 3, "Bhayandar": 4, "Borivali": 5, "Byculla": 6, "Chembur": 7, "Chinchpokli": 8, "Dadar": 9, "Dahisar": 10, "Ghatkopar": 11, "Goregaon": 12, "Govandi": 13, "Jogeshwari": 14, "Kalyan": 15, "Kandivali": 16, "Kanjurmarg": 17, "Khar": 18, "Kurla": 19, "Lower Parel": 20, "Mahim": 21, "Malad": 22, "Matunga": 23, "Mazgaon": 24, "Mira Road": 25, "Mulund": 26, "Mumbai Central": 27, "Nahur": 28, "Naigaon": 29, "Nalasopara": 30, "Navi Mumbai": 31, "Parel": 32, "Powai": 33, "Santacruz": 34, "Sewri": 35, "Sion": 36, "Thane": 37, "Tilak Nagar - Harbour Line": 38, "Ulhasnagar": 39, "Vasai": 40,"Vikhroli": 41, "Vile Parle": 42, "Virar": 43}'
#property_type = '{"New Property": 0, "Resale": 1}'
#property = '{"Flat": 0, "Individual House": 1}'
#furnished_status = '{"Furnished": 0, "Semi-Furnished": 1, "Unfurnished": 2}'

#parsed1 = json.loads(Station)
#parsed2 = json.loads(property_type)
#parsed3 = json.loads(property)
#parsed4 = json.loads(furnished_status)

Station = ['Ambernath', 'Andheri', 'Bandra', 'Bhandup', 'Bhayandar',
       'Borivali', 'Byculla', 'Chembur', 'Chinchpokli', 'Dadar',
       'Dahisar', 'Ghatkopar', 'Goregaon', 'Govandi', 'Jogeshwari',
       'Kalyan', 'Kandivali', 'Kanjurmarg', 'Khar', 'Kurla',
       'Lower Parel', 'Mahim', 'Malad', 'Matunga', 'Mazgaon', 'Mira Road',
       'Mulund', 'Mumbai Central', 'Nahur', 'Naigaon', 'Nalasopara',
       'Navi Mumbai', 'Parel', 'Powai', 'Santacruz', 'Sewri', 'Sion',
       'Thane', 'Tilak Nagar - Harbour Line', 'Ulhasnagar', 'Vasai',
       'Vikhroli', 'Vile Parle', 'Virar']

furnished_status = ['Furnished', 'Semi-Furnished', 'Unfurnished']

property_type = ['New Property', 'Resale']

bedrooms = [0,1,2,3,4,5,6,7,8,9,10]

bathrooms = [1,2,3,4,5]

balcony = [0,1,2,3,4,5,6,7,8]

lift = [0,1,2,3,4]

parking = [0,1,2,3]

#st.title('Mumbai Price Prediction')

st.title(':house: Mumbai House Price Prediction :house:')

#Station1 = st.selectbox('Station name',parsed1.keys())
Station1 = st.selectbox('Station name',Station)

col1, col2 = st.columns(2)

with col1:
    #property_type1 = st.selectbox('Property Type',parsed2.keys())
    property_type1 = st.selectbox('Property Type',property_type)
with col2:
    #furnished_status1 = st.selectbox('Furnished Status',parsed4.keys())
    furnished_status1 = st.selectbox('Furnished Status',furnished_status)

col4, col5, col6 = st.columns(3)

with col4:
    area = st.number_input('Area (in sqft)')
with col5:
    bedrooms = st.selectbox('Bedrooms',bedrooms)
with col6:
    bathrooms = st.selectbox('Bathrooms',bathrooms)

col7, col8, col9 = st.columns(3)

with col7:
    balcony = st.selectbox('Balcony',balcony)
with col8:
    lift = st.selectbox('Lift',lift)
with col9:
    parking = st.selectbox('Parking',parking)

price_sqft = st.number_input('Price per sqft (in rupees)')


if st.button('Predict Score'):
    
    input_df = pd.DataFrame(
     {'area': [area], 'Bedrooms': [bedrooms],'Bathrooms':[bathrooms], 'Balcony': [balcony], 'neworold': [property_type1], 
      'parking': [parking],  'Furnished_status': [furnished_status1], 'Lift': [lift], 'Price_sqft': [price_sqft], 'City_area': [Station1]})
    
    result = pipe.predict(input_df)
    st.header("Predicted House Price - Rs " + str(int(result[0])))


#str(int(result[0]))

#2000.0	3.0	3.0	1.0	2.0	1.0	Resale	Unfurnished	Flat	14750.000000	Jogeshwari
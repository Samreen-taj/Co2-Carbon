#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:56:42 2023

@author: sunilnandipati
"""


import numpy as np
import pickle
import streamlit as st

#!pip install st-annotated-text 
from annotated_text import annotated_text


# loading the saved model
#loaded_model = pickle.load (open ('/Users/sunilnandipati/Desktop/MLProjects/trained_model.sav', 'rb'))

pipe = pickle.load (open ('/Users/sunilnandipati/Desktop/MLProjects/pipe.pkl', 'rb'))

def perform_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    #input_data_as_numpy_array = input_data_as_numpy_array.astype('float64')
    
    input_data_as_numpy_array = input_data_as_numpy_array.astype('object')
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, 8)


    prediction = pipe.predict(input_data_reshaped)
    return prediction    



#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown (f"‹style›{f.read()}</style>", unsafe_allow_html=True)



def main() :
    

    #local_css('/Users/sunilnandipati/Desktop/MLProjects/style.css')
    
    # giving a title
    
    st.sidebar.header ("MISSION: Reduce Co2 emissions")
    #st.write ("This is **just** a **_test_**")

    
    st.sidebar.image('/Users/sunilnandipati/Desktop/MLProjects/co2_emi_img.jpg', width=250)
    
    st.sidebar.write ("Various factors contribute to Co2 emissions like:")
    st.sidebar.write ("**Fuel Type**")
    st.sidebar.write ("**Transmission Type**")
    st.sidebar.write ("**Size of the car**")
    st.sidebar.write ("**And of course, MILES TRAVELLED!!**")
    with st.sidebar:
        #annotated_text (("Go.. Check your car" ,"------>>>>","#ffda00 "),)  
        #annotated_text (("Go.."," Check your car ------>>>>","#2966b7"),)  
        annotated_text (("Go.."," Check your car ------>>>>","#FF4B4B"),)  
      
    
    st.title( 'Predict your Co2 Emission')
    
    st.write("---")
    
    
    #make = st.radio ('Select Make Type', ['Luxury', 'Premium', 'Sports', 'General'], index=1)
    
    # getting the input data from the user
    
    maketype, vehclass = st.columns ([2,2])
    with maketype:
        make = st.selectbox(label = "Choose Make Type", options = ['Luxury', 'Premium', 'Sports', 'General'])
    with vehclass:
        veh_cls = st.selectbox(label = "Choose Vehicle Class Type", options = ['Hatchback', 'SUV', 'Sedan', 'Truck'])
    
    #make = st.selectbox(label = "Choose Make Type", options = ['Luxury', 'Premium', 'Sports', 'General'])
    
    
 #   if make == "Luxury" :
 #       st.write("ACURA, BENTLEY, LINCOLN, ROLLS-ROYCE, GENESIS")
 #   if make == "Premium" :
 #       st.write("ALFA ROMEO, AUDI, BMW, BUICK, CADILLAC, CHRYSLER, DODGE, GMC, INFINITI, JEEP, LAND ROVER, LEXUS, MERCEDES-BENZ, MINI, SMART, VOLVO")
 #   if make == "Sports" :
 #       st.write("ABUGATTI, PORSCHE, MASERATI, ASTON MARTIN, LAMBORGHINI, JAGUAR, SRT")
 #   if make == "General" :
 #       st.write("CHEVROLET, FIAT, FORD, KIA, HONDA, HYUNDAI, MAZDA, MITSUBISHI, NISSAN, RAM, SCION, SUBARU, TOYOTA, VOLKSWAGEN")
        

    enginesz, cylinder, fuelcity, fuelhwy = st.columns ([1,1,2,2])
    with enginesz:
        eng_sz = st.text_input('Engine Size')
    with cylinder:
        cyln = st.text_input('Cylinder')
    with fuelcity:
        fuel_city = st.text_input('Stuck in Traffic  l/100km')
    with fuelhwy:
        fuel_hwy = st.text_input('Long Drives  l/100km')


    
    #transm = st.text_input ( 'Transmission')
    transm = st.selectbox(label = "Choose Transmission Type", options = ['AS','AM', 'AV','M','A'])
    
    #fuel_type = st.text_input ( 'Fuel Type')
    fuel_type = st.selectbox(label = "Choose Fuel Type", options = ['Z','D', 'X','E','N'])
    
                                                                              
    #code for Prediction
    output = 0
    
    
    # creating a button for Prediction
    if st.button( 'Display Results in g/km'):
        output = perform_prediction([eng_sz, cyln, transm, fuel_type, fuel_city, fuel_hwy, make, veh_cls])
                                       
     
    #st.text(output)                     
    st.success(output)
    
    
    if output < 150:
        annotated_text (("Nice" ,"car","#633d92"),)
    else:
        annotated_text (("Need to" ,"Improve","#FF4B4B"),)
    #("All" ,"Done", "#FF4B4B"),  
    #"Good" ,"Job","#faa")                     
    

if __name__ == '__main__':
    main()
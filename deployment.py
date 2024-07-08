import streamlit as st
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


import pickle

model = pickle.load(open(r"lr.pkl","rb"))

squarefeet = st.number_input("Enter the size of the house",min_value =600,max_value = 5000,step =50)
Bedrooms = st.number_input("Enter the number of bedrooms",min_value = 0,max_value = 5,step = 1)
bathrooms = st.number_input("Enter the number of bathrooms",min_value = 0,max_value = 5, step = 1)
Neighbourhood = st.radio("Enter the neighbourhood",["Rural","Urban","Suburb"])
neighbour = 1 if Neighbourhood=="Rural" else 2 if Neighbourhood == "Urban" else 3
Yearbuilt = st.number_input("Enter the year of construction",min_value = 1900,max_value = 2030,step =1)
price = model.predict([[squarefeet,Bedrooms,bathrooms,neighbour,Yearbuilt]])
st.write("The price of the plot for the given details is Rs.",price)
st.button("Predicted Price")




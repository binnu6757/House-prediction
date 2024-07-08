import streamlit as st
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


import pickle

model = pickle.load(open(r"C:\Users\reddy\lr.pkl","rb"))

squarefeet = st.number_input("Enter the size of the house",min_value =600,max_value = 5000,step =50)
Bedrooms = st.number_input("Enter the number of bedrooms",min_value = 0,max_value = 5,step = 1)
bathrooms = st.number_input("Enter the number of bathrooms",min_value = 0,max_value = 5, step = 1)
Neighbourhood = st.radio("Enter the neighbourhood",["Rural","Urban","Suburb"])
neighbour = 1 if Neighbourhood=="Rural" else 2 if Neighbourhood == "Urban" else 3
Yearbuilt = st.number_input("Enter the year of construction",min_value = 1900,max_value = 2030,step =1)
numeric_data = [["squarefeet","Bedrooms","bathrooms","neighbour","Yearbuilt"]]

numeric_data = np.array([[1500, 3, 2, 1, 2005]])

price = model.predict(numeric_data)

st.write("The Price for given flat details is Rs.",price)
import pickle
import pandas as pd
import streamlit as st
from PIL import Image



lst = [[90, 44, 38, 28.4343, 83.43243, 7.432432, 241.4242]]
    
# df = pd.DataFrame(lst, columns =['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

# print(df)
st.set_page_config(page_title="CropRec")

st.title('Crop Recommendation System')

st.sidebar.subheader("Enter the Following Info")

N = st.sidebar.number_input('Nitrogen')
st.sidebar.text('mg(s) of Nitrogen / kg of Soil')
P = st.sidebar.number_input('Phosphorus')
st.sidebar.text('mg(s) of Phosphorus / kg of Soil')
K = st.sidebar.number_input('Potassium')
st.sidebar.text('mg(s) of Potassium / kg of Soil')
temp = st.sidebar.number_input('Temperature')
st.sidebar.text('in °C')
hum = st.sidebar.number_input('Humidity')
st.sidebar.text('relative humidity in %')
ph = st.sidebar.number_input('PH')
st.sidebar.text('ph value of the soil')
rainfall = st.sidebar.number_input('Rainfall')
st.sidebar.text('MM')


lst2 = [[N, P , K, temp, hum, ph, rainfall]]

model_crop = pickle.load(open('model_crop.pkl', 'rb'))
x = model_crop.predict(lst2)

def numbers_to_strings(argument):
    switcher = {
        20: "rice",
        11: "maize",
        3: "chickpea",
        9: "kidneybeans",
        18: "pigeonpeas",
        13: "mothbeans",
        14: "mungbean",
        2: "blackgram",
        10: "lentil",
        19: "pomegranate",
        1: "banana",
        12: "mango",
        7: "grapes",
        21: "watermelon",
        15: "muskmelon",
        0: "apple",
        16: "orange",
        17: "papaya",
        4: "coconut",
        6: "cotton",
        8: "jute",
        5: "coffee"
    }

    return switcher.get(argument, "nothing")

captionx = numbers_to_strings(x[0])

image = Image.open('images/' + str(x[0]) + '.jpg')
st.image(image, caption=captionx, width = 500)

print(x)
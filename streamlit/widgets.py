import streamlit as st 
import pandas as pd
st.title('Streamlit text input')

name=st.text_input('Enter your name :')

if name:
    st.write('Hello ', name)
    
age=st.slider('Select your age :' ,0,100,25)
# 0-> start 100-> end 25->minimum age that slider will show
st.write('Your age is ', age)
    
options=['Java', 'Python' , 'C', 'C++']
lang=st.selectbox('Choose your favourite language :', options)
st.write('Your favourite language is :', lang)

df=pd.DataFrame(
    {
        'col1': [1,2,3,4],
        'col2' :[4,5,6,8]
    }
)
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file=st.file_uploader('Choose a CSV file ', type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    
    
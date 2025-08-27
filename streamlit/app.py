import streamlit as st 
import pandas as pd 
import numpy as np 

st.title('Hello streamlit')

# display a simple text
st.write('This is a simple text')

#create a simple dataframe
df=pd.DataFrame(
    {
        'col1': [1,2,3,4],
        'col2' :[4,5,6,8]
    }
)

st.write('This is a dataframe')
st.write(df)

#create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)

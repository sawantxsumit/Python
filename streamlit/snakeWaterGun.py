import streamlit as st 


# snake =1
# water =-1
# gun =0
# snake vs water : snakes drinks water ->snake wins
# gun vs water : gun drowns in water -> water wins
# gun vs snake : gun kills the snake -> gun wins

import random
computer =random.choice([-1 , 1 ,0])

st.write("RULES OF THE GAME")
st.write("Snake vs Water : snakes drinks water ->snake wins")
st.write("Gun vs Water : gun drowns in water -> water wins")
st.write("Gun vs Snake : gun kills the snake -> gun wins")

options=['snake','water','gun']
str=st.selectbox("SNAKE WATER or GUN \n choose one :",options)
dict={"snake" :1 , "water": -1 , "gun": 0}
revdict={value : key for key , value in reversed(dict.items())}
you=dict[str]
st.write("computer chose" , revdict[computer])

if((computer - you)== -1 or (computer - you)== 2):
    st.write("you lose")
else:
    st.write("you win")
    



import streamlit as st
#use of slider
st.header('Slider day4')
st.subheader('slider')

age = st.slider('How old are you ?',0,130,25)
st.write('I am ',age,'years old.')


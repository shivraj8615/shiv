import streamlit as st
st.header('#30 days of streamlit day2')
st.header('st.button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

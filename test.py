import streamlit as st
import pandas as pd
from plots import *

data = pd.read_csv('student-mat.csv', sep=';')
pd.set_option('display.max_columns',None)

st.markdown('## My First Awesome App ')

sex = ['M','F','Population']          
option_two = st.sidebar.selectbox('choose your filter based on gender: ', sex)
if option_two == 'M' or option_two =='F':
    gender = data.loc[data['sex'] == option_two]
else:
    gender = data

fig_alpha = draw_hist(gender)
fig_beta = draw_scatter(gender)
fig_gamma = draw_animscatter(gender)
fig_delta = draw_funnel(gender)
fig_eta = draw_3dfig(gender)


lst = ('No Selection', 'Histogram', 'Scatter', 'Animated Scatter', 'Funnel', '3D Figure')
option = st.selectbox('Choose your style: ', lst)

if option == 'Histogram':
    st.plotly_chart(fig_alpha, use_container_width=True)
    button = st.button('Description')
    if button:
        st.text('This my graph negger!')
if option == 'Scatter':
    st.plotly_chart(fig_beta, use_container_width=True)
if option == 'Animated Scatter':
    st.plotly_chart(fig_gamma, use_container_width=True)
if option == 'Funnel':
    st.plotly_chart(fig_delta, use_container_width=True)
if option == '3D Figure':
    st.plotly_chart(fig_eta, use_container_width=True)
    



    
    




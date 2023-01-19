
import pickle
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit_authenticator as stauth
import altair as alt

st.title("Avyattana's favorite number")
st.write("The numbers are started from 1 to 30 with each number has its own meaning and explanation")

## Load Dataframe
excel_file = 'Avy_fav_numbers.xlsx'
sheet_name = 'Sheet1'
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:C',
                   header=4)

df_pick = df.drop('Level', axis = 1)

#---- FILTER DATAFRAME BASED ON WHAT WE SELECT
st.sidebar.header("Pick the filters :")
opt_level = df['Level'].unique()
level = st.sidebar.multiselect(
    "Select The Preference Level:",
    options= df['Level'].unique(),
    default= df['Level'].unique()
)
df_selection = df.query('Level==@level')
st.dataframe(df_selection)  # To show the filters

#--- line Chart from the level of interest in number
df_level = df.groupby(by=['Level']).count()
df_level_chart = df_level.drop('Meaning', axis = 1)

line_figure = px.line(
    df_level_chart,
    labels= {df_level_chart.index.name: 'Level of Interest',  # index.name was level
             df_level_chart.columns[0]: 'Amount of interest'}, # columns[0] was the number
    color_discrete_sequence= ["#d8576b"]
)
st.plotly_chart(line_figure, use_container_width=True)

#---- FILTERING THE PICKED NUMBER BASED ON WHAT WE SELECT
pick_number = st.sidebar.number_input(
    "Select the number:",
    value=27,
    step=1
)
df_selection2 = df[df['Number'] == pick_number]
st.dataframe(df_selection2)


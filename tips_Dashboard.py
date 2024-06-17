# importing libraries
import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# must be first commend 
st.set_page_config(page_title="Tips Visualization Project" , layout="wide" ,page_icon=":bar_chart:")

df= pd.read_csv("tip.csv")
# sidebar
with st.sidebar:
    st.header("Tips Dashbosrd")
    st.image("tip.jpg")
    st.write("filltering you data :")
    categ_col=df.select_dtypes("object").columns.tolist()
    num_col =df.select_dtypes("number").columns.tolist()
    categ_filter = st.selectbox("Categorical" ,categ_col , index=None)
    num_filter = st.selectbox("Numerical" ,num_col ,index=None)
    raw_filter = st.selectbox("Raw filter" ,categ_col ,index=None)
    col_filter = st.selectbox("colum filter" ,categ_col ,index=None)



    st.markdown("Made with :stuck_out_tongue_winking_eye: by Eng . [Reda Mekky](www.linkedin.com/in/reda-mekky-1ba901181) ")


# Body
# Raw  1
col1,col2 , col3 ,col4 = st.columns(4)

col1.metric("Max . Total Bill" , df["total_bill"].max())
col2.metric("min . Total Bill" , df["total_bill"].min())
col3.metric("Max . tip" , df["tip"].max())
col4.metric("min . Tip" , df["tip"].min())

# Raw 2
st.subheader("Total Bill VS Tips")
fig =px.scatter(data_frame=df ,x="total_bill",
                y="tip",
                color=categ_filter ,
                size=num_filter ,
                facet_col=col_filter,
                facet_row=raw_filter)
st.plotly_chart(fig , use_container_width=True)

# Raw 3
c1 ,c2 ,c3 =st.columns((4,3,3))
with c1:
    fig=px.bar(data_frame=df , x="sex",
               y="total_bill",
               color=categ_filter)
    st.plotly_chart(fig , use_container_width=True)
with c2:
     fig=px.pie(data_frame=df , names="smoker",values="tip",
               color=categ_filter)
     st.plotly_chart(fig , use_container_width=True)
with c3:
    fig=px.pie(data_frame=df , names="day",values="tip",
               color=categ_filter,
               hole=.4)
    st.plotly_chart(fig , use_container_width=True)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#1. configure the page 

st.set_page_config(
    page_title="data science app",
    page_icon="&&",
    layout="centered"
)



#2. load the data
#@st.cache()
@st.cache_data
def load_data():
    url='data/Top_rated_movies1.csv'
    df=pd.read_csv(url,parse_dates=['release_date'])
    return df



#3. build the ui

st.title("Data Science")
with st.spinner("loading data...."):
    df=load_data()



st.header("IMDB")
st.info("kbjsdkdjn")
st.dataframe(df,use_container_width=True)




#4. add some graph and widgets
st.header("basic data visualization")
gop=['bar','line','area']


c1,c2=st.columns(2)
sel_op=c1.selectbox("select the type of plot for popularity",gop)
subset=df.sort_values(by='popularity')[:50]


if sel_op==gop[0]:
    #subset=df.sort_values(by='popularity')[:100]
    fig=px.bar(subset,x='title',y='popularity')
elif sel_op==gop[1]:
    #subset=df.sort_values(by='popularity')[:100]
    fig=px.line(subset,x='title',y='popularity')
elif sel_op==gop[2]:
    #subset=df.sort_values(by='popularity')[:100]
    fig=px.area(subset,x='title',y='popularity')
c1.plotly_chart(fig,use_container_width=True)





sel_op2=c2.selectbox("select the type of plot for vote count",gop)
subset=df.sort_values(by='vote_count')[:50]


if sel_op2==gop[0]:
    #subset=df.sort_values(by='popularity')[:100]
    fig=px.bar(subset,x='title',y='vote_count')
elif sel_op2==gop[1]:
    #subset=df.sort_values(by='popularity')[:100]
    fig=px.line(subset,x='title',y='vote_count')
elif sel_op2==gop[2]:
    #subset=df.sort_values(by='popularity')[:100]
    fig=px.area(subset,x='title',y='vote_count')
c2.plotly_chart(fig,use_container_width=True)










#c1.plotly_chart(fig,use_container_width='True')        


#5. adjust layout

t1,t2=st.tabs(["Bivariate","Trivariate"])
num_cols=df.select_dtypes(include=np.number).columns.tolist()
with t1:
    c1,c2=st.columns(2)
    col1=c1.radio("select the first column for scatter plot",num_cols)
    col2=c2.radio("select the second column for 3rd plot",num_cols)
    # col3=st.radio("select the first column for 3rd plot",num_cols)
    fig=px.scatter(df,x=col1,y=col2,title=f'{col1} vs {col2}')
    st.plotly_chart(fig,use_container_width=True)

with t2:
    c1,c2,c3=st.columns(3)
    col1=c1.selectbox("select the first column for scnatter plot",num_cols)
    col2=c2.selectbox("select the second column for 3rd plot",num_cols)
    col3=c3.selectbox("select the third column for 3rd plot",num_cols)
    fig=px.scatter_3d(df,x=col1,y=col2,z=col3,title=f'{col1} vs {col2} vs{col3}',height=700)
    st.plotly_chart(fig,use_container_width=True)
#6. how to run app
#7. open terminal and run:
#8. stramlit run main.py



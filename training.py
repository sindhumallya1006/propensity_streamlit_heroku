# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:44:41 2021

@author: Sindhu Mallya
"""

import streamlit as st
import pandas as pd
#import altair as alt
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

def app():
    #Header
    st.write("Training data used")
    #Reading the data
    training_sample_subset=pd.read_csv("training_sample_subset.csv")
    #display the data
    st.write(training_sample_subset.head(3))
    #header
    st.write("Distribution of Orders (Dependent variable)")
    #plot
    temp=training_sample_subset["ordered"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(["Not ordered","Ordered"],temp,color ='maroon')
    plt.xlabel("Order status")
    plt.ylabel("No. of customers")
    st.pyplot()
    
    

    
    
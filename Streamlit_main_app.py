# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import training
import predict

st.title("Customer Propensity to Purchase")

page_choices={"Know more about the training data":training,
              "Predict the Propensity of Purchase":predict}

page_selection = st.radio("Go to", list(page_choices.keys()))

page = page_choices[page_selection]

with st.spinner(f'Loading {page_selection} ...'):
    page.app()


# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:56:14 2025

@author: Marqu
"""

import streamlit as sl

sl.set_page_config(page_title="Times",
                   page_icon="⚽",
                   layout="wide")

df = sl.session_state["dados"]

clubes = df["Club"].unique()
clube_sb = sl.sidebar.selectbox("Selecione um clube", clubes)
df1 = df[df["Club"] == clube_sb]

sl.image(df1.iloc[0]["Club Logo"])
sl.markdown(f"# {clube_sb}")

colunas = ["Nationality",
           "Overall",
           "Club",
           "Age",
           "Photo",
           "Joined",
           "Contract Valid Until",
           "Flag",
           "Wage(£)",
           "Height(cm.)",
           "Weight(lbs.)"]

sl.dataframe(df1[colunas], column_config={"Overall" : sl.column_config.ProgressColumn(), 
                                          "Photo" : sl.column_config.ImageColumn(),
                                          "Flag" : sl.column_config.ImageColumn()})
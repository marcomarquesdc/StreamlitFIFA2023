# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:15:53 2025

@author: Marqu
"""

#Importação de bibliotecas
import streamlit as sl
import pandas as pd

# Importando dataframe referente ao ano de 2023 utilizando cacheamento 
if "dados" not in sl.session_state :
    df = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv")
    sl.session_state["dados"] = df
    

# Adicionando um título a nossa homepage e descrições sobre o dataset
sl.markdown("# FIFA 2023 OFFICIAL DATASET ⚽")
sl.sidebar.markdown("Desenvolvido por:\nMarco Marques de Castro")
sl.markdown("Link do dataset no Kaggle: [Clique aqui.](https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data)")
sl.markdown("""
            **CONTEXT**

The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. 
The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. 
With over 17,000 records, this dataset offers a valuable resource for football analysts, researchers, and 
enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player 
attributes, performance metrics, market valuation, club analysis, player positioning, 
and player development over time.
            """)

# Exibindo dados por um botao
botao_exibe_dados = sl.button("Clique aqui para exibir os dados")
if botao_exibe_dados :
    sl.write(sl.session_state["dados"])
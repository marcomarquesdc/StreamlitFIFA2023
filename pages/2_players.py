# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:55:38 2025

@author: Marqu
"""

#Importação de bibliotecas
import streamlit as sl

# Configuração da página
sl.set_page_config(page_title="Jogadores",
                   page_icon="🏃‍♂️",
                   layout="wide")
        
# Importando dados através do cacheamento
df = sl.session_state["dados"]

# Criando selectbox na sidebar para clube e jogador
clubes = df["Club"].unique()
clube_sb = sl.sidebar.selectbox("Selecione um clube", clubes)
df1 = df[df["Club"] == clube_sb]

nomes = df1["Name"].unique()
nome_sb = sl.sidebar.selectbox("Jogador", nomes)
df2 = df1[df1["Name"] == nome_sb]

# Criando variável para guardar as informações do jogador selecionado
jogador_info = df2.iloc[0]

# Exibindo informações do jogador selecionado
sl.image(jogador_info["Photo"])
sl.subheader(jogador_info["Name"])
sl.markdown(f"**Clube** : {jogador_info['Club']}")
sl.markdown(f"**Posição** : {jogador_info['Position']}")

c1, c2, c3, c4 = sl.columns(4)
c1.markdown(f"**Idade** : {jogador_info['Age']}")
c2.markdown(f"**Altura (cm)** : {jogador_info['Height(cm.)']}")
c3.markdown(f"**Peso (kg)** : {jogador_info['Weight(lbs.)'] * 0.453:.2f}")
sl.divider()

sl.subheader(f"Geral : {jogador_info['Overall']}")
sl.progress(int(jogador_info["Overall"]))

c1, c2, c3, c4 = sl.columns(4)
c1.metric(label="Valor de mercado", value=f"£ {jogador_info['Value(£)']}")
c2.metric(label="Remuneração semanal", value=f"£ {jogador_info['Wage(£)']}")
c3.metric(label="Cláusula de recisão", value=f"£ {jogador_info['Release Clause(£)']}")




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heart_failure.csv")
st.dataframe(df)

plt.rcParams['font.family'] = 'Malgun Gothic' # Windows
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("heart_failure.csv")

st.sidebar.header("필터")
age = st.sidebar.slider("최대 나이", 40, 90, 70)

df = df[df['age'] <= age]

c1, c2 = st.columns(2)
c1.metric("환자 수", len(df))
c2.metric("평균 나이", f"{df.age.mean():.0f}")

tab1, tab2 = st.tabs(["표", "차트"])
with tab1:
    st.dataframe(df)
with tab2:
    fig, ax = plt.subplots()
    ax.hist(df['age'])
    st.pyplot(fig)
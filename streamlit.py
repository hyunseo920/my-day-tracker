import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("나의 하루 기록하기")

# 활동 시간 입력
study = st.number_input("공부한 시간 (시간)", min_value=0.0, max_value=24.0, step=0.5)
youtube = st.number_input("유튜브 본 시간 (시간)", min_value=0.0, max_value=24.0, step=0.5)
sleep = st.number_input("잠 잔 시간 (시간)", min_value=0.0, max_value=24.0, step=0.5)

# 저장 버튼
if st.button("기록 저장"):
    df = pd.DataFrame({
        "활동": ["공부", "유튜브", "수면"],
        "시간": [study, youtube, sleep]
    })
    st.write("📊 당신의 시간 분포:")
    fig, ax = plt.subplots()
    ax.pie(df["시간"], labels=df["활동"], autopct="%1.1f%%")
    st.pyplot(fig)

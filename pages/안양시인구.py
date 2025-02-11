import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib  # 한글 폰트 설정

# 데이터 로드 (예제 데이터)
data = pd.DataFrame({
    "연령대": ["10대", "20대", "30대", "40대", "50대", "60대"],
    "남성": [50000, 60000, 55000, 52000, 49000, 45000],
    "여성": [48000, 57000, 53000, 51000, 47000, 44000]
})

# 페이지 제목
st.title("📊 안양시 인구 분포")

# 세대별 인구 분포 시각화 (막대그래프)
fig, ax = plt.subplots()
data.plot(x="연령대", kind="bar", stacked=False, ax=ax, color=["blue", "red"])
ax.set_ylabel("인구수")
ax.set_title("세대별 인구 분포")
st.pyplot(fig)

# 선택된 세대 확인
selected_age = st.selectbox("세대를 선택하세요", data["연령대"])

# 성별 분포 표시 (원형그래프)
if selected_age:
    selected_data = data[data["연령대"] == selected_age].iloc[:, 1:3]
    fig, ax = plt.subplots()
    ax.pie(selected_data.values[0], labels=["남성", "여성"], autopct="%1.1f%%", colors=["blue", "red"])
    ax.set_title(f"{selected_age} 성별 분포")
    st.pyplot(fig)

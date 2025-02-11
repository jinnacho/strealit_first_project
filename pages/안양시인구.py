import streamlit as st
import pandas as pd
import plotly
print(plotly.__version__)  # plotly 버전 확인


# 데이터 로드 (예제 데이터)
data = pd.DataFrame({
    "연령대": ["10대", "20대", "30대", "40대", "50대", "60대"],
    "남성": [50000, 60000, 55000, 52000, 49000, 45000],
    "여성": [48000, 57000, 53000, 51000, 47000, 44000]
})

# 페이지 제목
st.title("📊 안양시 인구 분포")

# 세대별 인구 분포 시각화
fig = px.bar(data, x="연령대", y=["남성", "여성"], barmode="group", title="세대별 인구 분포")
st.plotly_chart(fig)

# 선택된 세대 확인
selected_age = st.selectbox("세대를 선택하세요", data["연령대"])

# 성별 분포 표시
if selected_age:
    selected_data = data[data["연령대"] == selected_age].melt(id_vars=["연령대"], var_name="성별", value_name="인구수")
    fig_pie = px.pie(selected_data, names="성별", values="인구수", title=f"{selected_age} 성별 분포", hole=0.3)
    st.plotly_chart(fig_pie)

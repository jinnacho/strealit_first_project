import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("인구 분석 도구")

# File Upload
uploaded_file = st.file_uploader("인구 데이터를 포함한 .txt 파일을 업로드하세요", type=["txt"])

if uploaded_file is not None:
    # Load data into a DataFrame
    df = pd.read_csv(uploaded_file, sep=",", encoding="utf-8")

    # Show raw data
    st.subheader("원본 데이터")
    st.write(df.head())

    # 데이터 전처리
    st.subheader("데이터 전처리")
    if '행정구역' in df.columns:
        df['행정구역'] = df['행정구역'].str.strip()
        st.write("행정구역 정보가 정리되었습니다.")
    else:
        st.warning("'행정구역' 열이 데이터에 포함되어 있지 않습니다. 데이터 구조를 확인하세요.")

    # 연령대별 데이터 분석
    st.subheader("연령대별 인구 분석")
    age_columns = [col for col in df.columns if "계_" in col and "세" in col]

    if age_columns:
        age_data = df[age_columns].sum()
        age_data.index = age_data.index.str.extract(r'계_(.*)')[0]

        # Plot age distribution
        plt.figure(figsize=(10, 5))
        age_data.plot(kind="bar", color="skyblue")
        plt.title("연령대별 인구 분포")
        plt.xlabel("연령")
        plt.ylabel("인구수")
        st.pyplot(plt)
    else:
        st.warning("연령대별 데이터를 찾을 수 없습니다.")

    # 지역별 인구 분석
    st.subheader("지역별 총 인구 분석")
    if '2008년02월_계_총인구수' in df.columns:
        regional_data = df[['행정구역', '2008년02월_계_총인구수']].copy()
        regional_data['2008년02월_계_총인구수'] = regional_data['2008년02월_계_총인구수'].str.replace(',', '').astype(int)
        regional_data = regional_data.sort_values('2008년02월_계_총인구수', ascending=False).head(10)

        # Plot regional population
        plt.figure(figsize=(10, 5))
        plt.barh(regional_data['행정구역'], regional_data['2008년02월_계_총인구수'], color="orange")
        plt.xlabel("총 인구수")
        plt.ylabel("행정구역")
        plt.title("상위 10개 지역 총 인구수")
        st.pyplot(plt)
    else:
        st.warning("총 인구 데이터를 찾을 수 없습니다.")

import streamlit as st
import pandas as pd

# 책 데이터 불러오기 (간단히 예시 데이터로)
book_data = {
    "subject": ["국어", "국어", "영어", "영어", "수학", "수학", "과학", "과학"],
    "title": ["토지", "난중일기", "The Great Gatsby", "1984", "수학의 정석", "미적분학 개론", "과학혁명의 구조", "브리태니커 과학"],
    "author": ["박경리", "이순신", "F. Scott Fitzgerald", "George Orwell", "홍성대", "이우영", "Thomas Kuhn", "브리태니커"],
    "level": ["고급", "초급", "중급", "고급", "중급", "고급", "고급", "초급"]
}

# 데이터프레임으로 변환
df = pd.DataFrame(book_data)

# 제목과 설명
st.title("고등학생 맞춤형 책 추천")
st.write("과목을 선택하고, 관련된 추천 책을 확인해보세요!")

# 과목 선택
subject = st.selectbox("과목을 선택하세요", df["subject"].unique())

# 선택된 과목에 맞는 책 필터링
filtered_books = df[df["subject"] == subject]

# 추천 책 리스트 표시
st.write(f"**{subject} 과목 추천 책 리스트**")
for index, row in filtered_books.iterrows():
    st.write(f"**{row['title']}** (저자: {row['author']}, 난이도: {row['level']})")

import streamlit as st
st.header('안녕! 스트림릿!')
st.write('반가워')


# MBTI 설명 데이터
mbti_data = {
    "INTJ": {
        "description": "전략적인 사고와 계획을 중시하는 INTJ는 분석력과 창의력을 바탕으로 문제를 해결합니다.",
        "careers": "과학자, 엔지니어, 프로젝트 매니저, 데이터 분석가",
        "compatible": "논리적이고 성장 지향적인 사람"
    },
    "ENTP": {
        "description": "호기심 많고 창의적인 ENTP는 새로운 아이디어를 탐구하고 도전하는 것을 즐깁니다.",
        "careers": "기업가, 마케팅 전문가, 컨설턴트, 변호사",
        "compatible": "유연하고 대화가 잘 통하는 사람"
    },
    "ISFJ": {
        "description": "헌신적이고 세심한 ISFJ는 타인을 돕고 실질적인 도움을 제공하는 데 능숙합니다.",
        "careers": "간호사, 교사, 사회복지사, 행정직",
        "compatible": "따뜻하고 신뢰할 수 있는 사람"
    },
    "ENFP": {
        "description": "열정적이고 외향적인 ENFP는 창의성과 에너지가 넘치며 사람들과의 교류를 즐깁니다.",
        "careers": "예술가, 작가, 상담사, 이벤트 플래너",
        "compatible": "열정적이고 자유로운 사람"
    }
    # 추가 MBTI 유형에 대한 데이터를 여기에 추가하세요.
}

# Streamlit 앱 생성
st.title("MBTI 기반 직업 및 궁합 추천")

# MBTI 선택 드롭다운
selected_mbti = st.selectbox(
    "자신의 MBTI 유형을 선택하세요:",
    options=list(mbti_data.keys())
)

# 선택된 MBTI에 대한 정보 표시
if selected_mbti:
    st.subheader(f"{selected_mbti} 유형에 대한 설명")
    st.write(mbti_data[selected_mbti]["description"])

    st.subheader("추천 직업")
    st.write(mbti_data[selected_mbti]["careers"])

    st.subheader("잘 맞는 사람")
    st.write(mbti_data[selected_mbti]["compatible"])

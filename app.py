
import streamlit as st
import pandas as pd
import datetime
import io

st.set_page_config(page_title="근골격계 부담작업 체크리스트", layout="wide")
st.title("📋 근골격계 부담작업 체크리스트 시스템")

st.subheader("✅ 기본 정보 입력")
company = st.text_input("회사명")
department = st.text_input("부서명")
work_name = st.text_input("작업명")
unit_work = st.text_input("단위작업명")
writer = st.text_input("작성자")
write_date = st.date_input("작성일자", value=datetime.date.today())
weight = st.text_input("총중량 (Kg)")

# Example content
st.subheader("예시 항목")
example = st.text_area("작업내용 입력")

# Save example to Excel
if st.button("임시 저장"):
    df = pd.DataFrame([{
        "회사명": company,
        "부서명": department,
        "작업명": work_name,
        "작성자": writer,
        "작업내용": example
    }])
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    st.download_button(
        label="📂 temp_작성자명_날짜.xlsx 다운로드",
        data=buffer.getvalue(),
        file_name=f"temp_{writer}_{write_date}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

import streamlit as st
import streamlit.components.v1 as components
import os

# --- 페이지 설정 ---
# 페이지 레이아웃을 'wide'로 설정하여 넓은 화면을 사용합니다.
st.set_page_config(
    page_title="유치원 교사를 위한 디지털 역량 강화",
    layout="wide"
)

# --- HTML 파일 불러오기 ---
# app.py 파일이 있는 위치를 기준으로 'htmls' 폴더 안의 'index.html' 파일 경로를 지정합니다.
html_file_path = os.path.join('htmls', 'index.html')

# 파일이 존재하는지 확인합니다.
if os.path.exists(html_file_path):
    # 파일을 열고 내용을 읽습니다. UTF-8 인코딩으로 한글 깨짐을 방지합니다.
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_code = f.read()

    # --- Streamlit에 HTML 렌더링 ---
    # st.components.v1.html을 사용하여 HTML 코드를 웹페이지에 표시합니다.
    # height를 충분히 높게 설정하고 scrolling=True로 하여 페이지 전체를 볼 수 있도록 합니다.
    components.html(html_code, height=1500, scrolling=True)

else:
    # 파일이 없을 경우 에러 메시지를 표시합니다.
    st.error(f"'{html_file_path}' 경로에서 HTML 파일을 찾을 수 없습니다.")
    st.warning("app.py 파일과 같은 위치에 'htmls' 폴더를 만들고, 그 안에 'index.html' 파일이 있는지 확인해주세요.")

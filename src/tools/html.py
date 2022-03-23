import streamlit as st

# ----- ----- -----


def render(html_string):
    st.markdown(html_string, unsafe_allow_html=True)


def text(txt, style="", justify=True, margin_bottom=True):
    div_style = "font-size:16px;color:black;"
    if justify:
        div_style += "text-align:justify;"
    if margin_bottom:
        div_style += "margin-bottom:20px;"
    if style:
        div_style += style
    div_style = f' style="{div_style}"'
    st.caption(f"<div{div_style}>{txt}</div>", unsafe_allow_html=True)

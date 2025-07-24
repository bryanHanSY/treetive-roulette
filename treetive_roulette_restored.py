
import streamlit as st
import random
import time

# ---------------------- 설정 ----------------------
names = [
    "에드워드(edward)", "빅(vic)", "레나(rena)", "포드(ford)", "딜런(dylan)", "제제(jeje)", "쿠디(kudi)", "리오(rio)", "쥬니(junney)", "에이든(aiden)",
    "하이디(heidy)", "트루디(trudy)", "아놀드(arnold)", "세레나(serena)", "칼리(kali)", "앨빈(alvin)", "진(jin)", "엠버(amber)", "아나이스(anais)", "아이다(aida)"
]

# ---------------------- 상태 초기화 ----------------------
if "remaining" not in st.session_state:
    st.session_state.remaining = names.copy()
if "last_picked" not in st.session_state:
    st.session_state.last_picked = None

# ---------------------- 스타일 ----------------------
st.set_page_config(page_title="Treetive Roulette", layout="centered")

st.markdown("""
    <style>
    html, body, .main {
        background-color: #000000;
        color: #0ff;
    }
    h1 {
        text-align: center;
        color: #0ff;
    }
    .description {
        text-align: center;
        color: #888;
        margin-bottom: 30px;
    }
    .big-text {
        font-size: 48px;
        font-weight: bold;
        color: #00ffff;
        text-shadow: 0 0 1px #0ff, 0 0 2px #0ff;
        text-align: center;
        margin-top: 30px;
        animation: pulse 1.2s ease-in-out;
    }
    .emoji {
        font-size: 64px;
        text-align: center;
        animation: bounce 1s infinite;
    }
    .stButton>button {
        display: block;
        margin: 0 auto;
        font-size: 18px;
        padding: 0.6em 1.5em;
        background-color: #0ff;
        color: #000;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0 0 10px #0ff;
    }
    .stButton>button:hover {
        background-color: #00dddd;
    }
    @keyframes bounce {
        0%   { transform: translateY(0); }
        50%  { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.9; }
        100% { transform: scale(1); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- 타이틀 ----------------------
st.markdown('<div class="emoji">🎰</div>', unsafe_allow_html=True)
st.markdown('<h1>Treetive Roulette</h1>', unsafe_allow_html=True)
st.markdown('<div class="description">천하제일 AI포코톤</div>', unsafe_allow_html=True)

# ---------------------- 룰렛 실행 ----------------------
if st.button("룰렛 돌리기"):
    if not st.session_state.remaining:
        st.warning("✅ 모든 인원이 추첨 완료되었습니다!")
    else:
        placeholder = st.empty()
        spins = 20
        for i in range(spins):
            spin_name = random.choice(st.session_state.remaining)
            placeholder.markdown(f'<div class="big-text">{spin_name}</div>', unsafe_allow_html=True)
            time.sleep(0.1 + i * 0.01)

        selected = spin_name
        st.session_state.remaining.remove(selected)
        st.session_state.last_picked = selected
        placeholder.markdown(f'<div class="big-text">{selected}</div>', unsafe_allow_html=True)

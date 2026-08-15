import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="One Tiny Question",
    page_icon="🥀",
    layout="centered",
)

# -----------------------------
# Personalize here
# -----------------------------
HER_NAME = "Nadia"          # shows up in the copy — change anytime
MY_PHOTO = "assets/my-photo.jpeg"
HER_PHOTO = "assets/her-photo.jpeg"

# -----------------------------
# Session state
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = 1
if "date_type" not in st.session_state:
    st.session_state.date_type = None
if "date_time" not in st.session_state:
    st.session_state.date_time = None


def go_to(page):
    st.session_state.page = page
    st.rerun()


def img_path(rel):
    """Resolve a photo path relative to this file, so it works
    regardless of the working directory Streamlit is launched from."""
    p = Path(__file__).parent / rel
    return str(p) if p.exists() else None


# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Playfair+Display:ital,wght@0,700;1,600&display=swap');

        :root{
            --wine: #6b1f3d;
            --wine-deep: #3d0f24;
            --blush: #f6d9c9;
            --gold: #c9a24a;
            --ink: #35131f;
        }

        .stApp {
            background:
                radial-gradient(circle at 15% 10%, rgba(201,162,74,0.10), transparent 40%),
                radial-gradient(circle at 85% 90%, rgba(201,162,74,0.08), transparent 40%),
                linear-gradient(160deg, #fbe9e2, #f7dcd0 55%, #f3d2c3);
        }

        html, body, [class*="css"] {
            font-family: 'Cormorant Garamond', Georgia, serif;
        }

        .main-card {
            background: rgba(255,255,255,0.92);
            border: 1px solid rgba(107,31,61,0.12);
            border-radius: 22px;
            padding: 46px 34px;
            margin: 18px auto;
            max-width: 640px;
            text-align: center;
            box-shadow: 0 24px 60px -20px rgba(107,31,61,0.35);
            animation: riseIn 0.7s cubic-bezier(.2,.9,.25,1) both;
        }

        .eyebrow{
            letter-spacing: 0.3em;
            text-transform: uppercase;
            font-size: 13px;
            color: var(--gold);
            margin-bottom: 14px;
            font-weight: 600;
        }

        .heart {
            font-size: 44px;
            animation: pulse 1.6s ease-in-out infinite;
            margin-bottom: 6px;
        }

        .title {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-weight: 700;
            font-size: 40px;
            color: var(--wine-deep);
            margin: 6px 0 10px;
        }

        .subtitle {
            font-size: 21px;
            color: #7a4a58;
            margin-bottom: 8px;
            line-height: 1.5;
        }

        .plead {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-size: 27px;
            font-weight: 700;
            color: var(--wine-deep);
        }

        .success { font-size: 64px; margin-bottom: 4px; }

        .photo-ring{
            width: 152px;
            height: 152px;
            border-radius: 50%;
            margin: 4px auto 22px;
            overflow: hidden;
            border: 3px solid var(--gold);
            box-shadow: 0 10px 26px rgba(107,31,61,0.28);
        }
        .photo-ring img{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center 20%;
        }

        .stButton > button {
            width: 100%;
            border-radius: 999px;
            padding: 12px 20px;
            font-size: 17px;
            font-weight: 700;
            font-family: 'Cormorant Garamond', serif;
            border: none;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }
        .stButton > button:hover{
            transform: translateY(-2px);
        }

        div[data-testid="stHorizontalBlock"] { align-items: center; }

        @keyframes pulse { 50% { transform: scale(1.14); } }
        @keyframes riseIn {
            from { opacity: 0; transform: translateY(18px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (prefers-reduced-motion: reduce) {
            * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# PAGE 1 — THE QUESTION
# -----------------------------
if st.session_state.page == 1:

    her_photo = img_path(HER_PHOTO)

    st.markdown(f'<div class="main-card">', unsafe_allow_html=True)

    if her_photo:
        st.markdown(
            f"""
            <div class="photo-ring">
                <img src="data:image/jpeg;base64,{__import__('base64').b64encode(open(her_photo,'rb').read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
            <div class="eyebrow">a letter for {HER_NAME}</div>
            <div class="heart">🥀</div>
            <div class="title">One tiny question...</div>
            <div class="subtitle">Would you love to go on a date with me?</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes 🥰", type="primary", use_container_width=True):
            go_to(2)
    with col2:
        if st.button("Let me think 🙈", use_container_width=True):
            go_to(3)


# -----------------------------
# PAGE 2 — YES: PICK THE DATE
# -----------------------------
elif st.session_state.page == 2:

    st.markdown(
        """
        <div class="main-card">
            <div class="heart">💘</div>
            <div class="title">Yesss!</div>
            <div class="subtitle">Okay, now you get to choose our date.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    date_options = [
        "🍦 Ice cream & a walk",
        "🌊 Beach date",
        "🎬 Movie & food",
        "☕ Café & endless talking",
        "✨ Surprise me",
    ]

    selected = st.radio(
        "What kind of date do you want?",
        date_options,
        index=None,
        key="date_choice",
    )

    selected_datetime = st.datetime_input(
        "And when are you free?",
        value=None,
        key="date_picker",
    )

    if st.button("Let's make it official ❤️", type="primary", use_container_width=True):
        if selected is None:
            st.warning("You have to choose what kind of date you want 😌❤️")
        elif selected_datetime is None:
            st.warning("And you have to tell me when you're free 😭")
        else:
            st.session_state.date_type = selected
            st.session_state.date_time = selected_datetime
            go_to(4)


# -----------------------------
# PAGE 3 — HESITATION
# -----------------------------
elif st.session_state.page == 3:

    my_photo = img_path(MY_PHOTO)

    st.markdown('<div class="main-card"><div class="heart">🥺</div></div>', unsafe_allow_html=True)

    if my_photo:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <div class="photo-ring" style="margin: -10px auto 8px;">
                    <img src="data:image/jpeg;base64,{__import__('base64').b64encode(open(my_photo,'rb').read()).decode()}">
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="main-card">
            <div class="plead">Please reconsider.</div>
            <p style="font-size:20px;color:#7a4a58;line-height:1.6;">
                Look at this innocent face... 😭<br><br>
                He has been waiting for a date.<br>
                Don't break his heart. 💔
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Okay fine, YES 😭❤️", type="primary", use_container_width=True):
        go_to(2)


# -----------------------------
# PAGE 4 — LOCKED IN
# -----------------------------
elif st.session_state.page == 4:

    selected = st.session_state.date_type
    selected_datetime = st.session_state.date_time
    formatted_date = selected_datetime.strftime("%A, %d %B %Y at %I:%M %p")

    st.markdown(
        f"""
        <div class="main-card">
            <div class="success">🥰</div>
            <div class="title">Date locked in!</div>
            <div class="subtitle">
                You chose:<br><strong>{selected}</strong><br><br>
                See you on:<br><strong>{formatted_date}</strong><br><br>
                Can't wait to see you ❤️<br><br>
                Best decision ever. 😌
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Change my mind 😭", use_container_width=True):
        go_to(2)

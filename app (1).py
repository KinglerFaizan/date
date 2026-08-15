import streamlit as st
from pathlib import Path
from datetime import datetime

st.set_page_config(
    page_title="One Tiny Question ❤️",
    page_icon="❤️",
    layout="centered",
)

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


# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at top, #fff0f5, transparent 45%),
                linear-gradient(135deg, #ffdce7, #fff7fa);
        }

        .main-card {
            background: rgba(255,255,255,0.95);
            border-radius: 32px;
            padding: 42px 30px;
            margin: 20px auto;
            max-width: 650px;
            text-align: center;
            box-shadow: 0 20px 60px rgba(130,40,70,0.18);
        }

        .heart {
            font-size: 65px;
            animation: pulse 1.4s infinite;
        }

        .title {
            font-size: 42px;
            font-weight: 800;
            color: #3b2028;
            margin: 10px 0;
        }

        .subtitle {
            font-size: 20px;
            color: #704852;
            margin-bottom: 25px;
        }

        .plead {
            font-size: 28px;
            font-weight: 800;
            color: #3b2028;
        }

        .success {
            font-size: 75px;
        }

        .stButton > button {
            width: 100%;
            border-radius: 999px;
            padding: 12px 20px;
            font-size: 17px;
            font-weight: 700;
            border: none;
        }

        div[data-testid="stHorizontalBlock"] {
            align-items: center;
        }

        @keyframes pulse {
            50% {
                transform: scale(1.12);
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# PAGE 1
# -----------------------------
if st.session_state.page == 1:

    st.markdown(
        """
        <div class="main-card">
            <div class="heart">❤️</div>
            <div class="title">One tiny question...</div>
            <div class="subtitle">
                Would you love to go on a date with me?
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 🥰", type="primary", use_container_width=True):
            go_to(2)

    with col2:
        if st.button("NO 🙈", use_container_width=True):
            go_to(3)


# -----------------------------
# PAGE 2 — YES
# -----------------------------
elif st.session_state.page == 2:

    st.markdown(
        """
        <div class="main-card">
            <div class="heart">💘</div>
            <div class="title">Yesss! 🥹</div>
            <div class="subtitle">
                Okay, now you get to choose our date ❤️
            </div>
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
        "And when are you free? 📅",
        value=None,
        key="date_picker",
    )

    if st.button(
        "Let's make it official ❤️",
        type="primary",
        use_container_width=True,
    ):

        if selected is None:
            st.warning(
                "You have to choose what kind of date you want 😌❤️"
            )

        elif selected_datetime is None:
            st.warning(
                "And you have to tell me when you're free 😭"
            )

        else:
            st.session_state.date_type = selected
            st.session_state.date_time = selected_datetime
            go_to(4)


# -----------------------------
# PAGE 3 — NO
# -----------------------------
elif st.session_state.page == 3:

    st.markdown(
        """
        <div class="main-card">
            <div class="heart">🥺</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    photo_path = Path(__file__).parent / "my-photo.jpeg"

    if photo_path.exists():
        st.image(
            str(photo_path),
            width=300,
        )

    st.markdown(
        """
        <div class="main-card">
            <div class="plead">
                Please reconsider. 🥺
            </div>

            <p style="font-size:20px;color:#704852;">
                Look at this innocent face... 😭<br><br>
                He has been waiting for a date.<br>
                Don't break his heart. 💔
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "Okay fine, YES 😭❤️",
        type="primary",
        use_container_width=True,
    ):
        go_to(2)


# -----------------------------
# PAGE 4 — SUCCESS
# -----------------------------
elif st.session_state.page == 4:

    selected = st.session_state.date_type
    selected_datetime = st.session_state.date_time

    formatted_date = selected_datetime.strftime(
        "%A, %d %B %Y at %I:%M %p"
    )

    st.markdown(
        f"""
        <div class="main-card">

            <div class="success">
                🥰
            </div>

            <div class="title">
                Date locked in!
            </div>

            <div class="subtitle">

                You chose:<br>

                <strong>{selected}</strong>

                <br><br>

                See you on:<br>

                <strong>{formatted_date}</strong>

                <br><br>

                Can't wait to see you ❤️

                <br><br>

                Best decision ever. 😌

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Change my mind 😭", use_container_width=True):
        go_to(2)

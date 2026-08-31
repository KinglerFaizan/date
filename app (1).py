import streamlit as st
from photo_data import MY_PHOTO_B64, HER_PHOTO_B64

st.set_page_config(
    page_title="One Tiny Question",
    page_icon="🌹",
    layout="centered",
)

# -----------------------------
# Personalize here
# -----------------------------
HER_NAME = "Iram"  # change anytime

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
# Styling — red palette, explicit colors everywhere
# (no color is left to inherit a default that might be invisible)
# -----------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Playfair+Display:ital,wght@0,700;1,600&display=swap');

        :root{
            --red: #c81d3f;
            --red-deep: #7a0d24;
            --red-bright: #e8355a;
            --gold: #d9a441;
            --ink: #3a0d16;
            --card-bg: #fffaf7;
        }

        .stApp {
            background:
                radial-gradient(circle at 15% 10%, rgba(200,29,63,0.10), transparent 40%),
                radial-gradient(circle at 85% 90%, rgba(217,164,65,0.10), transparent 40%),
                linear-gradient(160deg, #fff1ee, #fde3df 55%, #fbd6d0);
        }

        html, body, [class*="css"] {
            font-family: 'Cormorant Garamond', Georgia, serif;
            color: var(--ink);
        }

        .main-card {
            background: var(--card-bg);
            border: 1px solid rgba(200,29,63,0.15);
            border-radius: 22px;
            padding: 40px 34px;
            margin: 18px auto;
            max-width: 640px;
            text-align: center;
            box-shadow: 0 24px 60px -20px rgba(122,13,36,0.35);
        }

        .eyebrow{
            letter-spacing: 0.3em;
            text-transform: uppercase;
            font-size: 13px;
            color: var(--gold);
            margin-bottom: 14px;
            font-weight: 700;
        }

        .heart { font-size: 44px; margin-bottom: 6px; }

        .title {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-weight: 700;
            font-size: 40px;
            color: var(--red-deep);
            margin: 6px 0 10px;
        }

        .subtitle {
            font-size: 21px;
            color: var(--ink);
            margin-bottom: 8px;
            line-height: 1.5;
        }

        .plead {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-size: 27px;
            font-weight: 700;
            color: var(--red-deep);
        }

        .success { font-size: 64px; margin-bottom: 4px; }

        .photo-ring{
            width: 152px;
            height: 152px;
            border-radius: 50%;
            margin: 4px auto 20px;
            overflow: hidden;
            border: 3px solid var(--gold);
            box-shadow: 0 10px 26px rgba(122,13,36,0.30);
        }
        .photo-ring img{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center 20%;
        }

        /* Buttons */
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
        .stButton > button:hover{ transform: translateY(-2px); }
        .stButton > button[kind="primary"]{
            background: linear-gradient(135deg, var(--red-bright), var(--red));
            color: #ffffff !important;
        }
        .stButton > button[kind="secondary"]{
            background: #ffffff;
            color: var(--red-deep) !important;
            border: 1px solid rgba(200,29,63,0.35) !important;
        }

        /* Force visible text on Streamlit's native widgets —
           this is what makes the date-idea options actually readable */
        .stRadio label, .stRadio p, .stRadio span,
        div[data-testid="stWidgetLabel"] p,
        .stDateInput label, .stDateInput p {
            color: var(--ink) !important;
            font-size: 19px !important;
            opacity: 1 !important;
        }
        .stRadio [role="radiogroup"] label {
            background: #ffffff;
            border: 1px solid rgba(200,29,63,0.18);
            border-radius: 12px;
            padding: 10px 14px;
            margin-bottom: 6px;
        }

        div[data-testid="stHorizontalBlock"] { align-items: center; }

        @media (prefers-reduced-motion: reduce) {
            * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# PAGE 1 — THE QUESTION
# (built as ONE markdown block so the card actually wraps its content)
# -----------------------------
if st.session_state.page == 1:

    st.markdown(
        f"""
        <div class="main-card">
            <div class="photo-ring">
                <img src="data:image/png;base64,{HER_PHOTO_B64}">
            </div>
            <div class="eyebrow">a letter for {HER_NAME}</div>
            <div class="heart">🌹</div>
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

    st.markdown(
        f"""
        <div class="main-card">
            <div class="heart">🥺</div>
            <div class="photo-ring" style="margin-bottom: 18px;">
                <img src="data:image/jpeg;base64,{MY_PHOTO_B64}">
            </div>
            <div class="plead">Please reconsider.</div>
            <p style="font-size:20px;color:var(--ink);line-height:1.6;">
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


import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Football Match Predictor",
    page_icon="⚽",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e3a5f,
        #0f766e
    );
}

/* Title */
h1 {
    text-align: center;
    color: white;
    font-size: 42px !important;
    margin-top: 20px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #d1d5db;
    font-size: 20px;
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #16a34a,
        #22c55e
    );
    color: white;
    font-size: 22px;
    border-radius: 14px;
    padding: 14px;
    border: none;
    font-weight: bold;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.2s;
}

/* Dropdown */
div[data-baseweb="select"] {
    color: black;
}

</style>
""", unsafe_allow_html=True)

# Load model and encoders
model = joblib.load("model/xgboost_model.pkl")
label_encoders = joblib.load("model/label_encoders.pkl")
target_encoder = joblib.load("model/target_encoder.pkl")

st.markdown(
    "<h1>⚽ Premier League Match Outcome Predictor</h1>",
    unsafe_allow_html=True
)

carousel_images = [
    "images/football1.jpg",
    "images/football2.jpg",
    "images/football3.jpg"
]

if "image_index" not in st.session_state:
    st.session_state.image_index = 0

left_space, center, right_space = st.columns([1, 8, 1])

with center:
    st.image(
        carousel_images[st.session_state.image_index],
        width=850
    )
st.session_state.image_index = (
    st.session_state.image_index + 1
) % len(carousel_images)


st.markdown("---")

st.write("Predict Home Win, Draw, or Away Win using Machine Learning ⚽")

# User inputs
home_team_options = list(label_encoders["home_team"].classes_)
away_team_options = list(label_encoders["away_team"].classes_)
referee_options = list(label_encoders["referee"].classes_)

home_team = st.selectbox(
    "Home Team",
    home_team_options
)

away_team = st.selectbox(
    "Away Team",
    away_team_options
)

referee = st.selectbox(
    "Referee",
    referee_options
)

matchday = st.number_input(
    "Matchday",
    min_value=1,
    max_value=38,
    value=1
)

home_form = st.number_input(
    "Home Team Form (Last 5 Matches)",
    min_value=0.0,
    value=7.0
)

away_form = st.number_input(
    "Away Team Form (Last 5 Matches)",
    min_value=0.0,
    value=5.0
)

home_avg_goals = st.number_input(
    "Home Avg Goals",
    min_value=0.0,
    value=1.8
)

away_avg_goals = st.number_input(
    "Away Avg Goals",
    min_value=0.0,
    value=1.4
)

home_avg_conceded = st.number_input(
    "Home Avg Goals Conceded",
    min_value=0.0,
    value=1.0
)

away_avg_conceded = st.number_input(
    "Away Avg Goals Conceded",
    min_value=0.0,
    value=1.3
)

if st.button("Predict Match Outcome"):

    try:
        # Encode text columns
        home_team_encoded = label_encoders["home_team"].transform([home_team])[0]
        away_team_encoded = label_encoders["away_team"].transform([away_team])[0]
        referee_encoded = label_encoders["referee"].transform([referee])[0]

        # Create dataframe
        input_data = pd.DataFrame([[
            home_team_encoded,
            away_team_encoded,
            matchday,
            referee_encoded,
            home_form,
            away_form,
            home_avg_goals,
            away_avg_goals,
            home_avg_conceded,
            away_avg_conceded
        ]], columns=[
            "home_team",
            "away_team",
            "matchday",
            "referee",
            "home_form",
            "away_form",
            "home_avg_goals",
            "away_avg_goals",
            "home_avg_conceded",
            "away_avg_conceded"
        ])

        # Prediction
        prediction = model.predict(input_data)

        # Convert result back to label
        result = target_encoder.inverse_transform(prediction)[0]

        # Nice output
        if result == "Home Win":
            st.success(f"🏆 Prediction: {home_team} Win")

        elif result == "Away Win":
            st.success(f"✈️ Prediction: {away_team} Win")

        else:
            st.success("🤝 Prediction: Draw")

    except Exception as e:
         st.error(f"Error: {e}")
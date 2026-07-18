import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
import joblib
import tensorflow as tf
import streamlit as st

import json
import os

st.set_page_config(
    page_title="AI Powered Placement Preparation Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

USER_FILE = "users.json"

if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

with open(USER_FILE, "r") as f:
    users = json.load(f)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🔐 AI Placement Assistant")

    menu = st.radio("", ["Login", "Register"])

    if menu == "Register":
        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")

        if st.button("Register"):

            if new_user in users:
                st.error("Username already exists")

            else:
                users[new_user] = new_pass

                with open(USER_FILE, "w") as f:
                    json.dump(users, f)

                st.success("Registration Successful")

    else:

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("Invalid Username or Password")

    st.stop()
# ----------------------------
# PAGE CONFIG
# ----------------------------


st.markdown("""
<style>

/* Hide Streamlit menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {
    background: transparent !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stToolbar"] {
    right: 1rem;
}            


/* Main background */
.stApp{
    background: linear-gradient(to right,#0f172a,#1e293b);
}

/* Main title */
.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:white;
    padding:20px;
    border-radius:15px;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    animation: fadeIn 1s;
}

/* Cards */
.card{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    color:white;
    box-shadow:0px 5px 20px rgba(0,0,0,0.4);
    transition:0.3s;
}

.card:hover{
    transform:scale(1.03);
}

@keyframes fadeIn{
from{opacity:0;}
to{opacity:1;}
}

</style>
""",unsafe_allow_html=True)

# ----------------------------
# LOAD MODELS
# ----------------------------

domain_model = joblib.load("domain_prediction_model2.pkl")

placement_model = tf.keras.models.load_model(
    "model.keras"
)
label_encoder = joblib.load("label_encoder.pkl")
career_skills = {
    "Web Development": ["HTML","CSS","JavaScript","React","NodeJS"],
    "Data Science": ["Python","Pandas","NumPy","SQL","Machine Learning"],
    "AI_ML": ["Python","TensorFlow","PyTorch","Deep Learning","NLP"],
    "Cyber Security": ["Networking","Linux","Ethical Hacking","Cryptography"],
    "Cloud Computing": ["AWS","Docker","Kubernetes","Linux"],
    "Mobile Development": ["Java","Kotlin","Android","Flutter"],
    "UI_UX": ["Figma","Wireframing","Prototyping"],
    "DevOps": ["Docker","Jenkins","Git","CI_CD"],
    "Blockchain": ["Solidity","Ethereum","Smart Contracts"],
    "Game Development": ["Unity","C#","Game Design"],
    "Software Testing": ["Selenium","Manual Testing","Automation Testing"]
}

# ----------------------------
# HEADER
# ----------------------------

#st.markdown("""
#<div class="title">
#🎯 AI Powered Placement Preparation Assistant
#</div>
#""",unsafe_allow_html=True)



with st.sidebar:

    selected = option_menu(
        menu_title="🤖 AI Assistant",
        options=[
            "Dashboard",
            "Career Recommendation",
            "Placement Prediction",
            "About"
        ],
        icons=[
            "house-fill",
            "briefcase-fill",
            "graph-up-arrow",
            "info-circle-fill"
        ],
        menu_icon="robot",
        default_index=0
    )
col1, col2 = st.columns([9, 1])

with col2:
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()
        
if selected == "Dashboard":
    st.markdown("""
    <div style="
        text-align:center;
        font-size:40px;
        font-weight:bold;
        color:white;
        padding:18px;
        border-radius:15px;
        background:linear-gradient(90deg,#2563EB,#7C3AED);
        margin-bottom:20px;">
        🎯 AI Powered Placement Preparation Assistant
    </div>
    """, unsafe_allow_html=True)

elif selected == "Career Recommendation":
    st.markdown("""
    <div style="
        text-align:center;
        font-size:38px;
        font-weight:bold;
        color:white;
        padding:18px;
        border-radius:15px;
        background:linear-gradient(90deg,#10B981,#059669);
        margin-bottom:20px;">
        💼 Career Recommendation
    </div>
    """, unsafe_allow_html=True)

elif selected == "Placement Prediction":
    st.markdown("""
    <div style="
        text-align:center;
        font-size:38px;
        font-weight:bold;
        color:white;
        padding:18px;
        border-radius:15px;
        background:linear-gradient(90deg,#F59E0B,#EF4444);
        margin-bottom:20px;">
        📊 Placement Prediction
    </div>
    """, unsafe_allow_html=True)

elif selected == "About":
    st.markdown("""
    <div style="
        text-align:center;
        font-size:38px;
        font-weight:bold;
        color:white;
        padding:18px;
        border-radius:15px;
        background:linear-gradient(90deg,#8B5CF6,#EC4899);
        margin-bottom:20px;">
         About Project
    </div>
    """, unsafe_allow_html=True)    

    st.markdown("---")

  

if selected == "Dashboard":

    st.markdown("## 👋 Welcome")

    st.write(
        """
Welcome to the **AI Powered Placement Preparation Assistant**.

This system helps students:

✅ Find the best Career Domain

✅ Predict Placement Probability

Choose any option from the left sidebar.
"""
    )

    col1, col2 = st.columns(2)

    with col1:

        st.info("🎯 Career Recommendation")

        st.write(
            "Predict the most suitable career based on your skills."
        )

    with col2:

        st.success("📊 Placement Prediction")

        st.write(
            "Predict your placement probability using academic details."
        )

# ==================================================
# TAB 1
# ==================================================

if selected == "Career Recommendation":

    st.subheader("Career Domain Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:

        Python = st.checkbox("Python")
        Java = st.checkbox("Java")
        Cpp = st.checkbox("C++")
        JavaScript = st.checkbox("JavaScript")
        SQL = st.checkbox("SQL")
        HTML = st.checkbox("HTML")
        CSS = st.checkbox("CSS")
        React = st.checkbox("React")
        Angular = st.checkbox("Angular")
        NodeJS = st.checkbox("NodeJS")
        Django = st.checkbox("Django")
        Flask = st.checkbox("Flask")

    with col2:

        SpringBoot = st.checkbox("SpringBoot")
        Android = st.checkbox("Android")
        Kotlin = st.checkbox("Kotlin")
        Swift = st.checkbox("Swift")
        MachineLearning = st.checkbox("Machine Learning")
        DeepLearning = st.checkbox("Deep Learning")
        NLP = st.checkbox("NLP")
        ComputerVision = st.checkbox("Computer Vision")
        TensorFlow = st.checkbox("TensorFlow")
        PyTorch = st.checkbox("PyTorch")
        AWS = st.checkbox("AWS")
        Azure = st.checkbox("Azure")

    with col3:

        GCP = st.checkbox("GCP")
        Docker = st.checkbox("Docker")
        Kubernetes = st.checkbox("Kubernetes")
        Linux = st.checkbox("Linux")
        Networking = st.checkbox("Networking")
        CyberSecurity = st.checkbox("Cyber Security")
        PenTesting = st.checkbox("Pen Testing")
        PowerBI = st.checkbox("Power BI")
        Tableau = st.checkbox("Tableau")
        Excel = st.checkbox("Excel")
        Statistics = st.checkbox("Statistics")

    if st.button("Predict Career Domain"):

        skill_input = np.array([[
            int(Python),
            int(Java),
            int(Cpp),
            int(JavaScript),
            int(SQL),
            int(HTML),
            int(CSS),
            int(React),
            int(Angular),
            int(NodeJS),
            int(Django),
            int(Flask),
            int(SpringBoot),
            int(Android),
            int(Kotlin),
            int(Swift),
            int(MachineLearning),
            int(DeepLearning),
            int(NLP),
            int(ComputerVision),
            int(TensorFlow),
            int(PyTorch),
            int(AWS),
            int(Azure),
            int(GCP),
            int(Docker),
            int(Kubernetes),
            int(Linux),
            int(Networking),
            int(CyberSecurity),
            int(PenTesting),
            int(PowerBI),
            int(Tableau),
            int(Excel),
            int(Statistics)
        ]])

        domain_names = {
            0: "Web Development",
            1: "Data Science",
            2: "AI_ML",
            3: "Cyber Security",
            4: "Cloud Computing",
            5: "Mobile Development",
            6: "UI_UX",
            7: "DevOps",
            8: "Blockchain",
            9: "Game Development",
            10: "Software Testing"
    
        }
        domain = int(domain_model.predict(skill_input.reshape(1, -1))[0])
        st.success(f"Recommended Domain: {domain_names.get(domain, 'Unknown')}")


        domain_name = domain_names.get(domain)
        required_skills = career_skills.get(domain_name, [])

        st.subheader("Required Skills")

        for skill in required_skills:
            st.markdown(f"✅ {skill}")
        

        current_skills = [
            "Python" if Python else None,
            "Java" if Java else None,
            "C++" if Cpp else None,
            "JavaScript" if JavaScript else None,
            "SQL" if SQL else None,
            "HTML" if HTML else None,
            "CSS" if CSS else None,
            "React" if React else None,
            "Angular" if Angular else None,
            "NodeJS" if NodeJS else None,
            "Django" if Django else None,
            "Flask" if Flask else None,
            "SpringBoot" if SpringBoot else None,
            "Android" if Android else None,
            "Kotlin" if Kotlin else None,
            "Swift" if Swift else None,
            "MachineLearning" if MachineLearning else None,
            "DeepLearning" if DeepLearning else None,
            "NLP" if NLP else None,
            "ComputerVision" if ComputerVision else None,
            "TensorFlow" if TensorFlow else None,
            "PyTorch" if PyTorch else None,
            "AWS" if AWS else None,
            "Azure" if Azure else None,
            "GCP" if GCP else None,
            "Docker" if Docker else None,
            "Kubernetes" if Kubernetes else None,
            "Linux" if Linux else None,
            "Networking" if Networking else None,
            "CyberSecurity" if CyberSecurity else None,
            "PenTesting" if PenTesting else None,
            "PowerBI" if PowerBI else None,
            "Tableau" if Tableau else None,
            "Excel" if Excel else None,
            "Statistics" if Statistics else None
        ]

        current_skills = [x for x in current_skills if x]

        missing_skills = [
            skill
            for skill in required_skills
            if skill not in current_skills
        ]

        #st.subheader("Skill Gap Analysis")

        #if len(missing_skills) == 0:
        #    st.success(
        #        "You already have all required skills."
        #    )
       # else:
        #    st.warning(
        #        missing_skills
       #     )

# ==================================================
# TAB 2
# ==================================================

if selected == "Placement Prediction":

    st.subheader("Placement Prediction")

    
    iq = st.number_input(
        "IQ",
        min_value=0
    )

    prev_sem = st.number_input(
        "Previous Semester Result"
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0
    )

    academic = st.number_input(
        "Academic Performance"
    )

    internship = st.number_input(
        "Internship Experience"
    )

    extracurricular = st.number_input(
        "Extra Curricular Score"
    )

    communication = st.number_input(
        "Communication Skills"
    )

    projects = st.number_input(
        "Projects Completed"
    )

    if st.button("Predict Placement"):

        placement_input = np.array([[
            iq,
            prev_sem,
            cgpa,
            academic,
            internship,
            extracurricular,
            communication,
            projects
        ]])

        prediction = placement_model.predict(
            placement_input
        )

        probability = float(prediction[0][0]) * 100

        if probability >= 80:
            st.success(f"🎉 Placement Chance : {probability:.2f}%")
    

        elif probability >= 60:
             st.warning(f"🙂 Placement Chance : {probability:.2f}%")
   

        else:
            st.error(f"⚠ Placement Chance : {probability:.2f}%")

if selected == "About":

    st.header("About Project")

    st.write("""
### AI Powered Placement Preparation Assistant

Technology Used

- Python

- Streamlit

- Machine Learning

- TensorFlow

- Scikit-learn

Developed By

Bhargav
""")   
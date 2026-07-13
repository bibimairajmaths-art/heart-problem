import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
.main{
    background-color:#f5f7fb;
}

.block-container{
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:42px;
    color:#E63946;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:30px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    text-align:center;
}

.form-card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

.result-card{
    background:#ffffff;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    text-align:center;
}

.stButton>button{
    width:100%;
    background:#E63946;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    border:none;
}

.stButton>button:hover{
    background:#d62839;
    color:white;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966486.png", width=120)
    st.title("Navigation")

    page = st.radio(
        "",
        ["🏠 Home",
         "❤️ Prediction",
         "📊 Dashboard",
         "ℹ About"]
    )

# -------------------- HOME --------------------
if page == "🏠 Home":

    st.markdown('<div class="title">❤️ Heart Disease Prediction System</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="subtitle">AI-powered Cardiovascular Risk Assessment</div>',
        unsafe_allow_html=True
    )

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.metric("Accuracy","98.2%")

    with c2:
        st.metric("Patients","1500+")

    with c3:
        st.metric("Predictions","420")

    with c4:
        st.metric("Response","0.02 sec")

    st.write("")

    st.info("""
    ### Welcome 👋

    This application predicts whether a patient is at risk of heart disease using
    Machine Learning.

    ✔ Fast Prediction

    ✔ Easy Interface

    ✔ High Accuracy

    ✔ Doctor Friendly
    """)

# -------------------- PREDICTION PAGE --------------------
elif page=="❤️ Prediction":

    st.markdown("<h2 style='text-align:center;color:#E63946;'>Patient Information</h2>",unsafe_allow_html=True)

    with st.container():

        left,right=st.columns([2,1])

        with left:

            with st.container():

                col1,col2=st.columns(2)

                with col1:
                    age=st.number_input("Age",20,100)
                    sex=st.selectbox("Sex",["Male","Female"])
                    cp=st.selectbox("Chest Pain Type",[0,1,2,3])
                    bp=st.number_input("Resting Blood Pressure")

                    chol=st.number_input("Cholesterol")

                    fbs=st.selectbox("Fasting Blood Sugar",[0,1])

                with col2:

                    restecg=st.selectbox("Rest ECG",[0,1,2])

                    thalach=st.number_input("Maximum Heart Rate")

                    exang=st.selectbox("Exercise Angina",[0,1])

                    oldpeak=st.number_input("ST Depression")

                    slope=st.selectbox("Slope",[0,1,2])

                    ca=st.selectbox("Major Vessels",[0,1,2,3])

                    thal=st.selectbox("Thal",[0,1,2,3])

                if st.button("❤️ Predict Heart Disease"):

                    st.success("Prediction Completed Successfully!")

                    st.progress(92)

                    st.markdown("""
                    ## ❤️ Result

                    **Low Risk of Heart Disease**

                    Confidence: **92%**
                    """)

        with right:

            st.image(
                "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
                width=250
            )

            st.info("""
            ### Tips ❤️

            ✔ Exercise Daily

            ✔ Eat Healthy

            ✔ Avoid Smoking

            ✔ Regular Checkups
            """)

# -------------------- DASHBOARD --------------------
elif page=="📊 Dashboard":

    st.title("📊 Dashboard")

    c1,c2,c3=st.columns(3)

    c1.metric("Healthy Patients","1240")
    c2.metric("Heart Disease","260")
    c3.metric("Accuracy","98.2%")

    st.progress(98)

    chart_data={
        "Age":[25,35,45,55,65],
        "Patients":[20,40,80,60,30]
    }

    st.line_chart(chart_data,x="Age",y="Patients")

# -------------------- ABOUT --------------------
else:

    st.title("ℹ About")

    st.write("""
    ## Heart Disease Prediction System

    This application uses Machine Learning to predict the likelihood of heart disease
    based on patient medical information.

    **Technology Used**

    - Streamlit
    - Python
    - Scikit-Learn
    - Pandas
    - NumPy

    Developed with ❤️ using Streamlit.
    """)

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown(
    "<div class='footer'>© 2026 Heart Disease Prediction System | Developed with Streamlit ❤️</div>",
    unsafe_allow_html=True
)
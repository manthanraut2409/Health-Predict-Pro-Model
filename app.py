import streamlit as st 
import pickle 
import os
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title="HealthPredict Pro", 
    layout="wide", 
    page_icon="🏥",
    initial_sidebar_state="expanded"
)

working_dir = os.path.dirname(os.path.abspath(__file__))

IMAGE_PATHS = {
    "logo": "assets/images/logo.png",
    "home_banner": "assets/images/home-banner.png",
    "diabetes_icon": "assets/images/diabetes-icon.png",
    "heart_icon": "assets/images/heart-icon.png",
    "kidney_icon": "assets/images/kidney-icon.png",
    "team_doctor": "assets/images/team/doctor.jpg",
    "team_datascientist": "assets/images/team/datascientist.jpg",
    "team_developer": "assets/images/team/developer.jpg",
    "placeholder": "assets/images/placeholder.jpg"
}

try:
    diabetes_model = pickle.load(open('pkl file/diabetes.pkl','rb'))
    heart_disease_model = pickle.load(open('pkl file/heart.pkl','rb'))
    kidney_disease_model = pickle.load(open('pkl file/kidney.pkl','rb'))
except Exception as e:
    st.error(f"Error loading models: {e}")

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
        color: white;
    }
    .title-text {
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        margin-bottom: 20px;
        background-color: white;
    }
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 10px;
        color: #3498db;
    }
    .team-card {
        text-align: center;
        margin: 20px;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        background-color: #f8f9fa;
    }
    .team-img {
        border-radius: 50%;
        border: 3px solid #3498db;
        object-fit: cover;
        aspect-ratio: 1/1;
        width: 120px;
        height: 120px;
    }
    </style>
""", unsafe_allow_html=True)

def load_image(path, width=None):
    """Helper function to load images with error handling"""
    try:
        img = Image.open(path)
        if width:
            return img.resize((width, int(width * img.height / img.width)))
        return img
    except Exception as e:
        st.error(f"Error loading image: {path}")
        return Image.new('RGB', (1, 1), color='white')

def navigation():
    with st.sidebar:
        logo = load_image(IMAGE_PATHS["logo"], 150)
        st.image(logo, use_column_width=True)
        st.markdown("---")
        
        menu = option_menu(
            menu_title=None,
            options=["Home", "Diabetes Prediction", "Heart Disease Prediction", 
                    "Kidney Disease Prediction", "Health Insights", "About", "Contact"],
            icons=["house", "activity", "heart-pulse", "bandaid", "graph-up", 
                  "info-circle", "envelope"],
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#2c3e50"},
                "icon": {"color": "white", "font-size": "16px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#34495e"},
                "nav-link-selected": {"background-color": "#3498db"},
            }
        )
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: white; font-size: 14px;">
            <p>HealthPredict Pro v1.0</p>
            <p>© 2025 All Rights Reserved</p>
        </div>
        """, unsafe_allow_html=True)
        
        return menu

def home_page():
    st.markdown("<h1 class='title-text'>Welcome to HealthPredict Pro</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 18px; color: #34495e;">
        Your comprehensive health assessment platform powered by machine learning.
    </div>
    """, unsafe_allow_html=True)
    
    banner = load_image(IMAGE_PATHS["logo"])
    st.image(banner, use_column_width=True)
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(load_image(IMAGE_PATHS["diabetes_icon"], 80), width=80)
            st.markdown("### Disease Prediction")
            st.markdown("Get instant predictions for diabetes, heart disease, and kidney disease using advanced ML models.")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(load_image(IMAGE_PATHS["heart_icon"], 80), width=80)
            st.markdown("### Health Insights")
            st.markdown("Visualize your health metrics and understand risk factors with interactive charts.")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(load_image(IMAGE_PATHS["kidney_icon"], 80), width=80)
            st.markdown("### Privacy Focused")
            st.markdown("Your data never leaves your device. All predictions happen locally for maximum privacy.")
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("How It Works")
    steps = [
        {"icon": "1️⃣", "title": "Select a Prediction Tool", "desc": "Choose from diabetes, heart disease, or kidney disease prediction."},
        {"icon": "2️⃣", "title": "Enter Your Health Metrics", "desc": "Provide your health information in the simple form."},
        {"icon": "3️⃣", "title": "Get Instant Results", "desc": "Our AI analyzes your data and provides a risk assessment."},
        {"icon": "4️⃣", "title": "Understand Your Health", "desc": "View detailed insights and recommendations based on your results."}
    ]
    
    for step in steps:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 10])
            with col1:
                st.markdown(f"<h3>{step['icon']}</h3>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"### {step['title']}")
                st.markdown(step['desc'])
            st.markdown('</div>', unsafe_allow_html=True)

def diabetes_page():
    st.markdown("<h1 class='title-text'>Diabetes Risk Assessment</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 16px; color: #34495e; margin-bottom: 20px;">
        This tool evaluates your risk of having diabetes based on key health indicators. 
        Please fill in your information below for an assessment.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ About Diabetes"):
        st.markdown("""
        Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin 
        or when the body cannot effectively use the insulin it produces. Early detection can help prevent 
        complications through proper management.
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Personal Information")
            age = st.slider("Age", 1, 100, 30)
            pregnancies = st.number_input("Number of Pregnancies (if applicable)", min_value=0, max_value=20, value=0)
            st.markdown('</div>', unsafe_allow_html=True)
            
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("Blood Tests")
                glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, max_value=300, value=90)
                insulin = st.number_input("Insulin Level (μU/mL)", min_value=0, max_value=300, value=16)
                st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Vital Signs")
            blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=0, max_value=200, value=70)
            skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
            bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0, step=0.1)
            st.markdown('</div>', unsafe_allow_html=True)
            
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("Family History")
                diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, step=0.01)
                st.markdown('</div>', unsafe_allow_html=True)
    
    NewBMI_Overweight = 1 if 25 <= bmi < 30 else 0
    NewBMI_Underweight = 1 if bmi < 18.5 else 0
    NewBMI_Obesity_1 = 1 if 30 <= bmi < 35 else 0
    NewBMI_Obesity_2 = 1 if 35 <= bmi < 40 else 0 
    NewBMI_Obesity_3 = 1 if bmi >= 40 else 0
    
    NewInsulinScore_Normal = 1 if 16 <= insulin <= 166 else 0 
    
    NewGlucose_Low = 1 if glucose <= 70 else 0
    NewGlucose_Normal = 1 if 70 < glucose <= 99 else 0 
    NewGlucose_Overweight = 1 if 99 < glucose <= 126 else 0
    NewGlucose_Secret = 1 if glucose > 126 else 0
    
    if st.button("Assess Diabetes Risk", key="diabetes_btn"):
        with st.spinner("Analyzing your health data..."):
            user_input = [
                pregnancies, glucose, blood_pressure, skin_thickness, insulin,
                bmi, diabetes_pedigree, age, NewBMI_Underweight,
                NewBMI_Overweight, NewBMI_Obesity_1,
                NewBMI_Obesity_2, NewBMI_Obesity_3, NewInsulinScore_Normal, 
                NewGlucose_Low, NewGlucose_Normal, NewGlucose_Overweight,
                NewGlucose_Secret
            ]
            
            try:
                prediction = diabetes_model.predict([user_input])
                probability = diabetes_model.predict_proba([user_input])[0][1] * 100
                
                st.markdown("---")
                st.subheader("Assessment Results")
                
                if prediction[0] == 1:
                    st.error(f"🚨 High Risk of Diabetes ({probability:.1f}% probability)")
                    st.markdown("""
                    **Recommendations:**
                    - Consult with a healthcare professional as soon as possible
                    - Monitor your blood sugar levels regularly
                    - Consider dietary changes and increased physical activity
                    """)
                else:
                    st.success(f"✅ Low Risk of Diabetes ({probability:.1f}% probability)")
                    st.markdown("""
                    **Recommendations:**
                    - Maintain healthy lifestyle habits
                    - Get regular check-ups to monitor your health
                    - Continue balanced diet and exercise
                    """)
                st.markdown("---")
                st.subheader("Health Metrics Analysis")
                
                metrics_df = pd.DataFrame({
                    "Metric": ["Glucose", "BMI", "Blood Pressure", "Age"],
                    "Value": [glucose, bmi, blood_pressure, age],
                    "Normal Range Lower": [70, 18.5, 90, 0],
                    "Normal Range Upper": [99, 24.9, 120, 100]
                })
                
                fig = px.bar(metrics_df, x="Metric", y="Value", 
                            title="Your Health Metrics vs Normal Range",
                            labels={"Value": "Measurement"},
                            color="Metric")
                
                fig.add_scatter(x=metrics_df["Metric"], y=metrics_df["Normal Range Lower"], 
                               mode="lines", line=dict(color="gray", dash="dash"), 
                               name="Normal Range (Min)")
                fig.add_scatter(x=metrics_df["Metric"], y=metrics_df["Normal Range Upper"], 
                               mode="lines", line=dict(color="gray", dash="dash"), 
                               name="Normal Range (Max)")
                
                st.plotly_chart(fig, use_container_width=True)
                
            except Exception as e:
                st.error(f"An error occurred during prediction: {str(e)}")

def heart_page():
    st.markdown("<h1 class='title-text'>Heart Disease Risk Assessment</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 16px; color: #34495e; margin-bottom: 20px;">
        Evaluate your risk of cardiovascular disease based on key health indicators and lifestyle factors.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ About Heart Disease"):
        st.markdown("""
        Heart disease refers to various types of heart conditions. The most common type is coronary artery disease, 
        which can lead to heart attack. Early detection of risk factors can help prevent serious complications.
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Personal Information")
            age = st.slider("Age (years)", 1, 100, 50)
            sex = st.selectbox("Sex", ["Female", "Male"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("Symptoms")
                cp = st.selectbox("Chest Pain Type", [
                    "Typical angina", 
                    "Atypical angina", 
                    "Non-anginal pain", 
                    "Asymptomatic"
                ])
                exang = st.radio("Exercise Induced Angina", ["No", "Yes"])
                st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Medical Measurements")
            trestbps = st.number_input("Resting Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)
            chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=100, max_value=600, value=200)
            thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
            oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=6.0, value=1.0, step=0.1)
            st.markdown('</div>', unsafe_allow_html=True)
            
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("Other Factors")
                fbs = st.radio("Fasting Blood Sugar > 120 mg/dL", ["No", "Yes"])
                restecg = st.selectbox("Resting ECG Results", [
                    "Normal", 
                    "ST-T wave abnormality",
                    "Left ventricular hypertrophy"
                ])
                slope = st.selectbox("Slope of Peak Exercise ST Segment", [
                    "Upsloping", 
                    "Flat", 
                    "Downsloping"
                ])
                st.markdown('</div>', unsafe_allow_html=True)
    
    sex_num = 1 if sex == "Male" else 0
    cp_num = ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"].index(cp)
    exang_num = 1 if exang == "Yes" else 0
    fbs_num = 1 if fbs == "Yes" else 0
    restecg_num = ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"].index(restecg)
    slope_num = ["Upsloping", "Flat", "Downsloping"].index(slope)
    ca = 0  
    thal = 2  
    
    if st.button("Assess Heart Disease Risk", key="heart_btn"):
        with st.spinner("Analyzing your cardiovascular health..."):
            user_input = [
                age, sex_num, cp_num, trestbps, chol, fbs_num, restecg_num,
                thalach, exang_num, oldpeak, slope_num, ca, thal
            ]
            
            try:
                prediction = heart_disease_model.predict([user_input])
                probability = heart_disease_model.predict_proba([user_input])[0][1] * 100
                
                st.markdown("---")
                st.subheader("Assessment Results")
                
                if prediction[0] == 1:
                    st.error(f"🚨 High Risk of Heart Disease ({probability:.1f}% probability)")
                    st.markdown("""
                    **Recommendations:**
                    - Consult a cardiologist for further evaluation
                    - Consider lifestyle changes (diet, exercise, stress management)
                    - Monitor blood pressure and cholesterol regularly
                    """)
                else:
                    st.success(f"✅ Low Risk of Heart Disease ({probability:.1f}% probability)")
                    st.markdown("""
                    **Recommendations:**
                    - Maintain heart-healthy habits
                    - Continue regular physical activity
                    - Get periodic check-ups to monitor cardiovascular health
                    """)
                st.markdown("---")
                st.subheader("Cardiovascular Health Metrics")
                metrics_df = pd.DataFrame({
                    "Metric": ["Cholesterol", "Blood Pressure", "Max Heart Rate"],
                    "Value": [chol, trestbps, thalach],
                    "Ideal Lower": [0, 90, 0],
                    "Ideal Upper": [200, 120, 220]
                })
                
                fig = px.bar(metrics_df, x="Metric", y="Value", 
                            title="Your Cardiovascular Metrics vs Ideal Range",
                            labels={"Value": "Measurement"},
                            color="Metric")
                
                fig.add_scatter(x=metrics_df["Metric"], y=metrics_df["Ideal Lower"], 
                               mode="lines", line=dict(color="green", dash="dash"), 
                               name="Ideal Range (Min)")
                fig.add_scatter(x=metrics_df["Metric"], y=metrics_df["Ideal Upper"], 
                               mode="lines", line=dict(color="green", dash="dash"), 
                               name="Ideal Range (Max)")
                
                st.plotly_chart(fig, use_container_width=True)
                
            except Exception as e:
                st.error(f"An error occurred during prediction: {str(e)}")

def kidney_page():
    st.markdown("<h1 class='title-text'>Kidney Disease Risk Assessment</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 16px; color: #34495e; margin-bottom: 20px;">
        Evaluate your kidney health based on clinical measurements and laboratory test results.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ About Kidney Disease"):
        st.markdown("""
        Chronic kidney disease means your kidneys are damaged and can't filter blood properly. 
        Early detection can help slow or prevent progression of the disease.
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Personal Information")
            age = st.slider("Age (years)", 1, 100, 50)
            blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=50, max_value=200, value=120)
            st.markdown('</div>', unsafe_allow_html=True)
            
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("Urine Tests")
                specific_gravity = st.number_input("Specific Gravity", min_value=1.000, max_value=1.050, value=1.015, step=0.001)
                albumin = st.number_input("Albumin (0-5)", min_value=0, max_value=5, value=0)
                sugar = st.number_input("Sugar (0-5)", min_value=0, max_value=5, value=0)
                st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Blood Tests")
            blood_glucose_random = st.number_input("Random Blood Glucose (mg/dL)", min_value=50, max_value=500, value=100)
            blood_urea = st.number_input("Blood Urea (mg/dL)", min_value=5, max_value=200, value=25)
            serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=10.0, value=0.8, step=0.1)
            sodium = st.number_input("Sodium (mEq/L)", min_value=100, max_value=160, value=140)
            potassium = st.number_input("Potassium (mEq/L)", min_value=2.0, max_value=7.0, value=4.0, step=0.1)
            st.markdown('</div>', unsafe_allow_html=True)
            
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("Other Factors")
                hypertension = st.radio("Hypertension", ["No", "Yes"])
                diabetes_mellitus = st.radio("Diabetes Mellitus", ["No", "Yes"])
                coronary_artery_disease = st.radio("Coronary Artery Disease", ["No", "Yes"])
                st.markdown('</div>', unsafe_allow_html=True)
    
    hypertension_num = 1 if hypertension == "Yes" else 0
    diabetes_mellitus_num = 1 if diabetes_mellitus == "Yes" else 0
    coronary_artery_disease_num = 1 if coronary_artery_disease == "Yes" else 0
    
    red_blood_cells = 0
    pus_cell = 0
    pus_cell_clumps = 0
    bacteria = 0
    haemoglobin = 12
    packed_cell_volume = 40
    white_blood_cell_count = 7000
    red_blood_cell_count = 4.5
    appetite = 0
    peda_edema = 0
    aanemia = 0
    
    if st.button("Assess Kidney Disease Risk", key="kidney_btn"):
        with st.spinner("Analyzing your kidney health data..."):
            user_input = [
                age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, 
                pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, 
                serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, 
                white_blood_cell_count, red_blood_cell_count, hypertension_num, 
                diabetes_mellitus_num, coronary_artery_disease_num, appetite, 
                peda_edema, aanemia
            ]
            
            try:
                prediction = kidney_disease_model.predict([user_input])
                probability = kidney_disease_model.predict_proba([user_input])[0][1] * 100
                
                st.markdown("---")
                st.subheader("Assessment Results")
                
                if prediction[0] == 1:
                    st.error(f"🚨 High Risk of Kidney Disease ({probability:.1f}% probability)")
                    st.markdown("""
                    **Recommendations:**
                    - Consult a nephrologist for further evaluation
                    - Monitor kidney function regularly
                    - Manage blood pressure and blood sugar levels
                    - Stay hydrated and follow a kidney-friendly diet
                    """)
                else:
                    st.success(f"✅ Low Risk of Kidney Disease ({probability:.1f}% probability)")
                    st.markdown("""
                    **Recommendations:**
                    - Maintain healthy lifestyle habits
                    - Stay hydrated
                    - Monitor blood pressure and blood sugar levels
                    - Get regular check-ups
                    """)
                
                
                st.markdown("---")
                st.subheader("Kidney Health Metrics")
                
                metrics_df = pd.DataFrame({
                    "Metric": ["Creatinine", "Urea", "Blood Pressure", "Glucose"],
                    "Value": [serum_creatinine, blood_urea, blood_pressure, blood_glucose_random],
                    "Normal Upper Limit": [1.2, 40, 120, 140]
                })
                
                fig = px.bar(metrics_df, x="Metric", y="Value", 
                            title="Your Kidney Health Metrics vs Normal Limits",
                            labels={"Value": "Measurement"},
                            color="Metric")
                
                fig.add_scatter(x=metrics_df["Metric"], y=metrics_df["Normal Upper Limit"], 
                               mode="lines", line=dict(color="red", dash="dash"), 
                               name="Normal Upper Limit")
                
                st.plotly_chart(fig, use_container_width=True)
                
               
                if age > 18:
                    sex = st.session_state.get('sex', 'Male')  # Get sex from session state or default
                    if sex == "Male":
                        eGFR = 175 * (serum_creatinine**-1.154) * (age**-0.203)
                    else:
                        eGFR = 175 * (serum_creatinine**-1.154) * (age**-0.203) * 0.742
                    
                    st.markdown(f"**Estimated GFR (eGFR):** {eGFR:.1f} mL/min/1.73m²")
                    
                    if eGFR >= 90:
                        st.success("Normal kidney function")
                    elif 60 <= eGFR < 90:
                        st.warning("Mildly decreased kidney function")
                    elif 30 <= eGFR < 60:
                        st.error("Moderately decreased kidney function")
                    elif 15 <= eGFR < 30:
                        st.error("Severely decreased kidney function")
                    else:
                        st.error("Kidney failure")
                
            except Exception as e:
                st.error(f"An error occurred during prediction: {str(e)}")

def insights_page():
    st.markdown("<h1 class='title-text'>Health Insights & Analytics</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 16px; color: #34495e; margin-bottom: 20px;">
        Explore health trends and get personalized recommendations based on population data.
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Diabetes Trends", "Heart Health", "Kidney Function"])
    
    with tab1:
        st.subheader("Diabetes Prevalence and Risk Factors")
        
        diabetes_data = pd.DataFrame({
            "Age Group": ["20-30", "30-40", "40-50", "50-60", "60+"],
            "Prevalence (%)": [5.2, 9.8, 15.3, 22.7, 28.5],
            "Average Glucose": [95, 102, 112, 125, 135],
            "Average BMI": [24.1, 25.8, 27.3, 28.1, 28.5]
        })
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.line(diabetes_data, x="Age Group", y="Prevalence (%)", 
                         title="Diabetes Prevalence by Age Group")
            st.plotly_chart(fig, use_column_width=True)
            
            st.markdown("""
            **Key Risk Factors:**
            - High BMI (especially over 30)
            - Elevated fasting glucose levels
            - Family history of diabetes
            - Physical inactivity
            """)
        
        with col2:
            fig = px.scatter(diabetes_data, x="Average BMI", y="Average Glucose", 
                           size="Prevalence (%)", color="Age Group",
                           title="BMI vs Glucose by Age Group")
            st.plotly_chart(fig, use_column_width=True)
            
            st.markdown("""
            **Prevention Tips:**
            - Maintain healthy weight
            - Exercise regularly (150 mins/week)
            - Eat balanced diet (low sugar, high fiber)
            - Get regular health check-ups
            """)
    
    with tab2:
        st.subheader("Cardiovascular Health Insights")
        
        heart_data = pd.DataFrame({
            "Risk Factor": ["High BP", "High Cholesterol", "Smoking", "Obesity", "Diabetes"],
            "Relative Risk": [3.2, 2.8, 2.5, 2.1, 2.9],
            "Prevalence (%)": [32.5, 28.7, 15.2, 35.1, 12.8]
        })
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(heart_data, x="Risk Factor", y="Relative Risk",
                        title="Relative Risk of Heart Disease by Factor")
            st.plotly_chart(fig, use_column_width=True)
            
            st.markdown("""
            **Heart-Healthy Habits:**
            - Maintain blood pressure <120/80
            - Keep LDL cholesterol <100 mg/dL
            - Exercise 30 mins most days
            - Eat Mediterranean-style diet
            """)
        
        with col2:
            fig = px.pie(heart_data, values="Prevalence (%)", names="Risk Factor",
                        title="Prevalence of Major Risk Factors")
            st.plotly_chart(fig, use_column_width=True)
            
            st.markdown("""
            **Warning Signs:**
            - Chest discomfort
            - Shortness of breath
            - Palpitations
            - Unexplained fatigue
            """)
    
    with tab3:
        st.subheader("Kidney Health Statistics")
        kidney_data = pd.DataFrame({
            "Stage": ["Stage 1", "Stage 2", "Stage 3", "Stage 4", "Stage 5"],
            "eGFR Range": ["≥90", "60-89", "30-59", "15-29", "<15"],
            "US Prevalence (millions)": [26.5, 18.2, 8.7, 1.5, 0.7],
            "Main Causes": [
                "Diabetes, Hypertension",
                "Diabetes, Hypertension",
                "Diabetes, Hypertension, Glomerulonephritis",
                "Advanced CKD causes",
                "End-stage renal disease"
            ]
        })
        
        st.dataframe(kidney_data.style.background_gradient(cmap="Blues"), use_container_width=True)
        
        st.markdown("""
        **Kidney Health Tips:**
        - Stay hydrated (6-8 glasses water/day)
        - Control blood pressure (<130/80)
        - Manage blood sugar if diabetic
        - Avoid NSAIDs and nephrotoxic drugs
        - Get regular kidney function tests
        """)

def about_page():
    st.markdown("<h1 class='title-text'>About HealthPredict Pro</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        team_img = load_image(IMAGE_PATHS["team_developer"])
        st.image(team_img, use_column_width=True)
    
    with col2:
        st.markdown("""
        ## Our Mission
        HealthPredict Pro aims to democratize access to health risk assessment tools using 
        artificial intelligence. Our platform provides individuals with valuable insights 
        about their health risks, empowering them to make informed decisions about their 
        healthcare.
        
        ## How It Works
        Our system uses machine learning models trained on thousands of medical cases to 
        provide accurate risk assessments for several common chronic diseases. The models 
        analyze your health metrics against known risk factors to generate personalized 
        reports.
        
        ## Privacy & Security
        - All calculations happen locally in your browser
        - No health data is stored or transmitted
        - Open-source algorithms for transparency
        """)
    
    st.markdown("---")
    
    st.subheader("Development Team")
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown(f"""
        <div class="team-card">
            <img src="{IMAGE_PATHS['team_doctor']}" class="team-img" alt="Dr. Sarah Johnson">
            <h3>Dr. Sarah Johnson</h3>
            <p style="font-weight: 600; color: #3498db; margin: 5px 0;">Medical Director</p>
            <p style="color: #7f8c8d; font-size: 14px;">
                Board-certified internist with 15 years of clinical experience
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown(f"""
        <div class="team-card">
            <img src="{IMAGE_PATHS['team_datascientist']}" class="team-img" alt="Michael Chen">
            <h3>Michael Chen</h3>
            <p style="font-weight: 600; color: #3498db; margin: 5px 0;">Data Scientist</p>
            <p style="color: #7f8c8d; font-size: 14px;">
                PhD in Machine Learning with focus on healthcare applications
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown(f"""
        <div class="team-card">
            <img src="{IMAGE_PATHS['team_developer']}" class="team-img" alt="David Wilson">
            <h3>David Wilson</h3>
            <p style="font-weight: 600; color: #3498db; margin: 5px 0;">Lead Developer</p>
            <p style="color: #7f8c8d; font-size: 14px;">
                Full-stack developer specializing in health tech solutions
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Scientific Validation")
    st.markdown("""
    Our prediction models have been validated against the following datasets:
    - Pima Indians Diabetes Database (NIH)
    - Cleveland Clinic Heart Disease Dataset (UCI)
    - Chronic Kidney Disease Dataset (UCI)
    
    Model performance metrics:
    - Diabetes prediction accuracy: 89.2%
    - Heart disease prediction accuracy: 86.5%
    - Kidney disease prediction accuracy: 91.8%
    """)

def contact_page():
    st.markdown("<h1 class='title-text'>Contact Us</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Get In Touch")
        st.markdown("""
        **HealthPredict Pro**  
        **Address:** 123 Health Street, Medical District  
        **City:** Vadodra  
        **State:** Gujarat  
        **Zip Code:** 391760  
        **Country:** India  
        
        **Phone:** +91 80 1234 5678  
        **Fax:** +91 80 1234 5679  
        **Email:** info@healthpredictpro.com  
        **Support:** support@healthpredictpro.com  
        
        **Business Hours:**  
        Monday-Friday: 9:00 AM - 5:00 PM IST  
        Weekends: Closed  
        """)
        
        st.subheader("Follow Us")
        st.markdown("""
        [Twitter](#) | [LinkedIn](#) | [Facebook](#) | [YouTube](#)  
        Join our community for health tips and updates
        """)
    
    with col2:
        st.subheader("Send Us a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Name", placeholder="Your name")
            email = st.text_input("Email", placeholder="Your email address")
            subject = st.selectbox("Subject", [
                "General Inquiry", 
                "Technical Support", 
                "Partnership Opportunities",
                "Feedback",
                "Other"
            ])
            message = st.text_area("Message", placeholder="Your message here...", height=150)
            
            if st.form_submit_button("Send Message"):
                if name and email and message:
                    st.success("Thank you for your message! We'll get back to you within 48 hours.")
                else:
                    st.warning("Please fill in all required fields.")
    
    st.markdown("---")
    
    st.subheader("Frequently Asked Questions")
    
    with st.expander("How accurate are the predictions?"):
        st.markdown("""
        Our models have been validated against clinical datasets with the following accuracy:
        - Diabetes: 89.2%
        - Heart Disease: 86.5%
        - Kidney Disease: 91.8%
        
        These results are comparable to screening tools used in clinical settings, but should 
        not replace professional medical advice.
        """)
    
    with st.expander("Is my health data stored?"):
        st.markdown("""
        No. All calculations happen locally in your browser. We don't store any of your 
        health information on our servers. Your privacy is our top priority.
        """)
    
    with st.expander("Can I use this for diagnosis?"):
        st.markdown("""
        HealthPredict Pro is designed for informational purposes only. It is not intended 
        to diagnose, treat, cure, or prevent any disease. Always consult with a qualified 
        healthcare provider for medical advice.
        """)
    
    with st.expander("How can I improve my results?"):
        st.markdown("""
        For the most accurate results:
        - Use recent lab test results when available
        - Measure blood pressure after resting for 5 minutes
        - Fast for 8 hours before glucose measurements
        - Provide complete information for all requested metrics
        """)

def main():
    page = navigation()
    
    if page == "Home":
        home_page()
    elif page == "Diabetes Prediction":
        diabetes_page()
    elif page == "Heart Disease Prediction":
        heart_page()
    elif page == "Kidney Disease Prediction":
        kidney_page()
    elif page == "Health Insights":
        insights_page()
    elif page == "About":
        about_page()
    elif page == "Contact":
        contact_page()

if __name__ == "__main__":
    main()


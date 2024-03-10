import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Disease Prediction",
                   layout="wide",
                   page_icon="🧑‍⚕️")

working_dir = os.path.dirname(os.path.abspath(__file__))


diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'User Manual'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'book'],
                           default_index=0)


if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            # Precautions for Diabetes
            st.subheader("Precautions for Diabetes:")
            st.write("- Maintain a healthy diet and monitor carbohydrate intake.")
            st.write("- Engage in regular physical activity.")
            st.write("- Monitor blood sugar levels regularly.")
            st.subheader("Risk Assessment")
            st.write("- Diabetes requires careful management to prevent complications such as cardiovascular diseases, nerve damage, and kidney problems.")

        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('cp')
    with col1:
        trestbps = st.text_input('trestbps')
    with col2:
        chol = st.text_input('chol')
    with col3:
        fbs = st.text_input('fbs')
    with col1:
        restecg = st.text_input('restecg')
    with col2:
        thalach = st.text_input('thalach')
    with col3:
        exang = st.text_input('exang')
    with col1:
        oldpeak = st.text_input('oldpeak')
    with col2:
        slope = st.text_input('slope')
    with col3:
        ca = st.text_input('ca')
    with col1:
        thal = st.text_input('thal')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            # Precautions for Heart Disease
            st.subheader("Precautions for Heart Disease:")
            st.write("- Maintain a heart-healthy diet low in saturated and trans fats.")
            st.write("- Engage in regular physical activity.")
            st.write("- Monitor blood pressure and cholesterol levels regularly.")
            st.subheader("Risk Assessment")
            st.write("Heart disease requires management to prevent complications such as heart attack and stroke.")

        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
            # Precautions for Parkinson's Disease
            st.subheader("Precautions for Parkinson's Disease:")
            st.write("- Engage in regular physical and occupational therapy.")
            st.write("- Maintain a balanced diet and hydration.")
            st.write("- Ensure proper medication management and follow-up with healthcare providers.")
            st.subheader("Risk Assessment")
            st.write("Parkinson's disease is a progressive disorder that requires ongoing care and management.")
                       

        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# User Manual Page
if selected == "User Manual":
    st.title("User Manual")

    st.subheader("Diabetes Prediction:")
    st.subheader("Diabetes mellitus, commonly referred to as diabetes, is a chronic condition characterized by high levels of sugar (glucose) in the blood. It occurs when the body either does not produce enough insulin or cannot effectively use the insulin it produces. Symptoms may include increased thirst, frequent urination, fatigue, and blurred vision.")

    st.write("Diabetes prediction requires the following input values:")
    st.write("- Number of Pregnancies: Number of pregnancies the individual has experienced.")
    st.write("- Glucose Level: The glucose concentration in the blood.")
    st.write("- Blood Pressure value: Blood pressure measurement.")
    st.write("- Skin Thickness value: Skin thickness measurement.")
    st.write("- Insulin Level: Insulin concentration in the blood.")
    st.write("- BMI value: Body Mass Index (BMI) calculation.")
    st.write("- Diabetes Pedigree Function value: Diabetes pedigree function.")
    st.write("- Age of the Person: Age of the individual.")

    st.subheader("Heart Disease Prediction:")
    st.subheader("Heart disease, also known as cardiovascular disease, encompasses a range of conditions affecting the heart and blood vessels. It often involves the build-up of fatty deposits in the arteries, leading to reduced blood flow to the heart. Symptoms may include chest pain, shortness of breath, fatigue, and irregular heartbeat.")

    st.write("Heart disease prediction requires the following input values:")
    st.write("- Age: Age of the individual.")
    st.write("- Sex: Gender of the individual (0 for female, 1 for male).")
    st.write("- cp: Chest pain type (0 to 3).")
    st.write("- trestbps: Resting blood pressure.")
    st.write("- chol: Serum cholesterol level.")
    st.write("- fbs: Fasting blood sugar level (> 120 mg/dl as 1, else 0).")
    st.write("- restecg: Resting electrocardiographic results.")
    st.write("- thalach: Maximum heart rate achieved.")
    st.write("- exang: Exercise induced angina (1 for yes, 0 for no).")
    st.write("- oldpeak: ST depression induced by exercise relative to rest.")
    st.write("- slope: Slope of the peak exercise ST segment.")
    st.write("- ca: Number of major vessels colored by fluoroscopy.")
    st.write("- thal: Thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect).")

    st.subheader("Parkinson's Disease Prediction:")
    st.subheader("Parkinson's disease is a progressive nervous system disorder that affects movement. It occurs when nerve cells in the brain gradually break down or die, leading to a decrease in dopamine levels. Symptoms may include tremors, stiffness, slowness of movement, and impaired balance and coordination.")

    st.write("Parkinson's disease prediction requires the following input values:")
    st.write("- MDVP:Fo(Hz): Fundamental frequency.")
    st.write("- MDVP:Fhi(Hz): Highest frequency.")
    st.write("- MDVP:Flo(Hz): Lowest frequency.")
    st.write("- MDVP:Jitter(%): Jitter in percentage.")
    st.write("- MDVP:Jitter(Abs): Absolute jitter.")
    st.write("- MDVP:RAP: Relative amplitude perturbation.")
    st.write("- MDVP:PPQ: Five-point period perturbation quotient.")
    st.write("- Jitter:DDP: Average absolute difference of differences between jitter cycles.")
    st.write("- MDVP:Shimmer: Shimmer in dB.")
    st.write("- MDVP:Shimmer(dB): Shimmer in decibels.")
    st.write("- Shimmer:APQ3: Amplitude perturbation quotient.")
    st.write("- Shimmer:APQ5: Amplitude perturbation quotient.")
    st.write("- MDVP:APQ: Amplitude perturbation quotient.")
    st.write("- Shimmer:DDA: Average absolute differences between the amplitudes of consecutive periods.")
    st.write("- NHR: Noise-to-harmonics ratio.")
    st.write("- HNR: Harmonics-to-noise ratio.")
    st.write("- RPDE: Recurrence period density entropy measure.")
    st.write("- DFA: Detrended fluctuation analysis.")
    st.write("- spread1: Spread1.")
    st.write("- spread2: Spread2.")
    st.write("- D2: Correlation dimension.")
    st.write("- PPE: Pitch period entropy.")

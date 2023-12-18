@author: Ajay
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open("trained_model.sav","rb"))
 
heart_disease_model = pickle.load(open("heart_train_model.sav","rb"))

Parkinsons_Disease_model = pickle.load(open("parkinson_train_model.sav","rb"))

# sidebar for navigation

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System",
                           ["Diabetes Prediction",
                            "Heart Disease Prediction",
                            "Parkinsons Prediction"],
                           icons = ["activity","heart","person"],
                           default_index = 0)
    
#Diabetes Prediction Page

if(selected == "Diabetes Prediction"):
    
    #page title
    st.title("Diabetes Prediction Using ML")
    
    #Getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        
    with col2:
        Glucose = st.text_input("Glucose Level")
        
    with col3:
        BloodPressure = st.text_input("BloodPressure Value")
        
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
        
    with col2:
        Insulin = st.text_input("Insulin Level")
        
    with col3:
        BMI = st.text_input("BMI Value")
        
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetic Prediction Function Value")
        
    with col2:
        Age = st.text_input("Age of the Person")
        
        
        
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button("Diabetes Test Result"):
        diagnosis_Pre = diabetes_model.predict([[ Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction, Age]])
        
        if (diagnosis_Pre[0]==0):
            diagnosis = "The Person is not Diabetic"
            
        else:
            diagnosis = "The Person is Diabetic"
            
    st.success(diagnosis)
        
    
if(selected == "Heart Disease Prediction"):
    
    #page title
    st.title("Heart Disease Prediction Using ML")
    
     
    #Getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Enter your age")
        
    with col2:
        sex = st.text_input("What is Your sex")
        
    with col3:
        cp = st.text_input("Enter your cp")
        
    with col1:
        trestbps= st.text_input("Enter trestbps")
        
    with col2:
        chol = st.text_input("Enter chol")
        
    with col3:
        fbs = st.text_input("Enter fbs")
        
    with col1:
        restecg=st.text_input("Enter restecg")
        
    with col2:
        thalach = st.text_input("Enter thalach")
        
    with col3:
        exang = st.text_input("Enter exang")
        
    with col1:
        oldpeak = st.text_input("Enter oldpeak")
        
    with col2:
        slope = st.text_input("Enter slope")
        
    with col3:
        ca = st.text_input("Enter ca")
        
    with col1:
        thal = st.text_input("Enter thal")
        
    disease = ''
     
    if st.button("Heart Disease Result"):
        
         
        disease_pre = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (disease_pre[0]==0):
            
            disease = "The Person is Healthy"
             
        else:
            
            disease = "The Person has Heart Disease"
            
    st.success(disease)
            
         
    
if(selected == "Parkinsons Prediction"):
    
    #page title
    st.title("Parkinsons Prediction Using ML")
    
      
    #Getting the input data from the user
    #columns for input fields
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
       MDVPFo = st.text_input("Enter MDVP:Fo(Hz)")
   
    with col2:
        MDVPFhi = st.text_input("Enter MDVP:Fhi(Hz)")
    
    with col3:
        MDVPFlo = st.text_input("Enter MDVP:Flo(Hz)")
    
    with col4:
        MDVPJitter = st.text_input("Enter MDVP:Jitter")
   
    with col1:
        MDVPJitter2 = st.text_input("Enter  MDVP:Jitter(Abs)")
    
    with col2:
        MDVPRAP = st.text_input("Enter MDVP:RAP")
   
    with col3:
        MDVPPPQ = st.text_input("Enter MDVP:PPQ")
    
    with col4:
        JitterDDP = st.text_input("Enter Jitter:DDP")
   
    with col1:
        MDVPShimmer = st.text_input("Enter MDVP:Shimmer")
   
    with col2:
        MDVPShimmer2 = st.text_input("Enter MDVP:Shimmer(dB)")
    
    with col3:
        ShimmerAPQ3 = st.text_input("Enter Shimmer:APQ3")
   
    with col4:
        ShimmerAPQ5 = st.text_input("Enter Shimmer:APQ5")
   
    with col1:
        MDVPAPQ = st.text_input("Enter  MDVP:APQ")
    
    with col2:
        ShimmerDDA = st.text_input("Enter Shimmer:DDA")
    
    with col3:
        NHR = st.text_input("Enter NHR")
   
    with col4:
        HNR = st.text_input("Enter  HNR")
   
    with col1:
        RPDE = st.text_input("Enter RPDE")
   
    with col2:
        DFA = st.text_input("Enter DFA")
    
    with col3:
        spread1 = st.text_input("Enter spread1")
   
    with col4:
        spread2 = st.text_input("Enter spread2")
        
    with col1:
       D2 = st.text_input("Enter D2")
   
    with col2:
        PPE = st.text_input("Enter PPE")
        
    Parkinson_Dise = ''
     
    if st.button("Parkinsons Predict Result"):
        
        
        Parkinson_Pre = Parkinsons_Disease_model.predict([[MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitter2,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmer2,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if (Parkinson_Pre[0]==0):
            Parkinson_Dise = "The Preson is Healthy"
            
        else:
            Parkinson_Dise = "The Preson has Parkinsons Disease"
            
    st.success(Parkinson_Dise)
         

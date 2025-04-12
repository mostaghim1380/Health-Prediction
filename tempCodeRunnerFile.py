# UI Streamlit
# with st.sidebar:
#     selected = option_menu("Multiple Disease Prediction", 
#                 ['Diabetes Prediction', 'Heart Disease Prediction', 'Kidney Disease Prediction'],
#                  menu_icon='hospital-fill', icons=['activity','heart', 'person'], default_index=0)

# if selected == 'Diabetes Prediction':
#     st.title("Diabetes Prediction Using Machine Learning")

#     col1, col2, col3 = st.columns(3)
#     Pregnancies = col1.text_input("Number of Pregnancies")
#     Glucose = col2.text_input("Glucose Level")
#     BloodPressure = col3.text_input("BloodPressure Value")
#     SkinThickness = col1.text_input("SkinThickness Value")
#     Insulin = col2.text_input("Insulin Value")
#     BMI = col3.text_input("BMI Value")
#     DiabetesPedigreeFunction = col1.text_input("DiabetesPedigreeFunction Value")
#     Age = col2.text_input("Age")

#     diabetes_result = ""

#     if st.button("Diabetes Test Result"):
#         try:
#             # دسته‌بندی BMI
#             NewBMI_Underweight = int(float(BMI) <= 18.5)
#             NewBMI_Overweight = int(24.9 < float(BMI) <= 29.9)
#             NewBMI_Obesity_1 = int(29.9 < float(BMI) <= 34.9)
#             NewBMI_Obesity_2 = int(34.9 < float(BMI) <= 39.9)
#             NewBMI_Obesity_3 = int(float(BMI) > 39.9)

#             # دسته‌بندی Insulin
#             NewInsulinScore_Normal = int(16 <= float(Insulin) <= 166)

#             # دسته‌بندی Glucose
#             NewGlucose_Low = int(float(Glucose) <= 70)
#             NewGlucose_Normal = int(70 < float(Glucose) <= 99)
#             NewGlucose_Overweight = int(99 < float(Glucose) <= 126)
#             NewGlucose_Secret = int(float(Glucose) > 126)

#             user_input = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
#                           BMI,DiabetesPedigreeFunction,Age,NewBMI_Underweight,
#                           NewBMI_Overweight,NewBMI_Obesity_1,NewBMI_Obesity_2,
#                           NewBMI_Obesity_3,NewInsulinScore_Normal,NewGlucose_Low,
#                           NewGlucose_Normal,NewGlucose_Overweight,NewGlucose_Secret]

#             user_input = [float(x) if x != '' else 0 for x in user_input]

#             prediction = diabetes_model.predict([user_input])

#             if prediction[0] == 1:
#                 diabetes_result = "The person has diabetes."
#             else:
#                 diabetes_result = "The person does not have diabetes."

#         except ValueError:
#             st.error("لطفاً همه مقادیر را به درستی وارد کنید.")

#     st.success(diabetes_result)
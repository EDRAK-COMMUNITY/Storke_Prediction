# import the necessary packages
import gradio as gr
import pickle
import pandas as pd

# Load the saved model using pickle
with open('../model/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a function to make predictions


def predict(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):
    # Convert the input into a pandas DataFrame
    input_df = pd.DataFrame([[gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]],
                            columns=['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type',
                                     'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status'])
    # Predict the stroke probability
    prediction = model.predict_proba(input_df)[0][1]
    # Return the prediction
    result = "The probability of stroke is {:.2f}%".format(prediction * 100) #to give a percentage 
    return result


# Create the input and output interfaces
gender = gr.inputs.Radio(choices=["Male", "Female"], label="Gender")
age = gr.inputs.Slider(minimum=0, maximum=100)
hypertension = gr.inputs.Radio(choices=["Yes", "No"], label="Hypertension")
heart_disease = gr.inputs.Radio(choices=["Yes", "No"], label="Heart Disease")
ever_married = gr.inputs.Radio(choices=["Yes", "No"], label="Ever Married")
work_type = gr.inputs.Dropdown(
    ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"], label="Work Type")
residence_type = gr.inputs.Radio(
    choices=["Urban", "Rural"], label="Residence Type")
avg_glucose_level = gr.inputs.Number(label="Average Glucose Level")
bmi = gr.inputs.Slider(minimum=0, maximum=60, label="BMI")
smoking_status = gr.inputs.Dropdown(
    ["formerly smoked", "never smoked", "smokes"], label="Smoking Status")

# Create the interface
inputs = [gender, age, hypertension, heart_disease, ever_married,
          work_type, residence_type, avg_glucose_level, bmi, smoking_status]
outputs = gr.outputs.Textbox(label="Stroke Probability")

# Launch the interface
demo = gr.Interface(fn=predict, inputs=inputs, outputs=outputs, title="Stroke Prediction",
                    description="Fill in the details and click submit to check the probability of stroke")
demo.launch(share=True)

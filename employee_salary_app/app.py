import streamlit as st
import pandas as pd
import pickle

# Load your trained model
model = pickle.load(open('model_pickle.pkl', 'rb'))

# Mapping Dictionaries (Example mappings, adjust based on your dataset's encoding)
workclass_mapping = {
    'Private': 0,
    'Self-emp-not-inc': 1,
    'Self-emp-inc': 2,
    'Federal-gov': 3,
    'Local-gov': 4,
    'State-gov': 5,
    'Without-pay': 6,
    'Never-worked': 7
}

marital_status_mapping = {
    'Married-civ-spouse': 0,
    'Divorced': 1,
    'Never-married': 2,
    'Separated': 3,
    'Widowed': 4,
    'Married-spouse-absent': 5
}

occupation_mapping = {
    'Tech-support': 0,
    'Craft-repair': 1,
    'Other-service': 2,
    'Sales': 3,
    'Exec-managerial': 4,
    'Prof-specialty': 5,
    'Handlers-cleaners': 6,
    'Machine-op-inspct': 7,
    'Adm-clerical': 8,
    'Farming-fishing': 9,
    'Transport-moving': 10,
    'Priv-house-serv': 11,
    'Protective-serv': 12,
    'Armed-Forces': 13
}

relationship_mapping = {
    'Wife': 0,
    'Own-child': 1,
    'Husband': 2,
    'Not-in-family': 3,
    'Other-relative': 4,
    'Unmarried': 5
}

race_mapping = {
    'White': 0,
    'Asian-Pac-Islander': 1,
    'Amer-Indian-Eskimo': 2,
    'Other': 3,
    'Black': 4
}

gender_mapping = {'Male': 0, 'Female': 1}

native_country_mapping = {
    'United-States': 0,
    'Other': 1  # You can expand this dictionary if needed
}

# Streamlit frontend
st.title('Employee Salary Prediction')

# Inputs
age = st.number_input('Age', min_value=17, max_value=90)
workclass = st.selectbox('Workclass', list(workclass_mapping.keys()))
fnlwgt = st.number_input('FNLWGT')
edu_num = st.number_input('Education Number', min_value=1, max_value=16)
marital_status = st.selectbox('Marital Status', list(marital_status_mapping.keys()))
occupation = st.selectbox('Occupation', list(occupation_mapping.keys()))
relationship = st.selectbox('Relationship', list(relationship_mapping.keys()))
race = st.selectbox('Race', list(race_mapping.keys()))
gender = st.selectbox('Gender', list(gender_mapping.keys()))
capital_gain = st.number_input('Capital Gain')
capital_loss = st.number_input('Capital Loss')
hours_per_week = st.number_input('Hours per Week', min_value=1, max_value=100)
native_country = st.selectbox('Native Country', list(native_country_mapping.keys()))

if st.button('Predict Income'):
    input_data = pd.DataFrame({
        'age': [age],
        'workclass': [workclass_mapping[workclass]],
        'fnlwgt': [fnlwgt],
        'educational-num': [edu_num],
        'marital-status': [marital_status_mapping[marital_status]],
        'occupation': [occupation_mapping[occupation]],
        'relationship': [relationship_mapping[relationship]],
        'race': [race_mapping[race]],
        'gender': [gender_mapping[gender]],
        'capital-gain': [capital_gain],
        'capital-loss': [capital_loss],
        'hours-per-week': [hours_per_week],
        'native-country': [native_country_mapping[native_country]]
    })

    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Income Group: {prediction}')

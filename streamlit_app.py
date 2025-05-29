import streamlit as st 
import requests

# Set the app title 
st.title('My first class with Dr. Zamri !!') 

# Add a welcome message 
st.write('Welcome to my ACAP Streamlit app!') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)

# First, get the list of all currencies (we'll use MYR as default for this request)
initial_response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if initial_response.status_code == 200:
    initial_data = initial_response.json()
    all_currencies = sorted(initial_data['rates'].keys())

    # Add MYR to the list if it's not there (since MYR is the base, it may not appear in 'rates')
    if 'MYR' not in all_currencies:
        all_currencies.append('MYR')
        all_currencies.sort()

    # Dropdown for selecting base currency
    base_currency = st.selectbox('Select your base currency:', all_currencies)

    # Fetch exchange rates for the selected base currency
    response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency}')

    if response.status_code == 200:
        data = response.json()
        rates = data['rates']

        st.write(f"### Exchange Rates for 1 {base_currency}")
        st.json(rates)  # display all exchange rates in JSON format

    else:
        st.error(f"API call failed with status code: {response.status_code}")
else:
    st.error(f"Failed to fetch initial currency list. Status code: {initial_response.status_code}")

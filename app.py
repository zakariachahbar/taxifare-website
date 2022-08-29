import streamlit as st
import numpy as np
import pandas as pd
import requests
import datetime
import json

'''
# TaxiFareModel front
'''
# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

# pickup_date_test = 20130706
# pickup_time_test = 17:18:00
pickup_latitude_test = 40.783282
pickup_longitude_test = -73.950655
dropoff_latitude_test = 40.763137
dropoff_longitude_test = 73.993014

with st.form('Get Fare'):
    pickup_date = st.date_input(label='Pickup Date')
    # pickup_date = pickup_date_test

    pickup_time = st.time_input(label='Pickup Time')
    # pickup_time = pickup_time_test

    # pickup_latitude = st.text_input(label="Pickup Latitude")
    # pickup_latitude = pickup_latitude_test
    pickup_latitude = st.number_input(label="Pickup Latitude", min_value=pickup_latitude_test)

    # pickup_longitude = st.text_input(label="Pickup Longitude")
    # pickup_longitude = pickup_longitude_test
    pickup_longitude = st.number_input(label="Pickup Longitude", min_value=pickup_longitude_test)

    # dropoff_latitude = st.text_input(label="Dropoff Latitude")
    # dropoff_latitude = dropoff_latitude_test
    dropoff_latitude = st.number_input(label="Dropoff Latitude", min_value=dropoff_latitude_test)

    # dropoff_longitude = st.text_input(label="Dropoff Longitude")
    # dropoff_longitude = dropoff_longitude_test
    dropoff_longitude = st.number_input(label="Dropoff Longitude", min_value=dropoff_longitude_test)

    passenger_count = st.number_input(label="Passenger Count", min_value=1, key='int')

    submitted = st.form_submit_button('Get Fare')

# data = pd.DataFrame({
#     'awesome cities' : ['New York', 'New York'],
#     'lat' : [pickup_latitude_test, dropoff_latitude_test],
#     'lon' : [dropoff_latitude_test, dropoff_longitude_test]
# })

# Adding code so we can have map default to the center of the data
# midpoint = (np.average(data['lat']), np.average(data['lon']))

# st.map(data=data)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':
#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
2. Let's build a dictionary containing the parameters for our API...
'''
if submitted:
    parameters = {
        'pickup_datetime': datetime.datetime.combine(pickup_date, pickup_time),
        'pickup_latitude': float(pickup_latitude),
        'pickup_longitude': float(pickup_longitude),
        'dropoff_latitude': float(dropoff_latitude),
        'dropoff_longitude': float(dropoff_longitude),
        'passenger_count': int(passenger_count)
    }

'''
3. Let's call our API using the `requests` package...
'''
response = requests.get(url=url, params=parameters)

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...
'''
st.write(response.content)
st.write(type(response.content))
content = response.content
content_dict_str = content.decode('utf-8')
content_data = json.loads(content_dict_str)

'''
## Finally, we can display the prediction to the user
'''
fare = round(content_data['fare'], 2)
st.write(f'''Your predicted fare is {fare}''')

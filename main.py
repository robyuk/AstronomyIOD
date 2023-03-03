import streamlit as st
import requests

_debug_ = False
url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

web_data = requests.get(url)
content = web_data.json()
image_url = content['url']
image_title = content['title']
image_description = content['explanation']

image = requests.get(image_url).content

if _debug_:
    print(type(image))
    with open('image.jpg', 'wb') as file:
        file.write(image)

st.image(image)
st.title(image_title)
image_description
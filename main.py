import streamlit as st
import torch
import torchvision
import cv2
import time

with st.sidebar:
    image = st.file_uploader(label = 'Updoad the photo')
    st.write('...or')
    image = st.camera_input(label = 'Take a photo')
    
if image: 
    with st.spinner('Wait for it...'):
        time.sleep(5)

    st.image(image)
    st.success('Done!')

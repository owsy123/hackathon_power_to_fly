import cv2
import streamlit as st
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import easyocr

def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr


def main_loop():
    st.title("Hackathon")
    st.subheader("This app Indentify the personal information")
    st.text("We Use OCR and Streamlit in this POC")
    image_file = st.file_uploader("Upload Your Image")#, type=['jpg', 'png', 'jpeg','webp']
    if not image_file:
        return None
    
    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    reader = easyocr.Reader(['en'])
    result = reader.readtext(original_image)
    text = ""
    for i in result:
        text += " "+i[1]
    
    spacer = 100
    font = cv2.FONT_HERSHEY_SIMPLEX

    for detection in result: 
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        img = cv2.rectangle(original_image,top_left,bottom_right,(0,255,0),3)
        img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
        spacer+=15
    plt.figure(figsize = (20,20))    

    st.image([original_image]) 
    personal_info = ['visa','master','paypak','user name','name']

    for i in personal_info:
        if i in text.lower():
            return st.subheader('Sensitive and Personal Information Found')
        
        return st.subheader('Sensitive and Personal Information Not Found')


if __name__ == '__main__':
    main_loop()
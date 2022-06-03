# Writen for use with streamlit.io
#from asyncio.windows_events import NULL
#from curses.ascii import NUL
from ast import IsNot
from operator import is_not
from numpy import RankWarning
import streamlit as st
import requests, json 
import pandas as pd
from PIL import Image
import time
from requests.structures import CaseInsensitiveDict
import csv

endpoint= st.sidebar.selectbox("Endpoints", ['Baus','Panzer', 'Lotene','Sma11','Misterbeans'])
st.title(f"SMA11'S WHEELS BLACK BOOK - {endpoint}") 

# Get Opensea api
collection_slug="wilderworld"
asset_contract_address="0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D"
st.header ("Wilder World") 
if endpoint=="Baus":
    st.write("Baus")

elif endpoint == 'Sma11':
    st.sidebar.subheader("Filters")
    moto_dict={}
    moto={}
    filename="moto.csv"
    with open (filename,'r') as data:
        for line in csv.DictReader(data):
            
            col1, col2 = st.columns(2)
            with col1:
                st.image(line['image'])
               

            with col2:
                moto_dict={'trait':'Top Chassis','value':line['Top Chassis']},{'trait':'Side Cart','value':line['Side Cart']},{'trait':'Pattern','value':line['Pattern']},{'trait':'Color','value':line['Color']}, {'trait':'Number Plate','value':line['Number Plate']} 
                df = pd.DataFrame(moto_dict)
                st.dataframe(df,400,200)
                pic1 = line['image']    
                link_pic = f'[Pic]({pic1})'     
                st.markdown(link_pic, unsafe_allow_html=True) 
                animation1 = line['animation_url']    
                link_animation = f'[Video]({animation1})'     
                st.markdown(link_animation, unsafe_allow_html=True) 
                if line['Color']=='Color 0':
                    moto_dict2={'trait':'Base & Light','value':'#6BACDF'},{'trait':'Second Color','value':'#00193F'}, {'trait':'Third Color','value':'#D3B486'}
                    df=pd.DataFrame(moto_dict2)
                    st.dataframe(df,400,200)

            
            st.write(line['Pattern'])
            col1, col2 = st.columns(2)
            with col1:
           
                if line['Pattern']=='Pattern 3':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_79RFQST5QM37N.jpeg'
                    st.image(pattern_image)
            with col2:
                st.write("Color options")

            st.markdown("""---""")
            #st.video(line['animation_url'])     
            #st.write(line)




                

          
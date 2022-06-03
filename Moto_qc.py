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
    st.sidebar.subheader("Filters")
    moto_dict={}
    moto={}
    filename="Baus_moto.csv"
    with open (filename,'r') as data:
        for line in csv.DictReader(data):
            
            col1, col2 = st.columns(2)
            with col1:
                st.image(line['image'])
                st.write("Sidecar",line['Side Cart'])
               

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

                # if line['Color']=='Color 0':
                #     moto_dict2={'trait':'Base & Light','value':'#6BACDF'},{'trait':'Second Color','value':'#00193F'}, {'trait':'Third Color','value':'#D3B486'}
                #     df=pd.DataFrame(moto_dict2)
                #     st.dataframe(df,400,200)

            
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("CHASSIS ", line['Top Chassis'])
                if line['Top Chassis']=='Wheeled':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_MNT1LR4Y3PQSC.jpeg'

                elif line['Top Chassis']=='Sport':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5GKTR0KO8LR4X.jpeg'
               
                elif line['Top Chassis']=='Exotic':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_INVRFKVS4STYC.jpeg'
                                         
                elif line['Top Chassis']=='Hover':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                st.image(chassis_image)
                link_chassis = f'[Pic]({chassis_image})'  
                st.markdown(link_chassis, unsafe_allow_html=True) 

            with col2:
                st.write(line['Pattern'])
                if line['Pattern']=='Pattern 0':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6NAC9TFV1RSI7.jpeg'

                elif line['Pattern']=='Pattern 1':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RZ29BL791P5I9.jpeg'
               
                elif line['Pattern']=='Pattern 2':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6XZVW0INCUBOR.jpeg'
                                         
                elif line['Pattern']=='Pattern 3':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_79RFQST5QM37N.jpeg'
 
                elif line['Pattern']=='Pattern 4':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O6U62OUTJNAGD.jpeg'
               
                elif line['Pattern']=='Pattern 5':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_QF4JEGB7KQ3VP.jpeg'
                                         
                elif line['Pattern']=='Pattern 6':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_9VB0RAV2QAPP9.jpeg'
                elif line['Pattern']=='Pattern 7':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_98VHDRWX44A8W.jpeg'
               
                elif line['Pattern']=='Pattern 8':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_TX4VHVZSUMIW1.jpeg'
                                         
                elif line['Pattern']=='Pattern 9':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_1ZDR0K5IS9AHR.jpeg'
                elif line['Pattern']=='Pattern 10':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_E2VHPW0TWWO5T.jpeg'
               
                elif line['Pattern']=='Pattern 11':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_UIZT0I3L71EHT.jpeg'
                                         
                elif line['Pattern']=='Pattern 12':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_PZP8LP7NEJY5U.jpeg'

                elif line['Pattern']=='Pattern 13':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O9DDQSGPFN1IZ.jpeg'
                                               
                elif line['Pattern']=='Pattern 14':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                                               
                st.image(pattern_image)
                link_pattern = f'[Pic]({pattern_image})'  
                st.markdown(link_pattern, unsafe_allow_html=True) 

            st.markdown("""---""")
            st.markdown("""---""")



elif endpoint == 'Panzer':
    st.sidebar.subheader("Filters")
    moto_dict={}
    moto={}
    filename="Panzer_moto.csv"
    with open (filename,'r') as data:
        for line in csv.DictReader(data):
            
            col1, col2 = st.columns(2)
            with col1:
                st.image(line['image'])
                st.write("Sidecar",line['Side Cart'])
               

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

                # if line['Color']=='Color 0':
                #     moto_dict2={'trait':'Base & Light','value':'#6BACDF'},{'trait':'Second Color','value':'#00193F'}, {'trait':'Third Color','value':'#D3B486'}
                #     df=pd.DataFrame(moto_dict2)
                #     st.dataframe(df,400,200)

            
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("CHASSIS ", line['Top Chassis'])
                if line['Top Chassis']=='Wheeled':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_MNT1LR4Y3PQSC.jpeg'

                elif line['Top Chassis']=='Sport':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5GKTR0KO8LR4X.jpeg'
               
                elif line['Top Chassis']=='Exotic':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_INVRFKVS4STYC.jpeg'
                                         
                elif line['Top Chassis']=='Hover':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                st.image(chassis_image)
                link_chassis = f'[Pic]({chassis_image})'  
                st.markdown(link_chassis, unsafe_allow_html=True) 

            with col2:
                st.write(line['Pattern'])
                if line['Pattern']=='Pattern 0':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6NAC9TFV1RSI7.jpeg'

                elif line['Pattern']=='Pattern 1':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RZ29BL791P5I9.jpeg'
               
                elif line['Pattern']=='Pattern 2':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6XZVW0INCUBOR.jpeg'
                                         
                elif line['Pattern']=='Pattern 3':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_79RFQST5QM37N.jpeg'
 
                elif line['Pattern']=='Pattern 4':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O6U62OUTJNAGD.jpeg'
               
                elif line['Pattern']=='Pattern 5':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_QF4JEGB7KQ3VP.jpeg'
                                         
                elif line['Pattern']=='Pattern 6':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_9VB0RAV2QAPP9.jpeg'
                elif line['Pattern']=='Pattern 7':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_98VHDRWX44A8W.jpeg'
               
                elif line['Pattern']=='Pattern 8':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_TX4VHVZSUMIW1.jpeg'
                                         
                elif line['Pattern']=='Pattern 9':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_1ZDR0K5IS9AHR.jpeg'
                elif line['Pattern']=='Pattern 10':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_E2VHPW0TWWO5T.jpeg'
               
                elif line['Pattern']=='Pattern 11':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_UIZT0I3L71EHT.jpeg'
                                         
                elif line['Pattern']=='Pattern 12':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_PZP8LP7NEJY5U.jpeg'

                elif line['Pattern']=='Pattern 13':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O9DDQSGPFN1IZ.jpeg'
                                               
                elif line['Pattern']=='Pattern 14':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                                               
                st.image(pattern_image)
                link_pattern = f'[Pic]({pattern_image})'  
                st.markdown(link_pattern, unsafe_allow_html=True) 

            st.markdown("""---""")
            st.markdown("""---""")

elif endpoint == 'Lotene':
    st.sidebar.subheader("Filters")
    moto_dict={}
    moto={}
    filename="Lotene_moto.csv"
    with open (filename,'r') as data:
        for line in csv.DictReader(data):
            
            col1, col2 = st.columns(2)
            with col1:
                st.image(line['image'])
                st.write("Sidecar",line['Side Cart'])
               

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

                # if line['Color']=='Color 0':
                #     moto_dict2={'trait':'Base & Light','value':'#6BACDF'},{'trait':'Second Color','value':'#00193F'}, {'trait':'Third Color','value':'#D3B486'}
                #     df=pd.DataFrame(moto_dict2)
                #     st.dataframe(df,400,200)

            
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("CHASSIS ", line['Top Chassis'])
                if line['Top Chassis']=='Wheeled':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_MNT1LR4Y3PQSC.jpeg'

                elif line['Top Chassis']=='Sport':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5GKTR0KO8LR4X.jpeg'
               
                elif line['Top Chassis']=='Exotic':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_INVRFKVS4STYC.jpeg'
                                         
                elif line['Top Chassis']=='Hover':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                st.image(chassis_image)
                link_chassis = f'[Pic]({chassis_image})'  
                st.markdown(link_chassis, unsafe_allow_html=True) 

            with col2:
                st.write(line['Pattern'])
                if line['Pattern']=='Pattern 0':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6NAC9TFV1RSI7.jpeg'

                elif line['Pattern']=='Pattern 1':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RZ29BL791P5I9.jpeg'
               
                elif line['Pattern']=='Pattern 2':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6XZVW0INCUBOR.jpeg'
                                         
                elif line['Pattern']=='Pattern 3':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_79RFQST5QM37N.jpeg'
 
                elif line['Pattern']=='Pattern 4':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O6U62OUTJNAGD.jpeg'
               
                elif line['Pattern']=='Pattern 5':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_QF4JEGB7KQ3VP.jpeg'
                                         
                elif line['Pattern']=='Pattern 6':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_9VB0RAV2QAPP9.jpeg'
                elif line['Pattern']=='Pattern 7':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_98VHDRWX44A8W.jpeg'
               
                elif line['Pattern']=='Pattern 8':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_TX4VHVZSUMIW1.jpeg'
                                         
                elif line['Pattern']=='Pattern 9':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_1ZDR0K5IS9AHR.jpeg'
                elif line['Pattern']=='Pattern 10':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_E2VHPW0TWWO5T.jpeg'
               
                elif line['Pattern']=='Pattern 11':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_UIZT0I3L71EHT.jpeg'
                                         
                elif line['Pattern']=='Pattern 12':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_PZP8LP7NEJY5U.jpeg'

                elif line['Pattern']=='Pattern 13':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O9DDQSGPFN1IZ.jpeg'
                                               
                elif line['Pattern']=='Pattern 14':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                                               
                st.image(pattern_image)
                link_pattern = f'[Pic]({pattern_image})'  
                st.markdown(link_pattern, unsafe_allow_html=True) 

            st.markdown("""---""")
            st.markdown("""---""")


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
                st.write("Sidecar",line['Side Cart'])
               

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

                # if line['Color']=='Color 0':
                #     moto_dict2={'trait':'Base & Light','value':'#6BACDF'},{'trait':'Second Color','value':'#00193F'}, {'trait':'Third Color','value':'#D3B486'}
                #     df=pd.DataFrame(moto_dict2)
                #     st.dataframe(df,400,200)

            
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("CHASSIS ", line['Top Chassis'])
                if line['Top Chassis']=='Wheeled':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_MNT1LR4Y3PQSC.jpeg'

                elif line['Top Chassis']=='Sport':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5GKTR0KO8LR4X.jpeg'
               
                elif line['Top Chassis']=='Exotic':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_INVRFKVS4STYC.jpeg'
                                         
                elif line['Top Chassis']=='Hover':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                st.image(chassis_image)
                link_chassis = f'[Pic]({chassis_image})'  
                st.markdown(link_chassis, unsafe_allow_html=True) 

            with col2:
                st.write(line['Pattern'])
                if line['Pattern']=='Pattern 0':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6NAC9TFV1RSI7.jpeg'

                elif line['Pattern']=='Pattern 1':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RZ29BL791P5I9.jpeg'
               
                elif line['Pattern']=='Pattern 2':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6XZVW0INCUBOR.jpeg'
                                         
                elif line['Pattern']=='Pattern 3':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_79RFQST5QM37N.jpeg'
 
                elif line['Pattern']=='Pattern 4':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O6U62OUTJNAGD.jpeg'
               
                elif line['Pattern']=='Pattern 5':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_QF4JEGB7KQ3VP.jpeg'
                                         
                elif line['Pattern']=='Pattern 6':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_9VB0RAV2QAPP9.jpeg'
                elif line['Pattern']=='Pattern 7':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_98VHDRWX44A8W.jpeg'
               
                elif line['Pattern']=='Pattern 8':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_TX4VHVZSUMIW1.jpeg'
                                         
                elif line['Pattern']=='Pattern 9':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_1ZDR0K5IS9AHR.jpeg'
                elif line['Pattern']=='Pattern 10':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_E2VHPW0TWWO5T.jpeg'
               
                elif line['Pattern']=='Pattern 11':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_UIZT0I3L71EHT.jpeg'
                                         
                elif line['Pattern']=='Pattern 12':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_PZP8LP7NEJY5U.jpeg'

                elif line['Pattern']=='Pattern 13':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O9DDQSGPFN1IZ.jpeg'
                                               
                elif line['Pattern']=='Pattern 14':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                                               
                st.image(pattern_image)
                link_pattern = f'[Pic]({pattern_image})'  
                st.markdown(link_pattern, unsafe_allow_html=True) 

            st.markdown("""---""")
            st.markdown("""---""")

elif endpoint == 'Misterbeans':
    st.sidebar.subheader("Filters")
    moto_dict={}
    moto={}
    filename="Misterbeans_moto.csv"
    with open (filename,'r') as data:
        for line in csv.DictReader(data):
            
            col1, col2 = st.columns(2)
            with col1:
                st.image(line['image'])
                st.write("Sidecar",line['Side Cart'])
               

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

                # if line['Color']=='Color 0':
                #     moto_dict2={'trait':'Base & Light','value':'#6BACDF'},{'trait':'Second Color','value':'#00193F'}, {'trait':'Third Color','value':'#D3B486'}
                #     df=pd.DataFrame(moto_dict2)
                #     st.dataframe(df,400,200)

            
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("CHASSIS ", line['Top Chassis'])
                if line['Top Chassis']=='Wheeled':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_MNT1LR4Y3PQSC.jpeg'

                elif line['Top Chassis']=='Sport':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5GKTR0KO8LR4X.jpeg'
               
                elif line['Top Chassis']=='Exotic':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_INVRFKVS4STYC.jpeg'
                                         
                elif line['Top Chassis']=='Hover':
                    chassis_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                st.image(chassis_image)
                link_chassis = f'[Pic]({chassis_image})'  
                st.markdown(link_chassis, unsafe_allow_html=True) 

            with col2:
                st.write(line['Pattern'])
                if line['Pattern']=='Pattern 0':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6NAC9TFV1RSI7.jpeg'

                elif line['Pattern']=='Pattern 1':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_RZ29BL791P5I9.jpeg'
               
                elif line['Pattern']=='Pattern 2':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_6XZVW0INCUBOR.jpeg'
                                         
                elif line['Pattern']=='Pattern 3':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_79RFQST5QM37N.jpeg'
 
                elif line['Pattern']=='Pattern 4':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O6U62OUTJNAGD.jpeg'
               
                elif line['Pattern']=='Pattern 5':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_QF4JEGB7KQ3VP.jpeg'
                                         
                elif line['Pattern']=='Pattern 6':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_9VB0RAV2QAPP9.jpeg'
                elif line['Pattern']=='Pattern 7':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_98VHDRWX44A8W.jpeg'
               
                elif line['Pattern']=='Pattern 8':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_TX4VHVZSUMIW1.jpeg'
                                         
                elif line['Pattern']=='Pattern 9':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_1ZDR0K5IS9AHR.jpeg'
                elif line['Pattern']=='Pattern 10':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_E2VHPW0TWWO5T.jpeg'
               
                elif line['Pattern']=='Pattern 11':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_UIZT0I3L71EHT.jpeg'
                                         
                elif line['Pattern']=='Pattern 12':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_PZP8LP7NEJY5U.jpeg'

                elif line['Pattern']=='Pattern 13':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_O9DDQSGPFN1IZ.jpeg'
                                               
                elif line['Pattern']=='Pattern 14':
                    pattern_image='https://wilder-moto-testing.s3.eu-central-1.amazonaws.com/Folder1/Moto_5VKSF0K0Y0JJL.jpeg'
                                               
                st.image(pattern_image)
                link_pattern = f'[Pic]({pattern_image})'  
                st.markdown(link_pattern, unsafe_allow_html=True) 

            st.markdown("""---""")
            st.markdown("""---""")



                

          
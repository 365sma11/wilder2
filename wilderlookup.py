from typing import Counter
import streamlit as st
import requests, json 
import pandas as pd

data = {'assets': []}
file= "wheelslist.json"
endpoint= st.sidebar.selectbox("Endpoints", ['Media Lookup'])
st.title(f"SMA11'S WHEELS BLACK BOOK - {endpoint}") 




counter=0
howmany=0

if endpoint == 'Collection':
    st.sidebar.subheader("Stats")
   
    collection_slug="wilderworld"
    asset_contract_address="0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D"
    params={}
    r = requests.get(f"https://api.opensea.io/api/v1/asset_contract/{asset_contract_address}",params=params)
    response = r.json()
    st.header (response["collection"]["name"]) 
    st.image(response["collection"]["image_url"],width=40)
    st.image (response["collection"]["banner_image_url"])
    link = '[Contract](https://etherscan.io/address/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d)'
    st.markdown(link, unsafe_allow_html=True)
    # df=pd.read_excel("WILDER_WHEELS.xlsx")
    # st.write(df)
   
#SIDEBAR -One day stats for collection on 
    r = requests.get(f"https://api.opensea.io/api/v1/collection/{collection_slug}/stats",params=params)
    response = r.json()
    st.sidebar.write("Floor Price: ", response["stats"]["floor_price"])
    st.sidebar.write("One day sales: ", response["stats"]["one_day_sales"])
    st.sidebar.write("One day avg price (Eth): ", response["stats"]["one_day_average_price"])
    st.sidebar.write("One day volume (Eth): ", response["stats"]["one_day_volume"])
    st.sidebar.write("Total NFT's: ", response["stats"]["total_supply"])
    st.sidebar.write("Number of Owners: ", response["stats"]["num_owners"])
    
    #st.slider("Select how many days", 1, 100, 100)




if endpoint == 'Media Lookup':
    st.sidebar.subheader("Filters")
    token = st.sidebar.text_input("Token ID")
    params={}
    params['limit']=50
    r=requests.get(f'https://api.covalenthq.com/v1/1/tokens/0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D/nft_metadata/{token}/?quote-currency=USD&format=JSON&key=ckey_fa91923a9dc34181ac2bbbdc82e')
    token_content=r.json()
    st.write(token_content)


    st.write(token_content['data']['items'][0]['nft_data'][0]['external_data']['name'])
    st.image(token_content['data']['items'][0]['nft_data'][0]['external_data']['image_256'])
    image256 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_256']
    image512 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_512']
    image1024 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_1024']
    animation1 = token_content['data']['items'][0]['nft_data'][0]['external_data']['animation_url']      
    opensea= 'https://opensea.io/assets/'+ token_content['data']['items'][0]['contract_address']+ "/" + token_content['data']['items'][0]['nft_data'][0]['token_id']
    st.write(token_content['data']['items'][0]['nft_data'][0]['token_id'])
    opensea_link= f'[OpenSea] ({opensea})'
    st.markdown(opensea_link, unsafe_allow_html=True)
    res=animation1.strip('ipfs://')
    
    animation= "https://ipfs.io/ipfs/"+ res

    link_256 = f'[Image 256] ({image256})'
    link_512 = f'[Image 512]({image512})'
    link_1024 = f'[Image 1024]({image1024})' 
    link_animation = f'[Video]({animation})' 
    st.markdown(link_256, unsafe_allow_html=True)
    st.markdown(link_512, unsafe_allow_html=True)
    st.markdown(link_1024, unsafe_allow_html=True)
    st.markdown(link_animation, unsafe_allow_html=True)

    st.write(token_content['data']['items'][0]['nft_data'][0]['external_data']['attributes'])
    df=token_content['data']['items'][0]['nft_data'][0]['external_data']['attributes']
    st.dataframe(df)
   




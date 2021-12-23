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



if endpoint == 'All':
    r = open('complete_wheels.json', 'r')
    data = r.read()
    response = json.loads(data)
    st.write(response)



if endpoint == 'Media Lookup':
    st.sidebar.subheader("Filters")
    token = st.sidebar.text_input("Token ID")
    params={}
    params['limit']=50
    r=requests.get("https://api.covalenthq.com/v1/1/tokens/0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D/nft_metadata/{token}/?quote-currency=USD&format=JSON&key=ckey_fa91923a9dc34181ac2bbbdc82e")
    token_content=r.json()
    st.write(token_content)
    st.write(response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['external_data']['name'])
    st.image(response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['external_data']['image_256'])
    image256 = response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['external_data']['image_256']
    image512 = response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['external_data']['image_512']
    image1024 = response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['external_data']['image_1024']
    animation1 = response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['external_data']['animation_url']      
    opensea= 'https://opensea.io/assets/'+ response['missing_complete_data'][counter]['data']['items'][0]['contract_address']+ "/" + response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['token_id']
    st.write(response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['token_id'])
    opensea_link= f'[OpenSea] ({opensea})'
    st.markdown(opensea_link, unsafe_allow_html=True)
    res=''
    for i in range(0, len(animation1)):
            if i>=n:
                res= res + animation1[i]
    
    animation= "https://ipfs.io/ipfs/"+ res
    link_256 = f'[Image 256] ({image256})'
    link_512 = f'[Image 512]({image512})'
    link_1024 = f'[Image 1024]({image1024})' 
    link_animation = f'[Video]({animation})' 
    st.markdown(link_256, unsafe_allow_html=True)
    st.markdown(link_512, unsafe_allow_html=True)
    st.markdown(link_1024, unsafe_allow_html=True)
    st.markdown(link_animation, unsafe_allow_html=True)
    r = requests.get("https://api.opensea.io/api/v1/assets/"+response['missing_complete_data'][counter]['data']['items'][0]['contract_address']+ "/" + response['missing_complete_data'][counter]['data']['items'][0]['nft_data'][0]['token_id'])
    current_sale = r.json()
    #st.write(current_sale)



        # if asset['image_256']:
        #     
        #     if asset['image_256'].endswith('mp4') or asset['image_256'].endswith('mov'):
        #         st.video(asset['image_url'])
        #     elif asset['image_256'].endswith('svg'):
        #         svg = requests.get(asset['image_256']).content.decode()
        #         st.image(svg)
        #     elif asset['image_256']:
        #         st.image(asset['image_256'])
         
        # else:
        #     st.write(howmany)
        #     howmany=howmany+1
        #     st.write("image_url is Null")
        #     st.write("Token id is")
        #     st.write(asset['token_id'])
        #     st.write(asset['owner'])

        #st.write(counter)
    

     

    
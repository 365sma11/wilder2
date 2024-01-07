# Writen for use with streamlit.io
import streamlit as st
import requests, json
import pandas as pd
from PIL import Image
from requests.structures import CaseInsensitiveDict
import csv
from moralis import evm_api

os_api= st.secrets["os_api"]
cov_api= st.secrets["cov_api"]
mor_api= st.secrets["mor_api"]
alch_api= st.secrets["alch_api"]

# Placeholder contract addresses for each endpoint
contract_addresses = {
    'Wheels': '0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d',
    'Cribs': '0xfEA385B9E6e4fdfA3508aE6863d540c4a8Ccc0fE',
    'Crafts': '0xE4954E4FB3C448f4eFBC1f8EC40eD54a2A1cc1f5',
    'Motos': '0x51bd5948cf84a1041d2720f56ded5e173396fc95',
    'AirWILD0': '0x1c42576aca321a590a809cd8b18492aafc1f3909',
    'AirWILD1': '0x4d8165cb6861253e9edfbac2f41a386ba1a0a175',
    'AirWILD2': '0x35d2f3cdaf5e2dea9e6ae3553a4caacba860a395',
    'Wolves': '0x1a178cfd768f74b3308cbca9998c767f4e5b2cf8',
    'Wapes': '0x05F81F870cBca79E9171f22886b58b5597A603AA',
    'Gens':'0x90a1f4B78Fa4198BB620b7686f510FD476Ec7A0B',
    'zNS':'0xC14ea65f0a478C649B7a037bC0aD0a765b49196B'

}
os_count=0 

def os_get_pic():
    params={
    "X-API-KEY":os_api
    }
    ro=requests.get(f'https://api.opensea.io/api/v1/asset_contract/{contract_id}',headers=params)
    os_contract=ro.json()
    image=os_contract['nft']['image_url']

def get_link(url):
    """Return a link to an image"""
    
    if url.startswith("http"):

        if "/ipfs/" in url:
            index = url.index("/ipfs/")
            #image_url = "https://ipfs.io" + url[index:]
            image_url = "https://4everland.io" + url[index:]
        else:
            image_url = url
    elif url.startswith("ipfs://"):
        image_url = url.replace("ipfs://", "https://4everland.io/ipfs/")
        #image_url = url.replace("ipfs://", "https://ipfs.io/ipfs/")
    elif url.startswith("ar://"):
        image_url = url.replace("ar://", "https://arweave.net/")
    #st.write(image_url)
    return image_url

    

# Function declarations for each endpoint
def default_process(contract_address,token_id):
    
    st.write("Token id:",token_id)
    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{alch_api}/getNFTMetadata?contractAddress={contract_address}&tokenId={token_id}&refreshCache=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    rjson= response.json()
    image= rjson['raw']['metadata']['image']
    image1= get_link(image)
    video= rjson['raw']['metadata']['animation_url']
    video1= get_link(video)

    #st.write(rjson['raw']['metadata'])
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, width=300)

    with col2:
        st.dataframe(rjson['raw']['metadata']['attributes'],height=300)
    
    image_lnk= f'[Image]({image1})'
    st.markdown(image_lnk, unsafe_allow_html=True) 
    video_lnk= f'[Video]({video1})'
    st.markdown(video_lnk, unsafe_allow_html=True) 
    st.divider ()





def cribs(contract_address,token_id):

    st.write("Token id:",token_id)
    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{alch_api}/getNFTMetadata?contractAddress={contract_address}&tokenId={token_id}&refreshCache=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    rjson= response.json()
    image= rjson['raw']['metadata']['image']
    image1= get_link(image)
    image_2= rjson['raw']['metadata']['image2']
    image2= get_link(image_2)

    #st.write(rjson['raw']['metadata'])
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, width=300)

    with col2:
        st.dataframe(rjson['raw']['metadata']['attributes'],height=300)
    
    image_lnk= f'[Image]({image1})'
    st.markdown(image_lnk, unsafe_allow_html=True) 
    video_lnk= f'[Image2]({image2})'
    st.markdown(video_lnk, unsafe_allow_html=True) 

    st.divider ()



def airwild0(contract_address,token_id):

    st.write("Token id:",token_id)
    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{alch_api}/getNFTMetadata?contractAddress={contract_address}&tokenId={token_id}&refreshCache=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    rjson= response.json()
    image= rjson['raw']['metadata']['image']
    image1= get_link(image)
    video= rjson['raw']['metadata']['animation_url']
    video1= get_link(video)

    #st.write(rjson['raw']['metadata'])
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, width=300)

    with col2:
        st.write(rjson['raw']['metadata']['name'])
        image_lnk= f'[Image]({image1})'
        st.markdown(image_lnk, unsafe_allow_html=True) 
        video_lnk= f'[Video]({video1})'
        st.markdown(video_lnk, unsafe_allow_html=True) 

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(rjson['raw']['metadata']['attributes'],height=300, width=300)    
    
    with col2:
  

        model= rjson['raw']['metadata']['attributes'][1]['value']
            #Add Utility
        #{\"trait_type\":\"Hat\",\"value\":\"Horns\"},
        if model=="Coral":
            utility= {"Utility":"Sprint Speed", "value":"3: Hyperspeed"}, {"Utility":"Hops", "value":"3: Mega Hops"}, {"Utility":"Swim Speed", "value":"3:Micheal Phelps Level"}, {"Utility":"Climb Ability", "value":"3: Climb any mountain in Wiami"},{"Utility":"Zero Gravity", "value":"No"},{"Utility":"Walk on Water", "value":"Yes"}
        elif model=="Lightning":
            utility= {"Utility":"Sprint Speed", "value":"3: Hyperspeed"}, {"Utility":"Hops", "value":"2: High Jump"}, {"Utility":"Swim Speed", "value":"2: Normal Swim"}, {"Utility":"Climb Ability", "value":"2: Steep Climb Ability"}, {"Utility":"Zero Gravity", "value":"Yes"}, {"Utility":"Walk on Water", "value":"No"}
        elif model=="Element":
            utility= {"Utility":"Sprint Speed", "value":"2: Fast"}, {"Utility":"Hops", "value":"2: High Jump"}, {"Utility":"Swim Speed", "value":"3:Micheal Phelps Level"}, {"Utility":"Climb Ability", "value":"2: Steep Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif model=="Rice Krispy":
            utility= {"Utility":"Sprint Speed", "value":"1: Increased Speed"}, {"Utility":"Hops", "value":"3: Mega Hops"}, {"Utility":"Swim Speed", "value":"1: Slow Waddle"}, {"Utility":"Climb Ability", "value":"1:Increased Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif model=="Lines":
            utility= {"Utility":"Sprint Speed", "value":"3: Hyperspeed"}, {"Utility":"Hops", "value":"1: Increased Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"1:Increased Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif model=="Monster":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"3: Mega Hops"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"1:Increased Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif model=="Circle":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"3: Micheal Phelps Level"}, {"Utility":"Climb Ability", "value":"1: Increased Climb Ability"},{"Utility":"Zero Gravity","value":"No"},{"Utility":"Walk on Water","value":"No"}
        elif model=="Animal":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"1: Increased Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"2: Steep Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif model=="Wave":
            utility= {"Utility":"Sprint Speed", "value":"2: Fast"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"1:Increased Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif model=="Acid Drip":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"2: High Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"1:Increased Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        else:
            utility='None'
        st.dataframe(utility,height=300, width=300) 

    st.divider ()
def airwild1(contract_address,token_id):
   
    st.write("Token id:",token_id)
    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{alch_api}/getNFTMetadata?contractAddress={contract_address}&tokenId={token_id}&refreshCache=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    rjson= response.json()
    image= rjson['raw']['metadata']['image']
    image1= get_link(image)
    video= rjson['raw']['metadata']['animation_url']
    video1= get_link(video)

    #st.write(rjson['raw']['metadata'])
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, width=300)

    with col2:
        st.write(rjson['raw']['metadata']['name'])
        image_lnk= f'[Image]({image1})'
        st.markdown(image_lnk, unsafe_allow_html=True) 
        video_lnk= f'[Video]({video1})'
        st.markdown(video_lnk, unsafe_allow_html=True) 

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(rjson['raw']['metadata']['attributes'],height=300, width=300)    
    
    with col2:
  

        nft_model= rjson['raw']['metadata']['attributes'][1]['value']
            #Add Utility
        #{\"trait_type\":\"Hat\",\"value\":\"Horns\"},
        if nft_model=="Blockchain":
            utility= {"Utility":"Sprint Speed", "value":"3: Hyperspeed"}, {"Utility":"Hops", "value":"2: High Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"},{"Utility":"Zero Gravity", "value":"No"},{"Utility":"Walk on Water", "value":"Yes"}
        elif nft_model=="Frosties":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"3: Mega Hops"}, {"Utility":"Swim Speed", "value":"2: Normal Swim"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"Yes"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Instrument":
            utility= {"Utility":"Sprint Speed", "value":"2: Fast"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"3: Climb any mountain in Wiami"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Metashroom":
            utility= {"Utility":"Sprint Speed", "value":"1: Increased Speed"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"3: Michael Phelps Level"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Liquid":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"2: Normal Swim"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Mandala":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"2: High Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Momentum":
            utility= {"Utility":"Sprint Speed", "value":"2: Fast"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"},{"Utility":"Zero Gravity","value":"No"},{"Utility":"Walk on Water","value":"No"}
        elif nft_model=="Ribbon":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"1: Increased Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Fear":
            utility= {"Utility":"Sprint Speed", "value":"1: Increased Speed"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Zero":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"1: Increased Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        else:
            utility={"None":"None", "None":"None"}


        st.dataframe(utility,height=300, width=300) 

    st.divider ()


def airwild2(contract_address,token_id):
  
    st.write("Token id:",token_id)
    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{alch_api}/getNFTMetadata?contractAddress={contract_address}&tokenId={token_id}&refreshCache=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    rjson= response.json()
    image= rjson['raw']['metadata']['image']
    image1= get_link(image)
    video= rjson['raw']['metadata']['animation_url']
    video1= get_link(video)

    
    #st.write(rjson['raw']['metadata'])
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, width=300)

    with col2:
        st.write(rjson['raw']['metadata']['name'])
        image_lnk= f'[Image]({image1})'
        st.markdown(image_lnk, unsafe_allow_html=True) 
        video_lnk= f'[Video]({video1})'
        st.markdown(video_lnk, unsafe_allow_html=True) 

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(rjson['raw']['metadata']['attributes'],height=300, width=300)    
    
    with col2:
  

        nft_model= rjson['raw']['metadata']['attributes'][0]['value']
            #Add Utility
        #{\"trait_type\":\"Hat\",\"value\":\"Horns\"},
        if nft_model=="Compression":
            utility= {"Utility":"Sprint Speed", "value":"3: Hyperspeed"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"2:Steep Clib Ability"},{"Utility":"Zero Gravity", "value":"No"},{"Utility":"Walk on Water", "value":"Yes"}
        elif nft_model=="Interference":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"3: Mega Hops"}, {"Utility":"Swim Speed", "value":"2: Normal Swim"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"Yes"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Scatter":
            utility= {"Utility":"Sprint Speed", "value":"2: Fast"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"3: Climb any mountain in Wiami"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Velocity":
            utility= {"Utility":"Sprint Speed", "value":"3: Hyperspeed"}, {"Utility":"Hops", "value":"1:Increased Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Convergence":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"2:High Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Radiation":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"2:Normal Swim"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Transmission":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"2:Steep Climb Ability"},{"Utility":"Zero Gravity","value":"No"},{"Utility":"Walk on Water","value":"No"}
        elif nft_model=="Range":
            utility= {"Utility":"Sprint Speed", "value":"1:Increased Speed"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Pulse":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"1:Increased Jump"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Wavelength":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"1:Slow Waddle"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Amplitude":
            utility= {"Utility":"Sprint Speed", "value":"None"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"1:Increased Climb Ability"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        elif nft_model=="Frequency":
            utility= {"Utility":"Sprint Speed", "value":"1:Increased Speed"}, {"Utility":"Hops", "value":"None"}, {"Utility":"Swim Speed", "value":"None"}, {"Utility":"Climb Ability", "value":"None"}, {"Utility":"Zero Gravity", "value":"No"}, {"Utility":"Walk on Water", "value":"No"}
        else:
            utility={"None":"None", "None":"None"}


        st.dataframe(utility,height=300, width=300) 

    st.divider ()

def gens(contract_address,token_id):
  
    st.write("Token id:",token_id)
    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{alch_api}/getNFTMetadata?contractAddress={contract_address}&tokenId={token_id}&refreshCache=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    rjson= response.json()
    image= rjson['raw']['metadata']['image']
    image1= get_link(image)
    image_2= rjson['raw']['metadata']['image_2']
    image2= get_link(image_2)
    image_3= rjson['raw']['metadata']['image_3']
    image3= get_link(image_3)
    video= rjson['raw']['metadata']['animation_url']
    video1= get_link(video)
    #st.write(rjson['raw']['metadata'])
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, width=300)

    with col2:
        st.dataframe(rjson['raw']['metadata']['attributes'],height=300)
    
    image_lnk1= f'[Image]({image1})'
    st.markdown(image_lnk1, unsafe_allow_html=True) 
    image_lnk2= f'[Image2]({image2})'
    st.markdown(image_lnk2, unsafe_allow_html=True) 
    image_lnk3= f'[Image3]({image3})'
    st.markdown(image_lnk3, unsafe_allow_html=True)
    video_lnk= f'[Video]({video1})'
    st.markdown(video_lnk, unsafe_allow_html=True) 
    st.divider ()

def zns(contract_address,token_id):
 
    st.write("Token id:",token_id)
    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{alch_api}/getNFTMetadata?contractAddress={contract_address}&tokenId={token_id}&refreshCache=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    rjson= response.json()
    image= rjson['raw']['metadata']['image']
    image1= get_link(image)
    image2= rjson['raw']['metadata']['image_full']
    image2= get_link(image2)
    image3= rjson['raw']['metadata']['original']
    image3= get_link(image3)

    #st.write(rjson['raw']['metadata'])
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, width=300)

    with col2:
        st.dataframe(rjson['raw']['metadata']['attributes'],height=300)
    
    image_lnk1= f'[Image]({image1})'
    st.markdown(image_lnk1, unsafe_allow_html=True) 
    image_lnk2= f'[Image2]({image2})'
    st.markdown(image_lnk2, unsafe_allow_html=True) 
    image_lnk3= f'[Image3]({image3})'
    st.markdown(image_lnk3, unsafe_allow_html=True)

    st.divider ()

# Streamlit app layout

st.title("SMA11'S WilderWorld BLACK BOOK interm service")
im= Image.open('ww_banner.png')
st.image(im)

# Replacing selectbox with wallet address input
wallet_address = st.sidebar.text_input("Enter Wallet Address")

def get_nfts_from_wallet(wallet_address):
    st.write("Wallet:",wallet_address)
    if wallet_address:
        api_key = mor_api
        params = {
            "address": wallet_address,
            "chain": "eth",
            "format": "decimal",
            "limit": 100,
            "token_addresses": [],
            "cursor": "",
            "normalizeMetadata": True,
        }

        result = []
        is_more_data = True

        while True:
            
            response = evm_api.nft.get_wallet_nfts(
                api_key=api_key,
                params=params,
            )
            result.extend(response['result'])
            

            # Check if there is a 'cursor' value for next page
            if 'cursor' in response and response['cursor']:
                params['cursor'] = response['cursor']
            else:
                break

   
        return result
    return []

# Checking NFTs in the wallet
nfts = get_nfts_from_wallet(wallet_address)
count=0
#st.write(nfts)
for nft in nfts:
    #st.write(contract_addresses.get('Crafts').lower())
    #st.write(count)
    nft_name= nfts[count]['name']
    #st.write(nft_name)
    contract_address = nft.get('token_address', '')
    #st.write(contract_address)
    token_id = nft.get('token_id', '')
    #st.write(token_id)
    # Check if the contract address matches any of the endpoints
    if contract_address == contract_addresses.get('Wheels') or contract_address == contract_addresses.get('Wheels').lower():
        st.write('Wheel')
        default_process(contract_address,token_id)
    elif contract_address == contract_addresses.get('Cribs') or contract_address == contract_addresses.get('Cribs').lower():
        st.write('Crib')
        cribs(contract_address,token_id)
    elif contract_address == contract_addresses.get('Crafts') or contract_address == contract_addresses.get('Crafts').lower():
        st.write('Craft')
        default_process(contract_address,token_id)
    elif contract_address == contract_addresses.get('Motos') or contract_address == contract_addresses.get('Motos').lower():
        st.write('Moto')
        default_process(contract_address,token_id)
    elif contract_address == contract_addresses.get('AirWILD0') or contract_address == contract_addresses.get('AirWILD0').lower():
        st.write('AirWILD0')
        airwild0(contract_address,token_id)
    elif contract_address == contract_addresses.get('AirWILD1') or contract_address == contract_addresses.get('AirWILD1').lower():
        st.write('AirWILD1')
        airwild1(contract_address,token_id)
    elif contract_address == contract_addresses.get('AirWILD2') or contract_address == contract_addresses.get('AirWILD2').lower():
        st.write('AirWILD2')
        airwild2(contract_address,token_id)
    elif contract_address == contract_addresses.get('Wolves') or contract_address == contract_addresses.get('Wolves').lower():
        st.write('Wolves')
        default_process(contract_address,token_id)
    elif contract_address == contract_addresses.get('Wapes') or contract_address == contract_addresses.get('Wapes').lower():
        st.write('Wapes')
        default_process(contract_address,token_id)
    elif contract_address == contract_addresses.get('zNS') or contract_address == contract_addresses.get('zNS').lower():
        st.write('zNS')
        zns(contract_address,token_id)
    elif contract_address == contract_addresses.get('Gens') or contract_address == contract_addresses.get('Gens').lower():
        st.write('GENS')
        gens(contract_address,token_id)
    #elif contract_address == contract_addresses.get('zNS'):
     #   zns(token_id)
    count+=1


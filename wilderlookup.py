# Writen for use with streamlit.io
import streamlit as st
import requests, json 
import pandas as pd
from PIL import Image

endpoint= st.sidebar.selectbox("Endpoints", ['Wheels/Crafts','Kicks S0','Missing', 'Fix'])
st.title(f"SMA11'S WHEELS BLACK BOOK - {endpoint}") 

# Get Opensea api
collection_slug="wilderworld"
asset_contract_address="0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D"
params={
    "X-API-KEY":st.secrets["os_api"]
}
r = requests.get(f"https://api.opensea.io/api/v1/asset_contract/{asset_contract_address}",headers=params)

response = r.json()
st.header (response["collection"]["name"]) 




   
#SIDEBAR -One day stats for collection on OpenSea- not accurate because opensea has all wilder collections mixed together
#r = requests.get(f"https://api.opensea.io/api/v1/collection/{collection_slug}/stats",params=params)
#response = r.json()
# st.sidebar.write("Floor Price: ", response["stats"]["floor_price"])
# st.sidebar.write("One day sales: ", response["stats"]["one_day_sales"])
# st.sidebar.write("One day avg price (Eth): ", response["stats"]["one_day_average_price"])
# st.sidebar.write("One day volume (Eth): ", response["stats"]["one_day_volume"])
# st.sidebar.write("Total NFT's: ", response["stats"]["total_supply"])
# st.sidebar.write("Number of Owners: ", response["stats"]["num_owners"])
# st.slider("Select how many days", 1, 100, 100)




if endpoint == 'Wheels/Crafts':
    st.image (response["collection"]["banner_image_url"])
    link = '[Contract](https://etherscan.io/address/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d)'
    st.markdown(link, unsafe_allow_html=True)
    st.sidebar.subheader("Filters")
    token = st.sidebar.text_input("Token ID")

    if not token:
        st.error("ENTER TOKEN ID ON LEFT")

    
    else:
        
        params={}
        params['limit']=50
        api_key= st.secrets["cov_api"]  # Get your own api key here: https://www.covalenthq.com/platform/#/apikey/
        r=requests.get(f'https://api.covalenthq.com/v1/1/tokens/0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D/nft_metadata/{token}/?quote-currency=USD&format=JSON&key={api_key}')
        token_content=r.json()


        # Write token content
        st.write(token_content['data']['items'][0]['nft_data'][0]['external_data']['name'])
        st.image(token_content['data']['items'][0]['nft_data'][0]['external_data']['image_512'])
        image256 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_256']
        image512 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_512']
        image1024 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_1024']
        animation1 = token_content['data']['items'][0]['nft_data'][0]['external_data']['animation_url']      
        opensea= 'https://opensea.io/assets/'+ token_content['data']['items'][0]['contract_address']+ "/" + token_content['data']['items'][0]['nft_data'][0]['token_id']
        st.write('Token ID:')
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

        df=token_content['data']['items'][0]['nft_data'][0]['external_data']['attributes']
        st.dataframe(df)


elif endpoint == 'Kicks S0':
    im= Image.open('AirWild.png')
    st.image(im)
    link = '[Contract](https://etherscan.io/address/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d)'
    st.markdown(link, unsafe_allow_html=True)
    st.sidebar.subheader("Filters")
    token = st.sidebar.text_input("Token ID")

    if not token:
        st.error("ENTER TOKEN ID ON LEFT")

    
    else:
         #Get Metadata and parse
        params={

            'x-api-key':st.secrets["mor_api"]
        }
        Mr=requests.get(f'https://deep-index.moralis.io/api/v2/nft/0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D/{token}/?chain=eth&format=decimal', headers=params)
        Mtoken_content=Mr.json()
        kicksdictionary = json.loads(Mtoken_content['metadata'])
        descriptions = kicksdictionary["description"]
        attributes = descriptions.split(" - ")[1]
        attributessplit = attributes.strip().split("//")
        attributesnew = []
        for keys in attributessplit:
            attributesnew += keys.split(":")

        #Add to kicksdictionary, under attributes
      #  attributessub = {attributesnew[0].strip(): attributesnew[1].strip(),attributesnew[2].strip(): attributesnew[3].strip(), attributesnew[4].strip(): attributesnew[5].strip(), attributesnew[6].strip(): attributesnew[7].strip(), attributesnew[8].strip(): attributesnew[9].strip()}
        attributessub = {"trait":attributesnew[0].strip(), "value":attributesnew[1].strip()}, {"trait":attributesnew[2].strip(), "value":attributesnew[3].strip()}, {"trait":attributesnew[4].strip(), "value":attributesnew[5].strip()}, {"trait":attributesnew[6].strip(), "value":attributesnew[7].strip()}, {"trait":attributesnew[8].strip(), "value":attributesnew[9].strip()}
        kicksdictionary["Attributes"] = attributessub
         

        #Add Utility
        #{\"trait_type\":\"Hat\",\"value\":\"Horns\"},
        if attributessub[0]['value']=="Coral":
            utility= {"trait":"Sprint Speed", "value":"3: Hyperspeed"}, {"trait":"Hops", "value":"3: Mega Hops"}, {"trait":"Swim Speed", "value":"3:Micheal Phelps Level"}, {"trait":"Climb Ability", "value":"3: Climb any mountain in Wiami"},{"trait":"Zero Gravity", "value":"N"},{"trait":"Walk on Water", "value":"Y"}
        elif attributessub[0]['value']=="Lightning":
            utility= {"trait":"Sprint Speed", "value":"3: Hyperspeed"}, {"trait":"Hops", "value":"2: High Jump"}, {"trait":"Swim Speed", "value":"2: Normal Swim"}, {"trait":"Climb Ability", "value":"2: Steep Climb Ability"}, {"trait":"Zero Gravity", "value":"Y"}, {"trait":"Walk on Water", "value":"N"}
        elif attributessub[0]['value']=="Element":
            utility= {"trait":"Sprint Speed", "value":"2: Fast"}, {"trait":"Hops", "value":"2: High Jump"}, {"trait":"Swim Speed", "value":"3:Micheal Phelps Level"}, {"trait":"Climb Ability", "value":"2: Steep Climb Ability"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif attributessub[0]['value']=="Rice Krispy":
            utility= {"trait":"Sprint Speed", "value":"1: Increased Speed"}, {"trait":"Hops", "value":"3: Mega Hops"}, {"trait":"Swim Speed", "value":"1: Slow Waddle"}, {"trait":"Climb Ability", "value":"1:Increased Climb Ability"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif attributessub[0]['value']=="Lines":
            utility= {"trait":"Sprint Speed", "value":"3: Hyperspeed"}, {"trait":"Hops", "value":"1: Increased Jump"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"1:Increased Climb Ability"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif attributessub[0]['value']=="Monster":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"3: Mega Hops"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"1:Increased Climb Ability"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif attributessub[0]['value']=="Circle":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"None"}, {"trait":"Swim Speed", "value":"3: Micheal Phelps Level"}, {"trait":"Climb Ability", "value":"1: Increased Climb Ability"},{"trait":"Zero Gravity","value":"N"},{"trait":"Walk on Water","value":"N"}
        elif attributessub[0]['value']=="Animal":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"1: Increased Jump"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"2: Steep Climb Ability"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif attributessub[0]['value']=="Wave":
            utility= {"trait":"Sprint Speed", "value":"2: Fast"}, {"trait":"Hops", "value":"None"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"1:Increased Climb Ability"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif attributessub[0]['value']=="Acid Drip":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"2: High Jump"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"1:Increased Climb Ability"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        else:
            utility='None'

        #Get info covalent
        params={}
        params['limit']=50
        api_key='ckey_fa91923a9dc34181ac2bbbdc82e'  # Get your api key here: https://www.covalenthq.com/platform/#/apikey/
        r=requests.get(f'https://api.covalenthq.com/v1/1/tokens/0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D/nft_metadata/{token}/?quote-currency=USD&format=JSON&key={api_key}')
        token_content=r.json()
        #st.write(token_content)

        # Write token content
        #st.write(token_content['data']['items'][0]['nft_data'][0]['external_data']['name'])
        #st.image(token_content['data']['items'][0]['nft_data'][0]['external_data']['image_512'])
        description = token_content['data']['items'][0]['nft_data'][0]['external_data']['description']
        image256 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_256']
        image512 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_512']
        image1024 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image_1024']
        animation1 = token_content['data']['items'][0]['nft_data'][0]['external_data']['image']      
        opensea= 'https://opensea.io/assets/'+ token_content['data']['items'][0]['contract_address']+ "/" + token_content['data']['items'][0]['nft_data'][0]['token_id']

        
        res=animation1.strip('https://ipfs.fleek.co/ipfs/')
        
        animation= "https://ipfs.io/ipfs/"+ res
        st.video(animation)
        st.header(kicksdictionary['title'])  
        st.write('Token ID:')
        st.write(token_content['data']['items'][0]['nft_data'][0]['token_id'])
        opensea_link= f'[OpenSea] ({opensea})'
        st.markdown(opensea_link, unsafe_allow_html=True)
 
        st.write(description)
        #link_256 = f'[Image 256] ({image256})'
        #link_512 = f'[Image 512]({image512})'
        #link_1024 = f'[Image 1024]({image1024})' 
        link_animation = f'[Video]({animation})' 
        #st.markdown(link_256, unsafe_allow_html=True)
        #st.markdown(link_512, unsafe_allow_html=True)
        #st.markdown(link_1024, unsafe_allow_html=True)
        st.markdown(link_animation, unsafe_allow_html=True)

        st.write ('ATTRIBUTES')
        st.dataframe(kicksdictionary["Attributes"])
        
        st.write("UTILITY")
        #df=kicksdictionary['Attributes']
        df=utility
        st.dataframe(df)


elif endpoint == 'Missing':
# run cli.py, nft.py to create missing.json
    st.sidebar.subheader("Recent Wheels with Metadata Refreshed") 
    st.image (response["collection"]["banner_image_url"])
    file= "missing.json"
    r= open(file,'r')
    data= r.read()
    response = json.loads(data)
    counter= 0
    while response:
            counter=counter+1
            st.write(counter)
            token = response['missing_data'][counter]['token_id']
            st.write(response['missing_data'][counter]['token_id'])
                       
            st.write (response['missing_data'][counter]['name'])
            #st.image(token_content['data']['items'][0]['nft_data'][0]['external_data']['image_256'])
            osea=response['missing_data'][counter]['opensea']
            opensea_link= f'[OpenSea] ({osea})'
            st.markdown(opensea_link, unsafe_allow_html=True)

elif endpoint == 'Fix':
# run cli.py, nft.py to create missing.json
    st.image (response["collection"]["banner_image_url"])
    st.sidebar.subheader("Opensea 'image' var not loading") 
    st.sidebar.subheader ('"Image" var picture is used in searches/filters.  eg. search for the token id')
    file= "fix.json"
    r= open(file,'r')
    data= r.read()
    response = json.loads(data)
    counter= 0
    while response:
            counter=counter+1
            st.write(counter)
            token = response['missing_data'][counter]['token_id']
        

            st.write(response['missing_data'][counter]['token_id'])
                       
            st.write (response['missing_data'][counter]['name'])
            #st.image(token_content['data']['items'][0]['nft_data'][0]['external_data']['image_256'])
            osea=response['missing_data'][counter]['opensea']
            opensea_link= f'[OpenSea] ({osea})'
            st.markdown(opensea_link, unsafe_allow_html=True)

                

          
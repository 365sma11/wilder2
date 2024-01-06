# Writen for use with streamlit.io
import streamlit as st
import requests, json
import pandas as pd
from PIL import Image
from requests.structures import CaseInsensitiveDict
import csv

#os_api= st.secrets["os_api"]
#cov_api= st.secrets["cov_api"]
#mor_api= st.secrets["mor_api"]
cov_api= 'ckey_fa91923a9dc34181ac2bbbdc82e'



endpoint= st.sidebar.selectbox("Endpoints", ['Motos', 'Craft Rarity','Wheels/Crafts','Kicks S0', 'Kicks S01', "Beast's", 'Wallet NFTs Value'])
st.title(f"SMA11'S WilderWorld BLACK BOOK - {endpoint}")

# Get Opensea api
collection_slug="wilderworld"
asset_contract_address="0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D"






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
    im= Image.open('wheels_banner.png')
    st.image(im)
    st.header("Download your Media files")
    link = '[Contract](https://etherscan.io/address/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d)'
    st.markdown(link, unsafe_allow_html=True)
    st.sidebar.subheader("Filters")
    token = st.sidebar.text_input("Token ID")

    if not token:
        st.write("In the URL to the opensea address of your token")
        st.write("example: https://opensea.io/assets/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d/44792931070073871902445706811038693742219397549916803539307329545058277134934")
        st.write("Copy the part after the last slash in the address (this is your token_id)")
        st.write("example: 44792931070073871902445706811038693742219397549916803539307329545058277134934")
        st.error("ENTER TOKEN ID ON LEFT")


    else:

        params={}
        params['limit']=50
        api_key= cov_api  # Get your own api key here: https://www.covalenthq.com/platform/#/apikey/
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

elif endpoint == "Craft Rarity":
    im= Image.open('Wolf.png')
    st.image(im)
    st.sidebar.subheader("Filters")
    environment = st.sidebar.text_input("Environment Multiplier")
    front_component = st.sidebar.text_input("Front Component Multiplier")
    front_kit = st.sidebar.text_input("Front Kit Multiplier")
    industry = st.sidebar.text_input("Industry Multiplier")
    mirror = st.sidebar.text_input("Mirror Multiplier")
    number_plate = st.sidebar.text_input("Number Plate Multiplier")
    pattern = st.sidebar.text_input("Pattern Multiplier")
    primary_color = st.sidebar.text_input("Primary Color Multiplier")
    rear_component = st.sidebar.text_input("Rear Component Multiplier")
    rear_kit = st.sidebar.text_input("Rear Kit Multiplier")
    scoop = st.sidebar.text_input("Scoop Multiplier")
    splitter = st.sidebar.text_input("Splitter Multiplier")
    spoiler = st.sidebar.text_input("Spoiler Multiplier")
    craft_name = st.sidebar.text_input("Name Multiplier")
    rarity_option= st.sidebar.selectbox("Rarity Option", ['Traditional','Open Rarity'])
    
    if st.sidebar.button('Calculate'):
        api_key= cov_api  
        r=requests.get(f'https://api.covalenthq.com/v1/1/tokens/0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D/nft_token_ids/?quote-currency=USD&format=JSON&key={api_key}')
        token_content=r.json() 



elif endpoint == "Beast's":
    im= Image.open('Wolf.png')
    st.sidebar.subheader("Filters")
    token_id = st.sidebar.text_input("Token ID")

    if not token_id:
        st.write("In the URL to the opensea address of your token")
        st.write("example: https://opensea.io/assets/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d/44792931070073871902445706811038693742219397549916803539307329545058277134934")
        st.write("Copy the part after the last slash in the address (this is your token_id)")
        st.write("example: 44792931070073871902445706811038693742219397549916803539307329545058277134934")
        st.error("ENTER TOKEN ID ON LEFT")


    else:

        #get token list

        #Find token id
        api_key= cov_api  # Get your own api key here: https://www.covalenthq.com/platform/#/apikey/
        r=requests.get(f'https://api.covalenthq.com/v1/1/tokens/0x1A178CFD768F74b3308cbca9998C767F4E5B2CF8/nft_metadata/{token_id}/?quote-currency=USD&format=JSON&key={api_key}')
        token_content=r.json()

        
        #get token data
        params={}
        params['limit']=50
        api_key= cov_api  # Get your own api key here: https://www.covalenthq.com/platform/#/apikey/
        r=requests.get(f'https://api.covalenthq.com/v1/1/tokens/0x1A178CFD768F74b3308cbca9998C767F4E5B2CF8/nft_metadata/{token_id}/?quote-currency=USD&format=JSON&key={api_key}')
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


# elif endpoint == 'Beast Whitelist':
#     im= Image.open('Wolf.png')
#     st.image(im)
#     st.sidebar.subheader("Filters")
#     wallet = st.sidebar.text_input("Wallet")

#     if not wallet:
#         st.error("ENTER WALLET ID ON LEFT")


#     else:
#         st.write("Checking your for your Wallet ...")
#         with open ('pets_mintlist.csv', mode='r') as csv_file:
#             csv_reader= csv.DictReader(csv_file)
#             line_count=0
#             found=0
#             for row in csv_reader:
#                 if row['wallet']==wallet:
#                     found=1
#                     break

#             if found==1:
#                 st.write(f"You are on the Whitelist! You get to mint {row['mint']} Beasts")
#             else:
#                 st.write("You are not on the Whitelsit")





elif endpoint == 'Kicks S0':
    im= Image.open('AirWild.png')
    st.header("Download your Media files and see your utility")
    st.image(im)
    link = '[Contract](https://etherscan.io/address/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d)'
    st.markdown(link, unsafe_allow_html=True)
    st.sidebar.subheader("Filters")
    token = st.sidebar.text_input("Token ID")
    #st.write({ "name": "OG Lightning", "description": "Offering the ability to turn night into day, if only for a moment. A true force which embodies the electricity held within a bolt of lightning.", "animation_url": "ipfs://QmYWpURqLoCwrSJ7Wn5WNd8vkCEMaAkjCZP6miofAJFPhH", "image": "ipfs://QmR6w7qZS8Jmh55HxBar8UeKuEafwRnhjP4MppU8tViqs6", "stakingrequests": "disabled", "attributes": [ { "trait_type": "Industry", "value": "Wilder.Kicks" }, { "trait_type": "Base Model", "value": "Lightning" }, { "trait_type": "Primary Material", "value": "Recycled Polymer" }, { "trait_type": "Primary Color", "value": "Black" }, { "trait_type": "Secondary Material", "value": "Metallic" }, { "trait_type": "Secondary Color", "value": "Purple" } ] })

    if not token:
        st.write("In the URL to the opensea address of your token")
        st.write("example: https://opensea.io/assets/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d/44792931070073871902445706811038693742219397549916803539307329545058277134934")
        st.write("Copy the part after the last slash in the address (this is your token_id)")
        st.write("example: 44792931070073871902445706811038693742219397549916803539307329545058277134934")

        st.error("ENTER TOKEN ID ON LEFT")


    else:
         #Get Metadata and parse

        params={

            'x-api-key':mor_api
        }
        Mr=requests.get(f'https://deep-index.moralis.io/api/v2/nft/0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D/{token}/?chain=eth&format=decimal', headers=params)
        Mtoken_content=Mr.json()
        st.write(Mtoken_content)
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
        api_key= cov_api  # Get your api key here: https://www.covalenthq.com/platform/#/apikey/
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

elif endpoint == 'Kicks S01':
    im= Image.open('AirWild.png')
    st.header("Download your Media files and see your utility")
    st.image(im)
    link = '[Contract](https://etherscan.io/address/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d)'
    st.markdown(link, unsafe_allow_html=True)
    st.sidebar.subheader("Filters")
    token = st.sidebar.text_input("Token ID")

    if not token:
        st.write("In the URL to the opensea address of your token")
        st.write("example: https://opensea.io/assets/0xc2e9678a71e50e5aed036e00e9c5caeb1ac5987d/44792931070073871902445706811038693742219397549916803539307329545058277134934")
        st.write("Copy the part after the last slash in the address (this is your token_id)")
        st.write("example: 44792931070073871902445706811038693742219397549916803539307329545058277134934")

        st.error("ENTER TOKEN ID ON LEFT")


    else:

        #Get info covalent
        params={}
        params['limit']=50
        api_key=cov_api  # Get your api key here: https://www.covalenthq.com/platform/#/apikey/
        r=requests.get(f'https://api.covalenthq.com/v1/1/tokens/0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D/nft_metadata/{token}/?quote-currency=USD&format=JSON&key={api_key}')
        token_content=r.json()
        nft_data=token_content['data']['items'][0]['nft_data'][0]
        nft_data_external=token_content['data']['items'][0]['nft_data'][0]['external_data']
        nft_model=nft_data_external['attributes'][1]['value']



        #Add Utility

        if nft_model=="BLOCKCHAIN":
            utility= {"trait":"Sprint Speed", "value":"3: Hyperspeed"}, {"trait":"Hops", "value":"2: High Jump"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"None"},{"trait":"Zero Gravity", "value":"N"},{"trait":"Walk on Water", "value":"Y"}
        elif nft_model=="FROSTIES":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"3: Mega Hops"}, {"trait":"Swim Speed", "value":"2: Normal Swim"}, {"trait":"Climb Ability", "value":"None"}, {"trait":"Zero Gravity", "value":"Y"}, {"trait":"Walk on Water", "value":"N"}
        elif nft_model=="INSTRUMENT":
            utility= {"trait":"Sprint Speed", "value":"2: Fast"}, {"trait":"Hops", "value":"None"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"3: Climb any mountain in Wiami"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif nft_model=="METASHROOM":
            utility= {"trait":"Sprint Speed", "value":"1: Increased Speed"}, {"trait":"Hops", "value":"None"}, {"trait":"Swim Speed", "value":"3: Michael Phelps Level"}, {"trait":"Climb Ability", "value":"None"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif nft_model=="LIQUID":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"None"}, {"trait":"Swim Speed", "value":"2: Normal Swim"}, {"trait":"Climb Ability", "value":"None"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif nft_model=="MANDALA":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"2: High Jump"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"None"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif nft_model=="MOMENTUM":
            utility= {"trait":"Sprint Speed", "value":"2: Fast"}, {"trait":"Hops", "value":"None"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"None"},{"trait":"Zero Gravity","value":"N"},{"trait":"Walk on Water","value":"N"}
        elif nft_model=="RIBBON":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"None"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"1: Increased Climb Ability"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif nft_model=="FEAR":
            utility= {"trait":"Sprint Speed", "value":"1: Increased Speed"}, {"trait":"Hops", "value":"None"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"None"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        elif nft_model=="ZERO":
            utility= {"trait":"Sprint Speed", "value":"None"}, {"trait":"Hops", "value":"1: Increased Jump"}, {"trait":"Swim Speed", "value":"None"}, {"trait":"Climb Ability", "value":"None"}, {"trait":"Zero Gravity", "value":"N"}, {"trait":"Walk on Water", "value":"N"}
        else:
            utility={"None":"None", "None":"None"}



        # Write token content
        #st.write(token_content['data']['items'][0]['nft_data'][0]['external_data']['name'])
        #st.image(token_content['data']['items'][0]['nft_data'][0]['external_data']['image_512'])
        description = nft_data_external['description']
        image256 = nft_data_external['image_256']
        image512 = nft_data_external['image_512']
        image1024 = nft_data_external['image_1024']
        animation1 = nft_data_external['animation_url']
        opensea= 'https://opensea.io/assets/'+ token_content['data']['items'][0]['contract_address']+ "/" + token_content['data']['items'][0]['nft_data'][0]['token_id']


        res=animation1.strip('ipfs://')

        animation= "https://ipfs.io/ipfs/"+ res
        st.video(animation)
        st.header(nft_data_external['name'])
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
        st.dataframe(nft_data_external['attributes'])

        st.write("UTILITY")
        #df=kicksdictionary['Attributes']
        df=utility
        st.dataframe(df)


# elif endpoint == 'Missing':
# # run cli.py, nft.py to create missing.json
#     st.sidebar.subheader("Recent Wheels with Metadata Refreshed")
#     im= Image.open('wheels_banner.png')
#     st.image(im)
#     file= "missing.json"
#     r= open(file,'r')
#     data= r.read()
#     response = json.loads(data)
#     counter= 0
#     while response:
#             counter=counter+1
#             st.write(counter)
#             token = response['missing_data'][counter]['token_id']
#             st.write(response['missing_data'][counter]['token_id'])

#             st.write (response['missing_data'][counter]['name'])
#             #st.image(token_content['data']['items'][0]['nft_data'][0]['external_data']['image_256'])
#             osea=response['missing_data'][counter]['opensea']
#             opensea_link= f'[OpenSea] ({osea})'
#             st.markdown(opensea_link, unsafe_allow_html=True)

elif endpoint == 'Wallet NFTs Value':

    st.sidebar.subheader("Wallet NFT's")
    wallet = st.sidebar.text_input("Wallet")

    if not wallet:
        st.error("ENTER WALLET ON LEFT")

    else:

        # params={}
        # params['limit']=50
        headers = {
            "accept":"application/json",
            "x-api-key": cov_api

        }
        url=f"https://api.covalenthq.com/v1/eth-mainnet/address/{wallet}/balances_nft"
        st.write(headers)
        r=requests.get(url, headers=headers)
        #st.write('get')
        #r=requests.get(f'https://api.covalenthq.com/v1/eth-mainnet/address/{wallet}/balances_nft/?quote-currency=USD&format=JSON&nft=true&no-nft-fetch=false&key={api_key}')
        st.write(r.text)
        token_content=r.json()
        counter=0
        st.write(token_content)
        wallet_value=0
        st.write(len(token_content['data']['items']))
        st.write('fetched')

        while token_content:


            if counter <= (len(token_content['data']['items']))-1:

                if token_content['data']['items'][counter]['nft_data']:
                    st.write(counter)

                    # while token_content['data']['items'][counter]['nft_data']:
                    for i in range(len(token_content['data']['items'][counter]['nft_data'])):
                        token_id=token_content['data']['items'][counter]['nft_data'][i]['token_id']
                        contract_id=token_content['data']['items'][counter]['contract_address']
                        token_name=token_content['data']['items'][counter]['nft_data'][i]['external_data']['name']
                        im=token_content['data']['items'][counter]['nft_data'][i]['external_data']['image_256']
                        #st.write(im)

                        if im != None:

                            st.image(im)


                            # Get Floor Price
                            params={
                            "X-API-KEY":os_api
                            }
                            ro=requests.get(f'https://api.opensea.io/api/v1/asset_contract/{contract_id}',headers=params)
                            os_contract=ro.json()
                            collection_slug=os_contract['collection']['slug']
                            ro=requests.get(f'https://api.opensea.io/api/v1/collection/{collection_slug}/stats',headers=params)
                            os_contract_stats=ro.json()
                            st.write(os_contract_stats)
                            floor=os_contract_stats['stats']['floor_price']
                            st.write(token_name)
                            st.write(f'Current Floor price {floor} Eth')
                            st.write(f'Token id: {token_id}')
                            st.write(f'Contract: {contract_id}')

                            if floor!= None:
                                wallet_value+= floor

                    counter+=1

                else:
                    counter=counter+1
            else:
                break
        st.header(f'Your Total Nft values based on current floor prices is: {wallet_value} Eth')
# elif endpoint == 'Fix':
# # run cli.py, nft.py to create missing.json
#     im= Image.open('wheels_banner.png')
#     st.image(im)
#     st.sidebar.subheader("Opensea 'image' var not loading")
#     st.sidebar.subheader ('"Image" var picture is used in searches/filters.  eg. search for the token id')
#     file= "fix.json"
#     r= open(file,'r')
#     data= r.read()
#     response = json.loads(data)
#     counter= 0
#     while response:
#             counter=counter+1
#             st.write(counter)
#             token = response['missing_data'][counter]['token_id']


#             st.write(response['missing_data'][counter]['token_id'])

#             st.write (response['missing_data'][counter]['name'])
#             #st.image(token_content['data']['items'][0]['nft_data'][0]['external_data']['image_256'])
#             osea=response['missing_data'][counter]['opensea']
#             opensea_link= f'[OpenSea] ({osea})'
#             st.markdown(opensea_link, unsafe_allow_html=True)




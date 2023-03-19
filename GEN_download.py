import requests
import streamlit as st
from PIL import Image

#api_alchemy= st.secrets["api_alchemy"]


st.title(f"SMA11'S WilderWorld BLACK BOOK")
im= Image.open('WWbanner.png')
st.image(im)
st.header("Download your Media files")
wallet = st.sidebar.text_input("Wallet")
project = st.sidebar.selectbox(
    "Project",
    [
        "GENs",
        "Wapes",
        "Motos",
        "Wolves",
        "AirWild 02",
        "Wheels, AirWild Season 0 & Season 1, Cribs, & Crafts",
        
    ],
)

def get_data_by_contract(contracts,wallet):
    page_key = None
    total_count = 0
    token_count=1
    url = (
            f"https://eth-mainnet.g.alchemy.com/nft/v2/{api_alchemy}/getNFTs?owner={wallet}&{contracts}&withMetadata=true&pageSize=100"
        )
    headers = {"accept": "application/json"}
    r = requests.get(url, headers=headers)
    tokens = r.json()
    st.write('Count=',tokens['totalCount'])
    st.markdown("""---""")
    while True:
        url = (
            f"https://eth-mainnet.g.alchemy.com/nft/v2/{api_alchemy}/getNFTs?owner={wallet}&{contracts}&withMetadata=true&pageSize=100"
        )
        if page_key:
            
            url += f"&pageKey={page_key}"
        headers = {"accept": "application/json"}
        r = requests.get(url, headers=headers)
        tokens = r.json()

        if "ownedNfts" not in tokens:
            break
        
        total_count += tokens["totalCount"]
        #count = 0
        owned = tokens["ownedNfts"]
        nft_search = "image"
        nft_animation = "animation"
        nft_video = "video"
        


        for count in range(0,len(owned),+1):
            st.write(token_count)
            col1, col2 = st.columns(2)
            with col1:
                st.write('Token ID:',owned[count]['id']['tokenId'])
                st.write(owned[count]['title'])
                st.image(owned[count]['media'][0]['thumbnail'])
                matching_keys = [key for key in owned[count]['metadata'].keys() if nft_search in key]
                matching_video = [key for key in owned[count]['metadata'].keys() if nft_animation in key]
            with col2:
                if 'attributes' in owned[count]['metadata']:
                    st.dataframe(owned[count]['metadata']['attributes'])

            for x in matching_keys:
                link=owned[count]['metadata'][x]
                res=link.strip('ipfs://')
                new_link= "https://ipfs.io/ipfs/"+ res
                final_link = f'[{x}] ({new_link})'
                file_name=f'{x}.png'
                st.markdown(final_link, unsafe_allow_html=True)

            for x in matching_video:
                rvideo=owned[count]['metadata'][x]
                svideo=rvideo.strip('ipfs://')
                nvideo="https://ipfs.io/ipfs/"+ svideo
                video=f'[Video] ({nvideo})'
                st.markdown(video, unsafe_allow_html=True)
            token_count= token_count+1
            count = count + 1
            st.markdown("""---""")
            
       
        
        if "pageKey" not in tokens:
            break
        else:
            page_key = tokens["pageKey"]
      


if not wallet:
    st.write("To download all GEN's & WW Assets in your wallet")
    st.error("ENTER WALLET ON LEFT")
elif project=='GENs':
    contracts = "contractAddresses[]=0x90a1f4B78Fa4198BB620b7686f510FD476Ec7A0B"
    get_data_by_contract(contracts,wallet)

elif project=='Wapes':
    contracts = "contractAddresses[]=0x05F81F870cBca79E9171f22886b58b5597A603AA"
    get_data_by_contract(contracts,wallet)

elif project=='Motos':
    contracts = "contractAddresses[]=0x51bd5948CF84a1041d2720F56DEd5e173396FC95"
    get_data_by_contract(contracts,wallet)

elif project=='Wolves':
    contracts = "contractAddresses[]=0x1A178CFD768F74b3308cbca9998C767F4E5B2CF8"
    get_data_by_contract(contracts,wallet)

elif project=='AirWild 02':
    contracts = "contractAddresses[]=0x35D2F3CDAf5e2DeA9e6Ae3553A4CaACBA860A395"
    get_data_by_contract(contracts,wallet)

  
elif project=='Wheels, AirWild Season 0 & Season 1, Cribs, & Crafts':
    contracts = "contractAddresses[]=0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D"
    get_data_by_contract(contracts,wallet)



# "&"
# "contractAddresses[]=0xcf8dfce1d4eb0c41194ea3462eb2cdaa880e073f&"
# "contractAddresses[]=0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D"


    

# [
#     "GENs",
#     "Wapes",
#     "Motos",
#     "Wolves",
#     "AirWild 02",
#     "Metaphoenix",
#     "Wheels, AirWild Season 0 & Season 1, Cribs, & Crafts",
#     "Cyberheist",
# ],



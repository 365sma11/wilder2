import requests
import streamlit as st

api_alchemy= st.secrets["api_alchemy"]

st.title(f"SMA11'S WilderWorld BLACK BOOK")
st.header("Download your Media files")
wallet = st.sidebar.text_input("Wallet")



if not wallet:
        st.write("To download all GEN's in your wallet")

        st.error("ENTER WALLET ON LEFT")

else:

    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{api_alchemy}/getNFTs?owner={wallet}&contractAddresses[]=0x90a1f4B78Fa4198BB620b7686f510FD476Ec7A0B&withMetadata=true&pageSize=100"
    headers = {"accept": "application/json"}
    r = requests.get(url, headers=headers)
    tokens=r.json()
    count=0
    owned= tokens['ownedNfts']
    nft_search='image'

    while count<tokens['totalCount']:
        col1, col2 = st.columns(2)
        with col1:
            st.write('Token ID:',owned[count]['id']['tokenId'])
            st.write(owned[count]['title'])
            st.image(owned[count]['media'][0]['thumbnail'])
            #get all 'image' keys
            matching_keys = [key for key in owned[count]['metadata'].keys() if nft_search in key]
        with col2:
            st.dataframe(owned[count]['metadata']['attributes'])
             
        
        for x in matching_keys:
            link=owned[count]['metadata'][x]
            res=link.strip('ipfs://')
            new_link= "https://ipfs.io/ipfs/"+ res
            final_link = f'[{x}] ({new_link})'
            st.markdown(final_link, unsafe_allow_html=True)
        rvideo=owned[count]['metadata']["animation_url"]
        svideo=rvideo.strip('ipfs://')
        nvideo="https://ipfs.io/ipfs/"+ svideo
        video=f'[Video] ({nvideo})'
        st.markdown(video, unsafe_allow_html=True)

        
        count=count +1
        st.markdown("""---""")





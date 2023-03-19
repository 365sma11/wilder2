import requests
import streamlit as st

#api_alchemy= st.secrets["api_alchemy"]
api_alchemy="3bt_UzBPIbWD96mIFUJaOlhEs_7In1kX"

st.title(f"SMA11'S WilderWorld BLACK BOOK")
st.header("Download your Media files")
wallet = st.sidebar.text_input("Wallet")
project= st.sidebar.selectbox("Project", ['GENs','Wapes','Motos','Wolves','AirWild 02','Metaphoenix','Wheels, AirWild Season 0 & Season 1, Cribs, & Crafts','Cyberheist'] )


if not wallet:
        st.write("To download all GEN's in your wallet")

        st.error("ENTER WALLET ON LEFT")

else:
    
    contracts='contractAddresses[]=0x90a1f4B78Fa4198BB620b7686f510FD476Ec7A0B&contractAddresses[]=0x05F81F870cBca79E9171f22886b58b5597A603AA&contractAddresses[]=0x51bd5948CF84a1041d2720F56DEd5e173396FC95&contractAddresses[]=0x35D2F3CDAf5e2DeA9e6Ae3553A4CaACBA860A395&contractAddresses[]=0x1A178CFD768F74b3308cbca9998C767F4E5B2CF8&contractAddresses[]=0xcf8dfce1d4eb0c41194ea3462eb2cdaa880e073f&contractAddresses[]=0xc2e9678A71e50E5AEd036e00e9c5caeb1aC5987D'
    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{api_alchemy}/getNFTs?owner={wallet}&{contracts}&withMetadata=true&pageSize=100"
    headers = {"accept": "application/json"}
    url += f"&pageKey=MHhjMmU5Njc4YTcxZTUwZTVhZWQwMzZlMDBlOWM1Y2FlYjFhYzU5ODdkOjB4ZGRmYTljZDE2YjNmOWNiMWE0NjI0MzgxMzFmOTE4YmNhMWI1ZWQzYzEyZGU0MGVjMWE2YTNhODEwYzNmZmExZTpmYWxzZQ=="
    r = requests.get(url, headers=headers)
    tokens=r.json()
    total_count=tokens['totalCount']
    st.write(f'Count=',[total_count])
    count=0
    owned= tokens['ownedNfts']
    nft_search='image'
    nft_animation='animation'
    nft_video='video'

    while count<tokens['totalCount']:
        st.write(count)
        col1, col2 = st.columns(2)
        with col1:
            st.write('Token ID:',owned[count]['id']['tokenId'])
            st.write(owned[count]['title'])
            st.image(owned[count]['media'][0]['thumbnail'])
            #get all 'image' keys
            matching_keys = [key for key in owned[count]['metadata'].keys() if nft_search in key]
            matching_video = [key for key in owned[count]['metadata'].keys() if nft_animation in key]
        with col2:
            st.dataframe(owned[count]['metadata']['attributes'])
             
        
        for x in matching_keys:
            link=owned[count]['metadata'][x]
            res=link.strip('ipfs://')
            new_link= "https://ipfs.io/ipfs/"+ res
            final_link = f'[{x}] ({new_link})'
            #final_link = f'[{x}](%s)'% new_link #clean embedded hyperlink
            file_name=f'{x}.png'
            st.markdown(final_link, unsafe_allow_html=True)

        for x in matching_video:
            rvideo=owned[count]['metadata'][x]
            svideo=rvideo.strip('ipfs://')
            nvideo="https://ipfs.io/ipfs/"+ svideo
            video=f'[Video] ({nvideo})'
            st.markdown(video, unsafe_allow_html=True)
       
        count=count +1
        st.markdown("""---""")





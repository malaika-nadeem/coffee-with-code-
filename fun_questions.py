import streamlit as st
from PIL import Image
st.title("7 Caror ky sawal's 💅")
name= st.text_input("Ap ky ama abba ny ap ka kai name rakha ha?😆😆","type here")
if st.button("Submit"):
    result=name.title()
    st.success(result)
st.markdown("**Kai ap ki ghar ma izzat ha🤨🤨?**")    
status = st.radio("" , ["izzat woh kai hoti ha" , "nahi ha" , "kabi milli hi nhi"])
if status == "izzat woh kai hoti ha":
       st.success("Mujay pata tha😉")
else:
    st.success("Mujay pata tha😂😂") 

if st.checkbox("AM i ur FRIEND??😋😋"):
    img = Image.open("cats.jfif")
    st.image(img,width=300)
hobby = st.selectbox("AP ko apni amma sy kis kis cheez sy maar pariha?💅",['thapaar','jotay sy','balanay sy']) 
st.write("shahbash😂",hobby)
if st.checkbox("kai ap canteen mein sabse pehle pahunchta hai par class mein sabse last?🤔"):
    st.markdown("shahbash laagay raho!!!😂😂")
    img = Image.open("shahbash.jfif")
    st.image(img,width=350)
import streamlit as st
st.set_page_config(
    page_title="My Calculator",
    page_icon="🧮",
    layout="wide"
)
st.markdown("""
    <style>
    .stApp {
        background-color: #F8C8DC;}
    .stNumberInput input{
        background-color: #FFB5C0;
        border: 2px solid #000000;
        border-radius: 5px;
    }
    .stButton button{
        font-weight: bold';
    } 
    .stSelectbox div[data-baseweb="select"]{
        background-color: #FDFD96;
        border: 2px solid #000000;
        border-radius: 5px;
    }
    div[class="stRadio"] label {
    font-size: 22px !important;
    font-weight: bold !important;
}
       
    
    </style>
""", unsafe_allow_html=True)

def calculator():
    st.title("Calculator")
    st.write("This is a simple calculator built with Streamlit.")
    col1,col2 = st.columns(2)
    with col1:
      num1 = st.number_input("Enter the first number:")
    
      num2 = st.number_input("Enter the second number:")
      operator = st.radio(
    "**Select operation:**",
    ["+", "-", "*", "/", "%"],
    horizontal=True    # shows them side by side!
)
    with col2:
     if st.button("**Calculate**"):
        result = perform_operation(num1, num2, operator)
        st.metric(label="Result", value=result)
        st.image("cute.jfif" , width=100)

def perform_operation(num1, num2, operator):
     if operator == "+":
        return num1 + num2
     elif operator == "-":
        return num1 - num2
     elif operator == "*":
        return num1 * num2
     elif operator == "/":
          return num1 / num2 if num2 != 0 else "Error: Division by zero"
     elif operator == "%":
        return num1 % num2 if num2 != 0 else "Error: Division by zero"
     
       

calculator()


import streamlit
from backend import IntBinary

streamlit.title("Integer to Binary Converter")
intvalue= int(streamlit.number_input("Input any integer value"))
if(streamlit.button('Convert to binary')):
    streamlit.text(f"Your converted value is : {IntBinary(intvalue)}")
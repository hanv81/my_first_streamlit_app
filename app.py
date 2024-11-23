import streamlit as st

def create_interface():
  a = st.number_input('Nhập số thực a')
  b = st.number_input('Nhập số thực b')
  return a,b
  
def calculate(a, b):
  return a + b, a - b

def main():
  a,b = create_interface()
  if st.button('Calculate', use_container_width=True):
    total, minus = calculate(a, b)
    st.write('Tổng của a & b là', total)
    st.write('Hiệu của a & b là', minus)

main()

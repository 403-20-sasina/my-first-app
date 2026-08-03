import streamlit as at
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):",value=0.0)
vat = price * 0.07
net_price = price - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider("นางสาวศศินา เดชเสน เลขที่20 ม.4/3")

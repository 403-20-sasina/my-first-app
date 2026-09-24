import streamlit as st

st.set_page_config(
    page_title="Slide Drive Thru - Smart Shop & Discount",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 Slide Drive Thru")
st.caption("Smart Shop & Discount Application | ระบบสั่งอาหารและคำนวณส่วนลดอัตโนมัติ")

tab1, tab2, tab3 = st.tabs(["🛒 สั่งซื้อสินค้า (Shop)", "🎮 ตอบคำถามสะสมแต้ม (Quiz)", "📖 คำศัพท์ภาษาอังกฤษ (Vocabulary)"])

with tab1:
    st.header("รายการสินค้า (Menu)")
    
    menu_items = {
        "Burger set": 150,
        "Double Beef Burger": 120,
        "Crispy Chicken Burger": 89,
        "Frenchfries": 60,
        "Soft drink": 40
    }
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("เลือกจำนวนสินค้า")
        cart = {}
        total_items = 0
        raw_price = 0.0
        
        for item, price in menu_items.items():
            qty = st.number_input(f"{item} ({price} ฿)", min_value=0, max_value=20, value=0, step=1, key=item)
            if qty > 0:
                cart[item] = {"qty": qty, "price": price, "subtotal": qty * price}
                raw_price += qty * price
                total_items += qty

    with col2:
        st.subheader("สรุปรายการสั่งซื้อ")
        if cart:
            for item, info in cart.items():
                st.write(f"- {item} x {info['qty']} = {info['subtotal']} ฿")
            st.divider()
            st.write(f"**ราคารวมขั้นต้น:** {raw_price:.2f} ฿")
        else:
            st.info("กรุณาเลือกรายการสินค้าด้านซ้าย")

    st.divider()
    
    st.header("🎁 สิทธิพิเศษ & การคำนวณส่วนลด")
    
    use_vip = st.checkbox("เป็นสมาชิก VIP Member (รับส่วนลดเพิ่ม 10%)")
    
    final_price = raw_price
    discount_amount = 0.0
    
    if use_vip and raw_price > 0:
        discount_amount = raw_price * 0.10
        final_price = raw_price - discount_amount
        st.success(f"🎉 ได้รับส่วนลด VIP 10% เป็นเงิน {discount_amount:.2f} บาท")
    
    st.metric(label="ยอดเงินสุทธิที่ต้องชำระ", value=f"{final_price:.2f} ฿")
    
    st.subheader("สิทธิ์ของแถมที่ได้รับตามยอดซื้อ:")
    
    if raw_price >= 500:
        st.balloons()
        st.success("🌟 ซื้อครบ 500 ฿: คุณได้รับสิทธิ์ลุ้นรับ **เบอร์เกอร์เนื้อ 1 ชิ้น ฟรี!**")
        st.info("🎉 คุณได้รับสิทธิ์สุ่มวงล้อรับเครื่องดื่มฟรี 1 แก้ว ด้วย!")
        st.info("🎁 คุณได้รับสิทธิ์ลุ้นรับของสะสมคาแรกเตอร์ Collab ด้วย!")
    elif raw_price >= 300:
        st.success("🎉 ซื้อครบ 300 ฿: คุณได้รับสิทธิ์ **สุ่มวงล้อรับเครื่องดื่มฟรี 1 แก้ว!**")
        st.info("🎁 คุณได้รับสิทธิ์ลุ้นรับของสะสมคาแรกเตอร์ Collab ด้วย!")
    elif raw_price >= 250:
        st.success("🎁 ซื้อครบ 250 ฿: คุณได้รับสิทธิ์ **ลุ้นรับของสะสมคาแรกเตอร์ที่ทางร้านทำการคอลแลปด้วย!**")
    elif raw_price > 0:
        st.warning(f"💡 ช้อปอีกเพียง {250 - raw_price:.2f} ฿ เพื่อรับสิทธิ์ลุ้นของสะสมสุดพิเศษ!")
    else:
        st.write("- ยังไม่มีรายการสั่งซื้อ")

with tab2:
    st.header("🎯 ควิซคำนวณส่วนลดและคำศัพท์")
    
    # คำถามที่ 1 (จากใบงานเดิม)
    st.subheader("ข้อที่ 1")
    q1 = st.radio(
        "Q: If you buy a Burger Set (150฿) with a 20% discount coupon, how much do you pay?",
        ["100 ฿", "120 ฿", "130 ฿", "150 ฿"],
        index=None
    )
    if q1:
        if q1 == "120 ฿":
            st.success("✅ ถูกต้อง! คำนวณจาก: 150 - (150 x 0.20) = 120 ฿")
        else:
            st.error("❌ ยังไม่ถูกต้อง ลองคำนวณใหม่อีกครั้งนะ!")

    st.divider()

    st.subheader("ข้อที่ 2")
    q2 = st.radio(
        "Q: หากซื้อ Frenchfries (60฿) + Soft drink (40฿) แล้วใช้คูปองส่วนลด 10% คุณต้องจ่ายเงินกี่บาท?",
        ["80 ฿", "85 ฿", "90 ฿", "100 ฿"],
        index=None
    )
    if q2:
        if q2 == "90 ฿":
            st.success("✅ ถูกต้อง! ราคารวม 100฿ หักส่วนลด 10% (10฿) เหลือ 90 ฿")
        else:
            st.error("❌ ยังไม่ถูกต้อง ลองคิดดูใหม่อีกทีนะ!")

    st.divider()

    st.subheader("ข้อที่ 3")
    q3 = st.radio(
        "Q: สั่ง Double Beef Burger 2 ชิ้น (ชิ้นละ 120฿) ช่วงโปรโมชั่น 'ซื้อ 2 ชิ้นลดทันที 30 บาท' ต้องจ่ายเงินกี่บาท?",
        ["210 ฿", "220 ฿", "240 ฿", "215 ฿"],
        index=None
    )
    if q3:
        if q3 == "210 ฿":
            st.success("✅ ถูกต้อง! (120 x 2) - 30 = 210 ฿")
        else:
            st.error("❌ คำตอบยังไม่ถูกค่ะ")

    st.divider()

    st.subheader("ข้อที่ 4")
    q4 = st.radio(
        "Q: สั่ง Crispy Chicken Burger (89฿) + Frenchfries (60฿) + Soft drink (40฿) รวมเป็นกี่บาท และถึงขั้นต่ำ 250฿ หรือไม่?",
        ["189 ฿ (ไม่ถึงสิทธิ์ขั้นต่ำ)", "200 ฿ (ถึงสิทธิ์ขั้นต่ำ)", "189 ฿ (ถึงสิทธิ์ขั้นต่ำ)"],
        index=None
    )
    if q4:
        if q4 == "189 ฿ (ไม่ถึงสิทธิ์ขั้นต่ำ)":
            st.success("✅ ถูกต้อง! ยอดรวม 189 บาท ยังไม่ถึงเกณฑ์ขั้นต่ำ 250 บาท")
        else:
            st.error("❌ ลองคำนวณยอดรวมใหม่อีกครั้ง")

with tab3:
    st.header("📖 คำศัพท์น่ารู้ประจำร้าน")
    
    vocab_data = {
        "คำศัพท์ (Vocabulary)": ["Drive thru", "Discount", "Combo set"],
        "ความหมาย (Meaning)": ["บริการไดร์ฟทรู", "ส่วนลด", "ชุดอาหารโปรโมชั่น"]
    }
    st.table(vocab_data)

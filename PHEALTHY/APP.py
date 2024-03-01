import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np

# Sample BMI distribution for individuals in Thailand
thai_bmi_distribution = {
    "Underweight": 10,
    "Normal": 60,
    "Overweight": 20,
    "Obese": 10
}

def main():
    st.set_page_config(
        page_title="P'Healthy",
        page_icon=":apple:",
        layout="centered",  # Center the content
        initial_sidebar_state="expanded",  # Sidebar expanded by default
    )

    # Set background color and text color
    st.markdown(
        """
        <style>
        body {
            background-color: #96cfcf;  /* Light grey background */
            color: #333333;  /* Dark grey text */
        }
        </style>
        """,
        unsafe_allow_html=True)

    # Sidebar navigation
    page = st.sidebar.selectbox("Search", ["หน้าหลัก", "สารอาหาร", "ออกกำลังกาย", "สูตรอาหาร", "หาค่า BMI(ดัชนีมวลกาย)","คำนวณความเสี่ยงโรค"])

    if page == "หน้าหลัก":
        show_home_page()
    elif page == "สารอาหาร":
        show_nutrition_page()
    elif page == "ออกกำลังกาย":
        show_exercise_page()
    elif page == "สูตรอาหาร":
        show_recipes_page()
    elif page == 'หาค่า BMI(ดัชนีมวลกาย)':
        show_bmi_page()
    elif page == "คำนวณความเสี่ยงโรค":
        show_disease_risk_page()    

def show_home_page():
    st.write("สวัสดีครับ ยินดีต้อนรับสู่ P'healthy เราเป็นเว็ปไซด์สายสุขภาพ เหมาะสำหรับใครที่อยากเริ่มที่จะดูแลสุขภาพ ")
    st.write('สิ่งที่เสียไปแล้วไม่กลับคืนมา มีเพียงเวลาและสุขภาพ')

def show_nutrition_page():
    st.title("สารอาหารที่มีประโยชน์ต่อร่างกาย")
    st.write("สารอาหารที่มีประโยชน์สำหรับร่างกายมีหลายประเภทและมีบทบาทสำคัญในการส่งเสริมสุขภาพและความเป็นอยู่ที่ดีของร่างกาย. ดังนี้คือรายละเอียดเกี่ยวกับสารอาหารที่มีประโยชน์ต่อร่างกาย:")
    
    st.markdown("1. **โปรตีน (Protein)**:")
    st.write("- โปรตีนเป็นสารอาหารที่สำคัญสำหรับการสร้างและซ่อมแซมเนื้อเยื่อในร่างกาย เช่น กล้ามเนื้อ, หนัง, และเส้นเลือด")
    st.write("- มีหลายแหล่งที่มาของโปรตีน เช่น เนื้อสัตว์, ถั่ว, ถั่วลิสง, เมล็ดพืช, และผลไม้")
    
    st.markdown("2. **คาร์โบไฮเดรต (Carbohydrates)**:")
    st.write("- คาร์โบไฮเดรตเป็นแหล่งพลังงานหลักสำหรับร่างกาย")
    st.write("- มีหลายชนิดของคาร์โบไฮเดรต เช่น คาร์โบไฮเดรตที่ซับซ้อนเช่น ธัญพืชและอาหารเค็ม และคาร์โบไฮเดรตที่ง่ายต่อการดูดซึมเช่น น้ำตาล")
    
    st.markdown("3. **ไขมัน (Fat)**:")
    st.write("- ไขมันมีบทบาทในการให้พลังงานและสร้างเซลล์ในร่างกาย")
    st.write("- มีไขมันที่ดีต่อร่างกาย เช่น ไขมันไม่อิ่มตัวเช่น ไขมันไม่อิ่มตัวหรือไขมันต่ำเช่น น้ำมันมะกอก, น้ำมันมะพร้าว, และไขมันในอาหารทะเล เป็นต้น")
    
    st.markdown("4. **วิตามินและแร่ธาตุ (Vitamins and Minerals)**:")
    st.write("- วิตามินและแร่ธาตุมีบทบาทสำคัญในการรักษาสุขภาพของร่างกาย โดยมีหลายชนิดที่มีความสำคัญ เช่น วิตามิน C, วิตามิน D, เหล็ก, แคลเซียม, และโซเดียม")
    st.write("- แหล่งที่มาของวิตามินและแร่ธาตุรวมถึงผัก, ผลไม้, เนื้อสัตว์, อาหารทะเล, และอาหารที่ถูกเสริมด้วยวิตามินและแร่ธาตุ")
    
    st.markdown("5. **ใยอาหาร (Dietary Fiber)**:")
    st.write("- ใยอาหารมีประโยชน์ต่อระบบย่อยอาหารและระบบย่อยอาหาร")
    st.write("- แหล่งที่มาของใยอาหารรวมถึงผัก, ผลไม้, ธัญพืช, เมล็ดพืช, และข้าวโอ๊ต")
    
    st.markdown("6. **น้ำ (Water)**:")
    st.write("- น้ำมีบทบาทสำคัญในการรักษาสมดุลของร่างกาย โดยช่วยในการระบายของเสีย, การย่อยอาหาร, และการส่งผ่านสารอาหารไปยังเซลล์ต่างๆในร่างกาย")
    st.write("- การดื่มน้ำเป็นวิธีง่ายๆในการรักษาสมดุลของร่างกายและการสุขภาพที่ดี")

def show_exercise_page():
    st.title("ออกกำลังกายเพื่อสุขภาพ")
    st.write("ออกกำลังกายเป็นส่วนสำคัญของการรักษาสุขภาพของร่างกาย ด้านล่างนี้เป็นบางกิจกรรมที่คุณสามารถทำเพื่อสุขภาพของคุณ:")
    st.write("- การวิ่ง")
    st.write("- การเดิน")
    st.write("- การว่ายน้ำ")
    st.write("- การยิงธนู")
    st.write("- การยกน้ำหนัก")
    st.write("- โยคะ")
    st.write("- การปั่นจักรยาน")

def show_recipes_page():
    st.header("สูตรอาหารเพื่อสุขภาพ")
    st.write("ขอแนะนำสูตรอาหารที่เหมาะสำหรับการรักษาสุขภาพของคุณ:")
    st.write("1. สลัดผักผลไม้สด: ผสมผักใบเขียวหลากหลายชนิดพร้อมผลไม้สด เช่น มะเขือเทศ, แตงกวา")
    st.write("2. ปลาย่างผักสด: ปรุงปลาชนิดต่างๆ ย่างบนเตาหรือเมนูอื่นๆ รับประทานคู่กับผักสด")
    st.write("3. สปาเก็ตตี้ผัก: ใช้สปาเก็ตตี้ที่ทำจากแป้งโฮลวีท คู่กับผักต่างๆ เช่น บรอกโคลี, มะเขือเทศ")
    st.write("4. ไก่ย่างพริกไทยดำ: ปรุงไก่ด้วยพริกไทยดำและสมุนไพรต่างๆ อย่างสับปะรดหรือมะเขือเทศ")
    st.write("5. ข้าวกล้องผัดผักรวม: ผักผลไม้ต่างๆ ผสมกับข้าวกล้อง และเติมโปรตีนจากไข่ไก่หรือไข่ไข่ไก่ขาว")

def show_bmi_page():
    st.title("คำนวณดัชนีมวลกาย (BMI)")
    st.write("กรุณากรอกข้อมูลเพื่อคำนวณดัชนีมวลกายของคุณ")

    # Input fields for height and weight
    height = st.number_input("ส่วนสูง (เซนติเมตร)", min_value=1.0, max_value=300.0, step=0.1, format="%.1f")
    weight = st.number_input("น้ำหนัก (กิโลกรัม)", min_value=1.0, max_value=1000.0, step=0.1, format="%.1f")

    if st.button("คำนวณ"):
        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)

        # Display BMI result
        st.write("ค่า BMI ของคุณคือ: {:.2f}".format(bmi))
        st.write("ผลลัพธ์ของคุณ")
        if bmi < 18.5:
            st.write("น้ำหนักน้อยหรือผอม")
        elif bmi < 25:
            st.write("ปกติ (สุขภาพดี)")
        elif bmi < 30:
            st.write("ท้วม (Overweight)")
        else:
            st.write("อ้วน (Obese)")

        # Display BMI result as a comparison with Thai BMI distribution
        fig, ax = plt.subplots()
        sns.barplot(x=list(thai_bmi_distribution.keys()), y=list(thai_bmi_distribution.values()), ax=ax, color='skyblue', label='Thai people')
        ax.axhline(bmi, color='red', linestyle='--', label='Your BMI')
        ax.set_ylabel("Percentage")
        ax.set_title("You vs Thai people ")
        ax.legend()
        st.pyplot(fig)

if __name__ == "__main__":
    main()

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nutrition_image_url = "https://cdn.lifeofpix.com/113763/_w1800/306929/lifeofpix-rawpixelcom1624-306929.webp"
exercise_image_url = "https://cdn.lifeofpix.com/243359/_w1800/365037/lifeofpix-timmy-365037.webp"
recipes_image_url = "https://cdn.lifeofpix.com/113763/_w1800/307999/lifeofpix-rawpixelcom1624-307999.webp"
bmi_image_url = "https://camillianhospital.org/wp-content/uploads/2023/10/bmi-adult-fb-600x315-1.jpg"

# Sample BMI distribution for individuals in Thailand
thai_bmi_distribution = {
    "Underweight": 10,
    "Normal": 60,
    "Overweight": 20,
    "Obese": 10
}
def main():

    page = st.sidebar.selectbox("Search", ["หน้าหลัก", "สารอาหาร", "ออกกำลังกาย", "สูตรอาหาร", "BMI(ดัชนีมวลกาย)","BMR(คำนวนแคลอรี่)"])
    
    if page == "หน้าหลัก":
        show_home_page()
    elif page == "สารอาหาร":
        show_nutrition_page()
    elif page == "ออกกำลังกาย":
        show_exercise_page()
    elif page == "สูตรอาหาร":
        show_recipes_page()
    elif page == 'BMI(ดัชนีมวลกาย)':
        show_bmi_page()
    elif page == 'BMR(คำนวนแคลอรี่)':
        show_bmr_page()

def show_home_page():
    st.subheader("สวัสดีครับ ยินดีต้อนรับสู่ P'healthy เราเป็นเว็ปไซด์สายสุขภาพ เหมาะสำหรับใครที่อยากเริ่มที่จะดูแลสุขภาพ ")
    st.subheader('สิ่งที่เสียไปแล้วไม่กลับคืนมา มีเพียงเวลาและสุขภาพ')
    st.write('     การดูแลสุขภาพเป็นปัจจัยสำคัญที่มีผลต่อคุณภาพชีวิตของเราทั้งทางร่างกายและจิตใจ มันไม่เพียงแต่ช่วยลดความเสี่ยงต่อโรคต่างๆ แต่ยังเสริมสร้างความเข้มแข็งในการเผชิญหน้ากับความกดดันและปัญหาทางสุขภาพที่อาจเกิดขึ้นในอนาคต ดังนั้น ขอนำเสนอเคล็บแน่นๆเกี่ยวกับการดูแลสุขภาพที่สามารถปรับใช้ในชีวิตประจำวันได้ มาพร้อมกันสำหรับการมีสุขภาพที่ดีอย่างยั่งยืน:')
    st.markdown('1. การบริโภคอาหารที่สมดุล: อาหารเป็นแหล่งพลังงานและสารอาหารสำคัญที่ส่งเสริมสุขภาพของร่างกาย เลือกอาหารที่มีประโยชน์และมีสารอาหารทุกประเภท เช่น ผัก ผลไม้ ธัญพืช เนื้อสัตว์ที่มีไขมันน้อย และโปรตีนคุณภาพสูง เพื่อสร้างสมดุลที่เหมาะสมในการบริโภค')
    st.markdown("")
    st.image('https://ccc.mots.go.th/uploads/cover_news/69eabba8806c2e3fc0cdd7af215730a3.jpg')
    st.markdown("")
    st.markdown('2. การออกกำลังกายอย่างสม่ำเสมอ: ออกกำลังกายเป็นสิ่งจำเป็นที่ช่วยบำรุงสุขภาพของหัวใจและระบบที่รองรับการทำงานของร่างกาย ควรมีกิจกรรมทางกายที่หลากหลาย เช่น การเดิน เล่นกีฬา โยคะ หรือการวิ่ง อย่างน้อย 30 นาทีต่อวันเพื่อรักษาระดับสุขภาพที่ดี **')
    st.markdown("")
    st.image('https://pt.mahidol.ac.th/ptcenter/wp-content/uploads/2021/12/1-1.jpg')
    st.markdown('3. การรักษาสุขภาพจิต: การดูแลสุขภาพจิตเป็นส่วนสำคัญที่ช่วยให้เรามีความสุขและสมดุลในชีวิต ควรให้เวลากับกิจกรรมที่ช่วยผ่อนคลาย เช่น การทำสมาธิ การฝึกโยคะ การพักผ่อน และการเรียนรู้เทคนิคการจัดการความเครียด **')
    st.markdown("")
    st.image('https://lh3.googleusercontent.com/proxy/7uAGHyxpYBZ95IhrsJ0DQwZJlP_Rxc2cx2OHrmcdQrLZHBrSnXQ28tEqk-4kJ0PbrXvOjDexokJKnJXxviA3t3KljRk3oJoOgXNuVAKRABU')
    st.markdown('4. การรักษาความสะอาด: การรักษาความสะอาดส่วนบุคคลและสิ่งแวดล้อมเป็นสิ่งสำคัญที่ช่วยลดความเสี่ยงต่อการติดเชื้อโรค ควรล้างมือบ่อยๆ ใช้หน้ากากอนามัยในสถานที่แออัด และรักษาความสะอาดของสิ่งแวดล้อมในบ้านและที่ทำงาน **')
    st.markdown("https://www.phitsanulok-hospital.com/stocks/news/c710x400/bw/zr/fyvibwzr0k5/16-9-65-th.png")
    st.image('https://www.phitsanulok-hospital.com/stocks/news/c710x400/bw/zr/fyvibwzr0k5/16-9-65-th.png')
    st.markdown('5. การนอนพักผ่อน: การนอนพักผ่อนเพียงพอเป็นปัจจัยสำคัญที่ช่วยฟื้นฟูร่างกายและสมอง ควรรักษาการนอนหลับให้เพียงพอตามที่แพทย์แนะนำ โดยเฉพาะผู้ใหญ่ควรนอนอย่างน้อย 7-8 ชั่วโมงต่อวัน **')
    st.markdown("")
    st.image('https://cdn05.zipify.com/0a7ZMYv_Af01lcvig4NUbi-tQXo=/fit-in/1080x0/d3472f1143ff4f93b4170db151c7342f/2.png')
    st.markdown('6. การตรวจสุขภาพประจำ: การตรวจสุขภาพประจำเป็นการตรวจสุขภาพเบื้องต้นและตรวจสุขภาพประจำปีที่ช่วยตรวจสอบสุขภาพทั้งร่างกายและจิตใจ ควรตรวจสุขภาพอย่างสม่ำเสมอเพื่อค้นหาปัญหาทางสุขภาพในระยะเริ่มต้นและป้องกันโรคที่เป็นไปได้ **')
    st.markdown("")
    st.image('https://png.pngtree.com/png-clipart/20210826/ourmid/pngtree-physical-examination-hand-drawn-cartoon-elements-png-image_3460465.jpg')
    st.markdown('7. การหลีกเลี่ยงสิ่งที่เสี่ยงต่อสุขภาพ: หลีกเลี่ยงการสูบบุหรี่ ดื่มสุราเป็นประจำ การบริโภคอาหารที่มีไขมันและน้ำตาลสูง และการพักผ่อนนอนหลับไม่เพียงพอ เป็นต้น เพื่อลดความเสี่ยงต่อการเป็นโรคในอนาคต **')
    st.markdown("")
    st.image('https://www.kidjapak.com/wp-content/uploads/2019/03/ไต.jpg')
    st.markdown('** การดูแลสุขภาพไม่ได้เป็นเรื่องที่ซับซ้อนหรือยากลำบาก มันเริ่มต้นจากการทำเล็กน้อยที่เราสามารถปรับเปลี่ยนได้ในชีวิตประจำวัน เมื่อเรามีการดูแลสุขภาพที่ดี เราจะสามารถมีคุณภาพชีวิตที่ดีและมีความสุขอย่างแท้จริงได้ในทุกๆ วัน อย่าลืมว่าสุขภาพที่ดีเป็นทรัพย์สำคัญที่สุดที่เรามีในชีวิต **')

def show_nutrition_page():
    st.title("สารอาหารที่มีประโยชน์ต่อร่างกาย")
    st.image(nutrition_image_url, use_column_width=True)
    st.write("สารอาหารที่มีประโยชน์สำหรับร่างกายมีหลายประเภทและมีบทบาทสำคัญในการส่งเสริมสุขภาพและความเป็นอยู่ที่ดีของร่างกาย. ดังนี้คือรายละเอียดเกี่ยวกับสารอาหารที่มีประโยชน์ต่อร่างกาย:")
    
    st.header("*โปรตีน (Protein)*:")
    st.write("- โปรตีนเป็นสารอาหารที่สำคัญสำหรับการสร้างและซ่อมแซมเนื้อเยื่อในร่างกาย เช่น กล้ามเนื้อ, หนัง, และเส้นเลือด")
    st.write("- มีหลายแหล่งที่มาของโปรตีน เช่น เนื้อสัตว์, ถั่ว, ถั่วลิสง, เมล็ดพืช, และผลไม้")
    
    st.header("*คาร์โบไฮเดรต (Carbohydrates)*:")
    st.write("- คาร์โบไฮเดรตเป็นแหล่งพลังงานหลักสำหรับร่างกาย")
    st.write("- มีหลายชนิดของคาร์โบไฮเดรต เช่น คาร์โบไฮเดรตที่ซับซ้อนเช่น ธัญพืชและอาหารเค็ม และคาร์โบไฮเดรตที่ง่ายต่อการดูดซึมเช่น น้ำตาล")
    
    st.header("*ไขมัน (Fat)*:")
    st.write("- ไขมันมีบทบาทในการให้พลังงานและสร้างเซลล์ในร่างกาย")
    st.write("- มีไขมันที่ดีต่อร่างกาย เช่น ไขมันไม่อิ่มตัวเช่น ไขมันไม่อิ่มตัวหรือไขมันต่ำเช่น น้ำมันมะกอก, น้ำมันมะพร้าว, และไขมันในอาหารทะเล เป็นต้น")
    
    st.header("*วิตามินและแร่ธาตุ (Vitamins and Minerals)*:")
    st.write("- วิตามินและแร่ธาตุมีบทบาทสำคัญในการรักษาสุขภาพของร่างกาย โดยมีหลายชนิดที่มีความสำคัญ เช่น วิตามิน C, วิตามิน D, เหล็ก, แคลเซียม, และโซเดียม")
    st.write("- แหล่งที่มาของวิตามินและแร่ธาตุรวมถึงผัก, ผลไม้, เนื้อสัตว์, อาหารทะเล, และอาหารที่ถูกเสริมด้วยวิตามินและแร่ธาตุ")
    
    st.header("*ใยอาหาร (Dietary Fiber)*:")
    st.write("- ใยอาหารมีประโยชน์ต่อระบบย่อยอาหารและระบบย่อยอาหาร")
    st.write("- แหล่งที่มาของใยอาหารรวมถึงผัก, ผลไม้, ธัญพืช, เมล็ดพืช, และข้าวโอ๊ต")
    
    st.header("*น้ำ (Water)*:")
    st.write("- น้ำมีบทบาทสำคัญในการรักษาสมดุลของร่างกาย โดยช่วยในการระบายของเสีย, การย่อยอาหาร, และการส่งผ่านสารอาหารไปยังเซลล์ต่างๆในร่างกาย")
    st.write("- การดื่มน้ำเป็นวิธีง่ายๆในการรักษาสมดุลของร่างกายและการสุขภาพที่ดี")

def show_exercise_page():
    st.title("ออกกำลังกายเพื่อสุขภาพ")
    st.image(exercise_image_url, use_column_width=True)
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
    st.image(recipes_image_url, use_column_width=True)
    st.write("ขอแนะนำสูตรอาหารที่เหมาะสำหรับการรักษาสุขภาพของคุณ:")
    st.write("1. สลัดผักผลไม้สด: ผสมผักใบเขียวหลากหลายชนิดพร้อมผลไม้สด เช่น มะเขือเทศ, แตงกวา")
    st.write("2. ปลาย่างผักสด: ปรุงปลาชนิดต่างๆ ย่างบนเตาหรือเมนูอื่นๆ รับประทานคู่กับผักสด")
    st.write("3. สปาเก็ตตี้ผัก: ใช้สปาเก็ตตี้ที่ทำจากแป้งโฮลวีท คู่กับผักต่างๆ เช่น บรอกโคลี, มะเขือเทศ")
    st.write("4. ไก่ย่างพริกไทยดำ: ปรุงไก่ด้วยพริกไทยดำและสมุนไพรต่างๆ อย่างสับปะรดหรือมะเขือเทศ")
    st.write("5. ข้าวกล้องผัดผักรวม: ผักผลไม้ต่างๆ ผสมกับข้าวกล้อง และเติมโปรตีนจากไข่ไก่หรือไข่ไข่ไก่ขาว")


def show_bmi_page():
    st.title("คำนวณดัชนีมวลกาย (BMI)")
    st.image(bmi_image_url, use_column_width=True)
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

def calculate_bmr(weight, height, age, gender):
    if gender == "ชาย":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

def show_bmr_page():
    st.subheader("คำนวณ BMR (Basal Metabolic Rate)")
    weight = st.number_input("น้ำหนัก (กิโลกรัม)", step=1)
    height = st.number_input("ส่วนสูง (เซนติเมตร)", step=1)
    age = st.number_input("อายุ",step=1)
    gender = st.radio("เพศ", ("ชาย", "หญิง"))
    if st.button("คำนวณ"):
        bmr = calculate_bmr(weight, height, age, gender)
        st.write("BMR (Basal Metabolic Rate): {:.2f} แคลอรี่".format(bmr))


if __name__ == "__main__":
    main()

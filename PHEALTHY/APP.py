import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import base64
import requests

class PhealthyApp:
    def __init__(self):
        self.nutrition_image_url = "https://cdn.lifeofpix.com/113763/_w1800/306929/lifeofpix-rawpixelcom1624-306929.webp"
        self.exercise_image_url = "https://cdn.lifeofpix.com/243359/_w1800/365037/lifeofpix-timmy-365037.webp"
        self.recipes_image_url = "https://cdn.lifeofpix.com/113763/_w1800/307999/lifeofpix-rawpixelcom1624-307999.webp"
        self.bmi_image_url = "https://camillianhospital.org/wp-content/uploads/2023/10/bmi-adult-fb-600x315-1.jpg"

# Sample BMI distribution for individuals in Thailand
        self.thai_bmi_distribution = {
            "Underweight": 10,
            "Normal": 60,
            "Overweight": 20,
            "Obese": 10
        }


    def main(self):
        st.title("P'HEALTHY")
        self.setup_background_page()
        page = st.sidebar.selectbox("Search", ["หน้าหลัก", "สารอาหาร", "ออกกำลังกาย", "สูตรอาหาร", "BMI(ดัชนีมวลกาย)","BMR(คำนวนแคลอรี่)"])

        if page == "หน้าหลัก":
            self.show_home_page()
        elif page == "สารอาหาร":
            self.show_nutrition_page()
        elif page == "ออกกำลังกาย":
            self.show_exercise_page()
        elif page == "สูตรอาหาร":
            self.show_recipes_page()
        elif page == 'BMI(ดัชนีมวลกาย)':
            self.show_bmi_page()
        elif page == 'BMR(คำนวนแคลอรี่)':
            self.show_bmr_page()
    @st.cache
    def get_img_as_base64(self, url):
        with st.spinner('Loading image...'):
            res = requests.get(url)
            encoded = base64.b64encode(res.content).decode()
        return f"data:image/png;base64,{encoded}"

    def setup_background_page(self):
        img = self.get_img_as_base64(self.bmi_image_url)

        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("https://images.wallpaperscraft.com/image/single/leaves_dark_plant_136935_1024x600.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        [data-testid="stSidebar"] > div:first-child {{
            background-image: url("https://cdn.wallpaperjam.com/content/images/79/4a/794a41be2d03c640ab6060088f0225b93177e304.jpg");
            background-position: center; 
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }}
        
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}
        
        [data-testid="stToolbar"] {{
            right: 2rem;
        }}
        </style>
        """        
        st.markdown(page_bg_img, unsafe_allow_html=True)

    
    def show_home_page(self):
        st.header("สวัสดีครับ ยินดีต้อนรับสู่ P'healthy เราเป็นเว็ปไซด์สายสุขภาพ เหมาะสำหรับใครที่อยากเริ่มที่จะดูแลสุขภาพ ")
        st.subheader(' "สิ่งที่เสียไปแล้วไม่กลับคืนมา มีเพียงเวลาและสุขภาพ" ')
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
        st.image('https://www.tmwa.or.th/new/lib/file/2016118185741.png')
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

    def show_nutrition_page(self):
        st.title("สารอาหารที่มีประโยชน์ต่อร่างกาย")
        st.image(self.nutrition_image_url, use_column_width=True)
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

    def show_exercise_page(self):
        st.title("ออกกำลังกายเพื่อสุขภาพ")
        st.image(self.exercise_image_url, use_column_width=True)
        st.write("ออกกำลังกายเป็นส่วนสำคัญของการรักษาสุขภาพของร่างกาย ด้านล่างนี้เป็นบางกิจกรรมที่คุณสามารถทำเพื่อสุขภาพของคุณ:")
        st.subheader("- การวิ่ง")
        st.markdown("")
        st.image('https://stadiumth.s3.ap-southeast-1.amazonaws.com/upload/1643382131153.jpg')
        st.subheader("- การเดิน")
        st.markdown("")
        st.image('https://inwfile.com/s-fl/mfeaxl.jpg')
        st.subheader("- การว่ายน้ำ")
        st.markdown("")
        st.image('https://i0.wp.com/www.vrunvride.com/wp-content/uploads/2019/07/serena-repice-lentini-TVOAbbLL050-unsplash.jpg?resize=750%2C534&ssl=1')
        st.subheader("- การยิงธนู")
        st.markdown("")
        st.image('https://media.istockphoto.com/id/1194824160/th/เวคเตอร์/ยิงธนูพร้อมทบต้นธนูกีฬา.jpg?s=1024x1024&w=is&k=20&c=sK9HEc7rvTInB5t995a2KxEbz4atjuAkII6fEqcWK24=')
        st.subheader("- การยกน้ำหนัก")
        st.markdown("")
        st.image('https://pt.mahidol.ac.th/knowledge/wp-content/uploads/2021/10/pic1.jpg')
        st.subheader("- โยคะ")
        st.markdown("")
        st.image("https://img.kapook.com/u/patcharin/Exercise/Yoga/yoga1_2.jpg")
        st.subheader("- การปั่นจักรยาน")
        st.markdown("")
        st.image('https://s.isanook.com/he/0/ud/3/16317/cycling.jpg')
  
    def show_recipes_page(self):
        st.header("สูตรอาหารเพื่อสุขภาพ")
        st.image(self.recipes_image_url, use_column_width=True)
        st.write("ขอแนะนำสูตรอาหารที่เหมาะสำหรับการรักษาสุขภาพของคุณ:")
        st.write("1. สลัดผักผลไม้สด: ผสมผักใบเขียวหลากหลายชนิดพร้อมผลไม้สด เช่น มะเขือเทศ, แตงกวา")
        st.write("2. ปลาย่างผักสด: ปรุงปลาชนิดต่างๆ ย่างบนเตาหรือเมนูอื่นๆ รับประทานคู่กับผักสด")
        st.write("3. สปาเก็ตตี้ผัก: ใช้สปาเก็ตตี้ที่ทำจากแป้งโฮลวีท คู่กับผักต่างๆ เช่น บรอกโคลี, มะเขือเทศ")
        st.write("4. ไก่ย่างพริกไทยดำ: ปรุงไก่ด้วยพริกไทยดำและสมุนไพรต่างๆ อย่างสับปะรดหรือมะเขือเทศ")
        st.write("5. ข้าวกล้องผัดผักรวม: ผักผลไม้ต่างๆ ผสมกับข้าวกล้อง และเติมโปรตีนจากไข่ไก่หรือไข่ไข่ไก่ขาว")
        st.markdown("")
        st.write("สูตรอาหารเพื่อสุขภาพยังมีอีก นอกจากนี้แต่ละบุคคลควรเลือกทานอาหารเหมาะสมกับตนเอง")
    def show_bmi_page(self):
        st.title("คำนวณดัชนีมวลกาย (BMI)")
        st.image(self.bmi_image_url, use_column_width=True)
        st.write("กรุณากรอกข้อมูลเพื่อคำนวณดัชนีมวลกายของคุณ")

        # Input fields for height and weight
        height = st.number_input("ส่วนสูง (เซนติเมตร)", min_value=1.0, max_value=300.0, step=0.1, format="%.1f")
        weight = st.number_input("น้ำหนัก (กิโลกรัม)", min_value=1.0, max_value=1000.0, step=0.1, format="%.1f")

        if st.button("คำนวณ"):
            # Calculate BMI
            bmi = weight / ((height / 100) ** 2)

            # Display BMI result
            st.markdown("ค่า BMI ของคุณคือ: {:.2f}".format(bmi))
            st.markdown("ผลลัพธ์ของคุณ")
            if bmi < 18.5:
                st.markdown("น้ำหนักน้อยหรือผอม")
            elif bmi < 25:
                st.markdown("ปกติ (สุขภาพดี)")
            elif bmi < 30:
                st.markdown("ท้วม (Overweight)")
            else:
                st.markdown("อ้วน (Obese)")

            # Display BMI result as a comparison with Thai BMI distribution
            fig, ax = plt.subplots()
            sns.barplot(x=list(self.thai_bmi_distribution.keys()), y=list(thai_bmi_distribution.values()), ax=ax, color='skyblue', label='Thai people')
            ax.axhline(bmi, color='red', linestyle='--', label='Your BMI')
            ax.set_ylabel("Percentage")
            ax.set_title("You vs Thai people ")
            ax.legend()
            st.pyplot(fig)

    def calculate_bmr(self,weight=None, height=None, age=None, gender=None):
        if gender == "ชาย":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return bmr
    def show_bmr_page(self):
        st.subheader("คำนวณ BMR (Basal Metabolic Rate)")
        st.markdown("")
        st.image('https://scontent.fubp1-1.fna.fbcdn.net/v/t1.6435-9/123354169_3758799590820211_5231114091774216903_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=7f8c78&_nc_eui2=AeHZlSCa5y9on58uPM3YoEDzkLnNwLiuLLmQuc3AuK4sucmWpL2K2Bg63bdnz50bjw1z9qjP6WTweADUDnk458oq&_nc_ohc=rMFAFBEBj0cAX9sXW1M&_nc_ht=scontent.fubp1-1.fna&oh=00_AfC9WGAS0Kb8FViIGEKxMeSIPeI1FmC1cxzcqrozNeWB4A&oe=660E348E')
        weight = st.number_input("น้ำหนัก (กิโลกรัม)", step=1)
        height = st.number_input("ส่วนสูง (เซนติเมตร)", step=1)
        age = st.number_input("อายุ",step=1)
        gender = st.radio("เพศ", ("ชาย", "หญิง"))
        if st.button("คำนวณ"):
            bmr = self.calculate_bmr(self,weight, height, age, gender)
            st.write("BMR (Basal Metabolic Rate): {:.2f} แคลอรี่".format(bmr))


if __name__ == "__main__":
    app = PhealthyApp()
    app.main()

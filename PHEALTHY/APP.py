import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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
            background-color: #f0f2f6;  /* Light grey background */
            color: #333333;  /* Dark grey text */
        }
        </style>
        """,
        unsafe_allow_html=True)

    # Sidebar navigation
    page = st.sidebar.selectbox("Topic", ["หน้าหลัก", "สารอาหาร", "ออกกำลังกาย", "สูตรอาหาร", "หาค่า BMI(ดัชนีมวลกาย)"])

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

def show_home_page():
    st.write("สวัสดีครับ ยินดีต้อนรับสู่ P'healthy เราเป็นเว็ปไซด์สายสุขภาพ เหมาะสำหรับใครที่อยากเริ่มที่จะดูแลสุขภาพ ")
    st.write('สิ่งที่เสียไปแล้วไม่กลับคืนมา มีเพียงเวลาและสุขภาพ')

def show_nutrition_page():
    st.write("This is the Nutrition page. Here you can find information about healthy eating habits.")

def show_exercise_page():
    st.write("This is the Exercise page. Here you can find information about different exercises and workouts.")

def show_recipes_page():
    st.write("This is the Recipes page. Here you can find healthy recipes for meals and snacks.")

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

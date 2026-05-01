import streamlit as st
import streamlit.components.v1 as components

# 1. كود إثبات الملكية لجوجل أدسنس (يجب أن يكون في البداية)
adsense_meta = """
<google.com, pub-9614186560098079, DIRECT, f08c47fec0942fa0>
"""
components.html(adsense_meta, height=0)

# 2. إعدادات الصفحة
st.set_page_config(page_title="مخطط الدايت الذكي", page_icon="⚖️")

# 3. واجهة التطبيق
st.title("🏃‍♂️ تطبيق حساب السعرات وتوقع خسارة الوزن")
st.write("أدخل بياناتك للحصول على خطة مخصصة")

# تقسيم المدخلات
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("الوزن الحالي (كجم)", min_value=30.0, max_value=250.0, value=80.0)
    height = st.number_input("الطول (سم)", min_value=100, max_value=250, value=170)
    age = st.number_input("العمر", min_value=10, max_value=100, value=25)

with col2:
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    activity = st.selectbox("مستوى النشاط البدني", 
                            ["خامل (بدون تمارين)", "نشاط خفيف", "نشاط متوسط", "نشاط عالٍ"])
    target_period = st.number_input("مدة الدايت (بالأيام)", min_value=7, max_value=365, value=30)

# معادلة BMR (Mifflin-St Jeor)
if gender == "ذكر":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

# معامل النشاط
activity_multipliers = {
    "خامل (بدون تمارين)": 1.2,
    "نشاط خفيف": 1.375,
    "نشاط متوسط": 1.55,
    "نشاط عالٍ": 1.725
}

maintenance_calories = bmr * activity_multipliers[activity]

st.divider()

# حسابات الدايت (بناءً على عجز 500 سعرة يومياً)
daily_deficit = 500 
diet_calories = maintenance_calories - daily_deficit
total_loss_kg = (daily_deficit * target_period) / 7700 

st.header("📊 النتائج المتوقعة")
c1, c2, c3 = st.columns(3)
c1.metric("سعرات المحافظة", f"{int(maintenance_calories)}")
c2.metric("سعرات الدايت", f"{int(diet_calories)}")
c3.metric("الخسارة المتوقعة", f"{total_loss_kg:.2f} كجم")

st.info(f"💡 إذا استمريت لمدة **{target_period}** يوم، يتوقع أن يصبح وزنك **{weight - total_loss_kg:.2f}** كجم.")

# 4. قسم "قيمة مضافة" لزيادة فرص قبول جوجل (نصوص مفيدة)
st.divider()
st.subheader("📝 نصائح صحية من أجل دايت ناجح")
st.write("""
*   **شرب الماء:** تأكد من شرب 2-3 لتر يومياً لتحسين عملية الأيض.
*   **البروتين:** احرص على تناول كمية كافية من البروتين للحفاظ على الكتلة العضلية.
*   **النوم:** النوم الكافي يساعد جسمك على حرق الدهون بشكل أسرع.
""")

# 5. قسم تقييم التجربة
st.divider()
st.header("📉 سجل نتائجك وقيم تجربتك")
old_weight = st.number_input("الوزن عند البداية", value=weight)
current_actual_weight = st.number_input("الوزن الحالي بعد التجربة", value=weight - 1.0)

if st.button("احسب صافي الخسارة"):
    diff = old_weight - current_actual_weight
    if diff > 0:
        st.success(f"كفو يا بطل! لقد خسرت {diff:.2f} كجم. استمر! 🔥")
    else:
        st.info("الوزن ثابت، حاول زيادة نشاطك البدني قليلاً.")

# 6. تذييل الصفحة (Footer) - مهم جداً لمتطلبات جوجل
st.markdown("---")
st.caption("حقوق النشر © 2026 - تطبيق عبدالله الذكي للصحة")

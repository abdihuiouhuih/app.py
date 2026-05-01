import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق التحديات اليومية", page_icon="🏆")

# تنسيق الواجهة لتناسب اللغة العربية
st.markdown("""
    <style>
    .main { text-align: right; direction: rtl; }
    div[data-testid="stBlock"] { direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 مدربك الشخصي للتحديات")
st.write("تابع تقدمك اليومي وحقق أهدافك!")

# استخدام الـ Session State لحفظ البيانات مؤقتاً أثناء تشغيل البرنامج
if 'challenges' not in st.session_state:
    st.session_state.challenges = [
        {"id": 1, "name": "🏃 تحدي الرياضة", "days": 30, "current": 0},
        {"id": 2, "name": "📵 ترك العادات السيئة", "days": 21, "current": 0},
        {"id": 3, "name": "📚 تحدي الدراسة", "days": 15, "current": 0}
    ]

# عرض التحديات
for idx, ch in enumerate(st.session_state.challenges):
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(ch['name'])
            # حساب النسبة المئوية للتقدم
            progress_val = ch['current'] / ch['days']
            st.progress(progress_val)
            st.write(f"التقدم: {ch['current']} من {ch['days']} يوم")
            
        with col2:
            st.write(" ") # موازنة المسافة
            if st.button(f"تم الإنجاز ✅", key=f"btn_{idx}"):
                if ch['current'] < ch['days']:
                    st.session_state.challenges[idx]['current'] += 1
                    st.rerun()
                else:
                    st.balloons()
                    st.success("أنهيت التحدي! بطل!")

        st.divider()

# إضافة تحدي جديد
with st.sidebar:
    st.header("إضافة تحدي جديد")
    new_name = st.text_input("اسم التحدي")
    new_days = st.number_input("عدد الأيام", min_value=1, value=30)
    if st.button("إضافة ➕"):
        new_id = len(st.session_state.challenges) + 1
        st.session_state.challenges.append({"id": new_id, "name": new_name, "days": new_days, "current": 0})
        st.rerun()

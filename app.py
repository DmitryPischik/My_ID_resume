from pathlib import Path
import streamlit as st
from PIL import Image

#-----Path settings------
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'summary.pdf'
profile_pic = current_dir / 'assets' / 'photo.jpg'

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Резюме | Пищик Дмитрий Александрович"
PAGE_ICON = ":wave:"
NAME = "Пищик Дмитрий Александрович"
DESCRIPTION = "Менеджер по управлению запасами."
EMAIL = " pischik@bk.ru"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Скачать резюме",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Опыт работы")
st.write(
    """
Менеджер по управлению запасами
ТД "Детские товары" (Бубль-Гум) 
С 10.01.2014 / Владивосток
1.	Расчет прогноза спроса по отдельным товарам, а также по группам товарам.
2.	Формирование прогноза продаж с учетом тренда и сезонности, а также с учетом очистки статистики продаж от дефицитов и случайных всплесков продаж, например акции.
3.	Расчет оптимального периода между поставками от внешних поставщиков.
4.	Расчет заказов внешним поставщикам с учетом существующих заказов поставщикам, страховых и презентационных запасов, периодичности поставок, текущего остатка и потребности в товарах, с учетом логистических и финансовых ограничений.
5.	Контроль движения заказов в цепочке поставок от внешних поставщиков до Магазинов.
6.	Управление параметрами снабжения магазинов.
7.	Определение и устранение причин дефицитов.
8.	Участие в составление расходной части бюджета компании.
9.	Автоматизация процессов отдела с применением VBA и Python.
10.	Получение и обработка данных из различных источников с помощью Power Query и SQL.
11.	Работа с витринами данных.

Ведущий специалист аналитического отдела.
КГУП «Примтеплоэнерго»
C 16.10.2006 по 31.12.13 / Владивосток
1.	Координация деятельности филиалов КГУП «Примтеплоэнерго» по формированию отчетности по сбытовой деятельности.
2.	Формирование сводных отчетов и их первичный анализ для руководства предприятия, администрации ПК и Приморскстата.
3.	Формирование годового плана затрат по договорам со сторонними организациями, оказывающими услугу по начислению, приему платежей и ведению лицевых счетов.  Ежемесячный сбор, свод и анализ информации по фактическому исполнению этих планов.
4.	Формирование доходной части экономического бюджета предприятия.
5.	Подготовка и анализ прогнозной информации по начислениям и оплатам для руководства предприятия.

"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Технические навыки")
st.write(
    """
- 👩‍💻 Программирование: Python (NumPy, Pandas, xlwings), SQL, VBA
- 📊 Визуализация данных: PowerBi, MS Excel, Tableau
- 📚 MS Office: Excel, Word, Access, Outlook, PowerPoin
- 🗄️ Базы данных: Postgres, Oracle
"""
)
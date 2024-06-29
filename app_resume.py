from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Paulina Mirota"
PAGE_ICON = ":wave:"
NAME = "Paulina Mirota"
DESCRIPTION = """
Passionate and detail-oriented Data Enthusiast with extensive experience in task automation using VBA, Power BI, 
and Python. Proven track record of transforming raw data into meaningful insights and driving efficiency through innovative solutions. 
Adept at designing and implementing data visualization tools to support business decision-making. 
Seeking a challenging role as a Power BI Specialist to leverage my skills in data analysis, automation, 
and visualization to contribute to the success of a forward-thinking organization.
"""
EMAIL = "pmirota1992@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/paulina-mirota-02871918b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app",
    "GitHub": "https://github.com/pmirota92/",

}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across categories": "https://github.com/pmirota92/PowerBI-SalesDashboard",
    "🏆 Salaries in the Data Science domain": "https://ds-salaries-analysis-app.streamlit.app/",
    "🏆 Analysis of the Polish Sejm IX and X Term ": "https://github.com/pmirota92/PowerBI-Polski_Sejm_IX-X",
    "🏆 SQL Solution": "https://github.com/pmirota92/SQL/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#st.sidebar.title("Curriculum Vitae")

# --- HERO SECTION ---

st.sidebar.image(profile_pic, width=300)
# --- Projects & Accomplishments ---
st.sidebar.write('\n')
st.sidebar.subheader("Projects & Accomplishments")
st.sidebar.write("---")
for project, link in PROJECTS.items():
    st.sidebar.write(f"[{project}]({link})")

# --- SKILLS ---
st.sidebar.write('\n')
st.sidebar.subheader("Hard Skills")
st.sidebar.write("---")
st.sidebar.write(
    """
- 👩‍💻 **Programming**: Python (Streamlit, Pandas), SQL, VBA
- 📊 **Data Visulization**: Power BI, MS Excel, Plotly
- 📚 **Modeling**: Logistic regression, linear regression
- 🗄️ **Databases**:  MySQL, Snowflake
- 🚀 **Other**: Power Automate, SAP
"""
)


st.title(NAME)
st.write(DESCRIPTION)
st.download_button(
    label=" 📄 Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)

st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Power BI, Python and Excel including VBA
- ✔️ Good understanding of designing, building and implementing analytical projects in Power BI
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Automation Specialist | ABB Business Services Sp. z o. o.**")
st.write("04/2022 - Present")
st.write(
    """
- ► Demonstrated proficiency in utilizing Power BI, DAX, VBA, Power Automate to develop insightful reports and analytical solutions,
- ► Regularly used Power BI and Power Automate to streamline data workflows, integrating seamlessly with database environments like Snowflake,
- ► Applied expertise in Power BI architecture and optimization techniques to enhance performance and usability,
- ► Executed ETL processes to ensure seamless data integration and transformation for analysis,
- ► Developed comprehensive visualizations to represent Key Performance Indicators (KPIs) for business processes across multiple countries, facilitating global performance tracking,
- ► SQL, used for querying databases and optimizing data retrieval processes,
- ► Exhibited analytical thinking skills to tackle complex challenges and provide innovative solutions,
- ► Translated client requirements into technical solutions with precision and accuracy,
- ► Excelled in organizing and managing own work effectively, ensuring timely delivery of projects,
- ► Conducted a comprehensive training session on Power BI.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Financial Analyst | International Paper Global Business Service Center** (cash flows, working capital and automation specialist)")
st.write("10/2019 - 03/2022")
st.write(
    """
- ► Prepared recurring and ad hoc reports to support business decision-making,
- ► Participated in developing new reporting methods and redesigning existing processes using VBA, Blue Prism, and Power BI (including writing DAX queries and creating visualizations),
- ► Executed month-end, quarter-end, and year-end closing activities accurately and efficiently,
- ► Analyzed financial data to identify trends and provide actionable insights for improving cash flow and working capital management,
- ► Automated routine financial tasks and processes, enhancing efficiency and reducing manual errors.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Accountant in Accounts Payable Department | Philip Morris International SCE**")
st.write("03/2016 - 09/2019")
st.write(
    """
- ► Verified documents in compliance with tax regulations,
- ► Posted PO, non-PO invoices in the SAP ERP and SIRIUS,
- ► Performed accounts reconciliation and prepared financial reports,
- ► Managed email and phone queries, maintaining regular relationships with internal and external clients,
- ► Created and implemented VBA macros to streamline processes,
- ► Developed test cases and scenarios for the created macros.
"""
)




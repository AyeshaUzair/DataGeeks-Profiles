import streamlit as st
import base64
import pandas as pd


main_bg = "image10.jpg"
main_bg_ext = "jpg"
side_bg = "image9.jpg"
side_bg_ext = "jpeg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

template = """<div style = 'background-color:#17186e; padding: 1px;'>
                <h2 style = 'color:white; text-align:center;'>Data Geeks - Team Portfolios</h2>
            </div>"""
st.markdown(template, unsafe_allow_html=True)

st.sidebar.title("Member Profiles")
dropdown = st.sidebar.selectbox("Select member to view profile", ["Ayesha Uzair", "Rebecca Palmer", "Nadia Vermaes"])

if dropdown == "Ayesha Uzair":
    st.title("Ayesha Uzair")
    st.sidebar.image("Ayesha.PNG", width=300)
    x = st.sidebar.radio("Select option to view details", ["About", "Experience", "Education", "Skills", "Contact"])
    if x == "About":
        st.write("Hello, I am Ayesha from the Data Geeks Team. :sunglasses:")
        st.write("I'm an algorithm developer with 3+ years of work experience in software solution design and network "
                 "operations. I possess good programming skills in Python, Javascript, C++, and MATLAB. "
                 "My core areas of expertise are signal processing, mobile communications, machine learning, and "
                 "algorithm and software development.")
        st.write("Currently, I am a student of AI/ML Bootcamp organized by The Code to Change.")
        st.markdown("""<a href="https://www.linkedin.com/in/ayesha-uzair/">Linkedin</a>""", unsafe_allow_html=True, )
        st.markdown("""<a href="https://github.com/AyeshaUzair">Github</a>""", unsafe_allow_html=True, )

    if x == "Experience":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Dates")
            "Jul 2020 - Present"
            "Jul 2019 - Feb 2020"
            "Sep 2016 - Apr 2017"
            "Oct 2015 - Sep 2016"
            "Oct 2014 - Jun 2015"

        with col2:
            st.subheader("Company")
            "Narda Safety Test Solutions"
            "IHF"
            "Telenor"
            "Telenor"
            "Mobilink (Jazz)"

        with col3:
            st.subheader("Designation")
            "Associate Software Engineer"
            "Master Thesis Student"
            "CBS Solutions Officer"
            "Network Management Officer"
            "RAN Planning Intern"

    if x == "Education":
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader("Dates")
            "Oct 2021 - Present"
            "Oct 2017 - Mar 2020"
            "Sep 2010 - Jun 2014"

        with col2:
            st.subheader("Company")
            "The Code 2 Change"
            "RWTH Aachen"
            "NUST"

        with col3:
            st.subheader("Country")
            "Netherlands"
            "Germany"
            "Pakistan"

        with col4:
            st.subheader("Degree")
            "Data Science Bootcamp"
            "M.Sc. Information Tech."
            "B.Sc. Electrical Engg."

    if x == "Contact":
        st.subheader("Contact Info: ")
        st.write("**Address:** Aachen, Germany")
        st.write("**Phone:** +49 17677583321")
        st.write("**Email:** ayesha.shafqat92@gmail.com")
        st.subheader("Feel free to leave a message:")
        with st.form("Contact Form:"):
            a = st.text_input("Enter your name")
            print(a)
            b = st.text_input("Subject")
            c = st.text_input("Email")
            d = st.text_input("Message")
            bt = st.form_submit_button(label="Submit")
            if a is None:
                st.error("Please enter your name.")
            if c is None:
                st.error("Please enter your email.")
            if bt:
                st.success("Your message has been sent to Ayesha.")
                st.balloons()


if dropdown == "Rebecca Palmer":
    st.title("Rebecca Palmer")
    st.sidebar.image("Rebecca_full.jpg", width=300)
    # x = st.sidebar.radio("Select Option",["About", "Experience", "Education", "Skills", "Contact"])
    st.header("Work Experience")
    col1, col2, col3 = st.columns(3)
    with col1:
        "Dates"
        "Oct 2018 - Present"
        "Aug 2016 - Oct 2018"
        "Sep 2013 - Aug 2016"
        "Jun 2011 - Aug 2013"
        "Nov 2005 - Jun 2011"
        "Aug 2004 - Nov 2005"
        "Nov 2003 - Jul 2004"
        "Mar 2003 - Nov 2003"

    with col2:
        "Company"
        "Irdeto"
        "Irdeto"
        "Irdeto"
        "Irdeto"
        "Irdeto"
        "Witter Towbars Ltd"
        "Mitras Automotive"
        "Oxford Conversis"
    with col3:
        "Position"
        "Sales Operations Manager"
        "Manager, Sales Support"
        "Manager, Business Services EMEA"
        "Senior Commercial Co-ordinator"
        "Sales Support Administrator"
        "Sales Co-ordinator"
        "Sales & Marketing Co-ordinator"
        "Administrator"
    st.header("Education")
    df_education = pd.read_csv("education_rebecca.csv")
    df_education.set_index('From')
    st.table(df_education)
    st.header("Personal")
    st.text("British citizen based in the Netherlands with work/residence permit and full driving licence")
    st.text("Experienced in all aspectes of sales operations including sales incentive administration, "
            "sales forecasting etc.")

if dropdown == "Nadia Vermaes":
    st.title("Nadia Vermaes")

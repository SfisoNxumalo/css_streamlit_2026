import streamlit as st

def show_developer_details():

    st.set_page_config(
        page_title="About Me | Sifiso Mawila",
        page_icon="👨🏽‍💻",
        layout="wide"
    )

    # ------------------ CUSTOM CSS ------------------
    st.markdown("""
    <style>
    .profile-card {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        padding: 2rem;
        border-radius: 16px;
        color: white;
    }
    .skill-chip {
        display: inline-block;
        padding: 6px 12px;
        margin: 4px;
        border-radius: 20px;
        background-color: #eef2f7;
        font-size: 14px;
    }
    .section-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 14px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

    # ------------------ HEADER ------------------
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "sfisomawila_resized.jpg",  # replace with your image or URL
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="profile-card">
            <h1>Sifiso Mawila</h1>
            <h3>Junior Software Developer</h3>
            <p>
            Hi, I’m Sifiso. I enjoy building secure full-stack applications. I consider myself tech-agnostic; however, my current tech stack includes C#, .NET, React, and SQL Server. I’m currently exploring the nitty-gritty of the data science world. 
            </p>
            <p>📍 Johannesburg, South Africa</p>
            <p>
                <a href="https://www.linkedin.com/in/sifiso-mawila-1b888a224/" style="color:#7dd3fc;">LinkedIn</a> |
                <a href="https://github.com/SfisoNxumalo" style="color:#7dd3fc;">GitHub</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ------------------ METRICS ------------------
    st.markdown("### Quick Overview")
    m1, m2, m3 = st.columns(3)

    m1.metric("Experience", "1+")
    m2.metric("Cloud Platforms", "Azure")
    m3.metric("Certifications", "4 Microsoft")
    # m4.metric("Achievements", "SATNAC 2025 Winner")

    # ------------------ TABS ------------------
    tabs = st.tabs(["🎓 Education", "🧠 Skills", "🏆 Achievements"])

    with tabs[0]:
        st.markdown("""
        <div class="section-card">
            <h3>Education</h3>
            <ul>
                <li><b>Postgraduate Diploma in Information Technology | 2025</b><br/>Cape Peninsula University of Technology | 2025</li>
                <b>Relevant Coursework</b>
                <p>
                Software Engineering, Database Management, AI, Data Science, 
                Computational Mathematics, Capstone Project, Research Methods
                </p>
                <li><b>Advanced Diploma in Information Technology | 2024</b> – <i>Graduated with Distinction</i><br/>Cape Peninsula University of Technology | 2024</li>
                <li><b>Diploma in Systems Development | 2022</b><br/>Boston City Campus</li>
            </ul>

            
        </div>
        """, unsafe_allow_html=True)

    # ------------------ SKILLS ------------------
    with tabs[1]:
        st.markdown("""
        <div class='section-card'>
            <h3>Technical Skills</h3>
            <p><b>Programming Languages:</b> C#, Java, JavaScript, TypeScript, Python, SQL</p>
            <p><b>Frameworks:</b>
            ASP.NET Core, EF Core, React, Angular, Express.js, Flutter
            </p>
            <p><b>Cloud & DevOps:</b>
            Microsoft Azure, AWS, Azure DevOps, GitHub Actions, Docker, Bicep
            </p>
            <p><b>Databases:</b>
            SQL Server, MySQL, MongoDB, Firebase, Snowflake
            </p>
            <p><b>Architecture:</b>
            Onion Architecture, Microservices, MVC
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ------------------ ACHIEVEMENTS ------------------
    with tabs[2]:
        st.markdown("""
        <div class="section-card">
            <h3>🏆 Achievements</h3>
            <ul>
                <li>
                    <b>🥇 1st Place – SATNAC Industry Challenge 2025</b><br/>
                    Developed an ML model to assess EV charging site viability
                    using geospatial and operational data for Openserve.
                </li>
                <li>
                    🎓 Graduated with Distinction (81%) – Advanced Diploma in IT
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # ------------------ FOOTER ------------------
    st.markdown("---")

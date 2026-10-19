import streamlit as st
from PIL import Image
from streamlit.components.v1 import html

# Page config
st.set_page_config(page_title="Raghavendra Rongali", page_icon="💼", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitle {
            font-size: 1.5em;
            color: #16a085;
        }
        .section-title {
            font-size: 1.3em;
            margin-top: 30px;
            margin-bottom: 10px;
            color: #2980b9;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            margin-top: 50px;
            color: #95a5a6;
        }
        .card {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Info
st.sidebar.image("My photo official.jpg", width=150)
st.sidebar.title("Raghavendra Rongali")
st.sidebar.markdown("**Role:** Senior Associate")
st.sidebar.markdown("📍 Visakhapatnam, India")
st.sidebar.markdown("📫 [Email](mailto:raghavendra95550@gmail.com)")
st.sidebar.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/raghavendra-rongali-90827013a/)")
st.sidebar.markdown("🐙 [GitHub](https://github.com/raghava95550)")

# Main content
st.markdown("<div class='main-title'>Hello, I'm Raghavendra Rongali</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Senior Software Engineer | Full Stack Developer | AI Enthusiast</div>", unsafe_allow_html=True)

st.markdown("""<div class='section-title'>🧑‍💼 About Me</div>
Results-driven AI/LLM Engineer with 5+ years of software engineering experience, specializing in
designing, building, and deploying production-grade applications, AI chatbots, LLM API integrations,
and Snowflake Cortex Agent workflows. Highly proficient in GitHub Copilot-driven
development—leveraging it for ~80% of code generation—and advanced prompt engineering to build
scalable enterprise solutions. Actively upskilling and expanding practical competencies in RAG pipelines,
LangChain, LangGraph, Agent-to-Agent (A2A) protocols, and Model Context Protocol (MCP) through
hands-on LLM API integrations. Proven track record in microservices development using Spring Boot,
with extensive experience in AWS Cloud infrastructure, LLM observability, and end-to-end CI/CD in
global environments.

I have a proven track record of leading full product lifecycles—from technical design to production deployment—within Agile teams. I'm currently deepening my knowledge in Generative AI, working with LLM-based applications, Retrieval-Augmented Generation (RAG) frameworks, and rapid ML prototyping using Python.
I'm passionate about blending strong software engineering practices with AI-driven innovation, aiming to deliver intelligent, resilient systems in modern cloud environments.

<div class='section-title'>🧠 Skills</div>""", unsafe_allow_html=True)
st.markdown("""
- **Backend Development:** Java, J2EE, Spring Boot, REST APIs, Hibernate
- **Distributed Systems & Cloud:** Microservices Architecture, Docker, Kubernetes, AWS(EC2, Lambda, S3, RDS)
- **Databases:** Oracle SQL, PL/SQL, Snowflake, MySQL, MongoDB
- **GenAI & ML (In Progress):** Python, LLM Agents (OpenAI, LangChain), RAG Pattern,OpenCV, Jupyter Notebook
- **DevOps & CI/CD:** Jenkins, Spinnaker, GitHub Actions, Git, Bitbucket
- **Frontend:** Angular, TypeScript, HTML/CSS
- **Agile & SDLC:** Scrum, Kanban, JIRA
- **Other Tools:** Eclipse, VS Code, Postman, Swagger
""")

st.markdown("<div class='section-title'>💼 Experience</div>", unsafe_allow_html=True)
st.markdown("""
**Sr. Software Engineer** – Zensar Technologies (Nov 2020 - Present)  
- Backend System Design & Optimization: Developed and maintained robust, scalable backend systems using Java Spring Boot to support high-traffic applications, ensuring minimal downtime and optimal performance.  
✿ **API Development:** Led the design and implementation of RESTful APIs using Java Spring Boot and AWS Lambda, improving system performance by reducing API response times by 25%.  
✿ **Cloud Integration:** Integrated cloud-native solutions by developing AWS Lambda functions and using AWS API Gateway to improve the scalability of web services and reduce infrastructure costs.  
✿ **Database Management:** Worked with Snowflake and Oracle for data storage and optimized database queries to handle large datasets efficiently.  
✿ **Mentorship & Code Review:** Mentored junior developers and conducted code reviews to ensure adherence to coding standards and best practices, improving overall code quality and team efficiency.  
✿ **Troubleshooting:** Diagnosed and resolved issues related to backend system performance, optimizing Java garbage collection and database connection handling to reduce latency and increase throughput.  
""")


st.markdown("<div class='section-title'>📂 Projects</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
    <b>CO Problem Backlog Management</b><br>
    Developed an AI-enabled Intelligent Intake Submission Form leveraging Snowflake Cortex
    Agent and Python LLM APIs, utilizing GitHub Copilot to accelerate ~80% of development and
    code generation for auto-enhancing problem titles, descriptions, and proposed resolutions.
    Built duplicate-problem detection workflow leveraging advanced prompt engineering and
    Snowflake Cortex semantic capabilities.
    Established prompt engineering standards and tool-calling integrations between front-end UI (Angular),
    Python FastAPI, LLM APIs, and core database layers.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
    <b>Partner Operational Readiness Assessment (PORA)</b><br>
    Developed a scalable application to assess partner readiness for software and licensing operations. Integrated AWS Lambda for serverless backend functions and implemented dynamic localization in 8 languages using Google Cloud Translate API
    </div>
    """, unsafe_allow_html=True)



with col2:
    st.markdown("""
    <div class='card'>
    <b>BPLO True Forward Tracker</b><br>
     Developed and deployed a customer data management system to update customer data through responsive UI screens, using Java Spring Boot and AWS Elastic Beanstalk.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
    <b>Customer Scope Definition</b><br>
     It is an application designed to create definitions by searching for values and retrieving the results. The application includes all features such as creating, editing, and downloading definitions
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
    <b>Anomaly Detection in Traffic Videos</b><br>
    Built a machine learning model to detect anomalous activities from traffic surveillance videos. Utilized Python, OpenCV, and HDP for video frame processing and anomaly detection.
    </div>
    """, unsafe_allow_html=True)
st.markdown("### 📄 Resume")
resume_url = "https://drive.google.com/uc?export=download&id=1mPvCKPWHFk-fg5uevW3i9TWVpeyz3uAn"
st.markdown(f"[👉 Download My Resume (PDF)]({resume_url})", unsafe_allow_html=True)

st.markdown("<div class='section-title'>📞 Contact</div>", unsafe_allow_html=True)
st.markdown("""
- Email: raghavendra95550@gmail.com
- LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/raghavendra-rongali-90827013a/)
- GitHub: [github.com/yourprofile](https://github.com/raghava95550)
""")

st.markdown("<div class='footer'>© 2025 Raghavendra Rongali | Powered by Streamlit</div>", unsafe_allow_html=True)

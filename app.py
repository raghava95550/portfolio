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
st.sidebar.image("https://drive.google.com/file/d/1k4oxtWETMRqhSpaa5eBBcXC6UpSuhcwH/view?usp=sharing", width=120)
st.sidebar.title("Raghavendra Rongali")
st.sidebar.markdown("**Role:** Senior Software Engineer")
st.sidebar.markdown("📍 Visakhapatnam, India")
st.sidebar.markdown("📫 [Email](mailto:raghavendra95550@gmail.com)")
st.sidebar.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/raghavendra-rongali-90827013a/)")
st.sidebar.markdown("🐙 [GitHub](https://github.com/raghava95550)")

# Main content
st.markdown("<div class='main-title'>Hello, I'm Raghavendra Rongali</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Senior Software Engineer | Full Stack Developer | AI Enthusiast</div>", unsafe_allow_html=True)

st.markdown("""<div class='section-title'>🧑‍💼 About Me</div>
I'm a Senior Java Developer with over 4 years of experience architecting and delivering high-performance, cloud-native enterprise applications using Java, Spring Boot, and microservices architecture. I specialize in building scalable, fault-tolerant distributed systems and integrating with Oracle SQL, with deployment expertise in Docker/Kubernetes on AWS.

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
    <b>Partner Operational Readiness Assessment (PORA)</b><br>
    Built with NLP and cosine similarity to recommend relevant articles.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <b>BPLO True Forward Tracker</b><br>
    Implemented using BLIP model and HuggingFace Transformers.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <b>Customer Scope Definition</b><br>
    Analyzed and predicted temperature fluctuations using Random Forest.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <b>Anomaly Detection in Traffic Videos</b><br>
    Built using Streamlit to showcase my work.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='section-title'>📞 Contact</div>", unsafe_allow_html=True)
st.markdown("""
- Email: raghavendra95550@gmail.com
- LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/raghavendra-rongali-90827013a/)
- GitHub: [github.com/yourprofile](https://github.com/raghava95550)
""")

st.markdown("<div class='footer'>© 2025 Raghavendra Rongali | Powered by Streamlit</div>", unsafe_allow_html=True)

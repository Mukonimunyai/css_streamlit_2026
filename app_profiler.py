import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Mukoni Monyai"
field = "Numerical optimization"
institution = "Sefako Makgatho Health Sciences University"

import streamlit as st

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Monyal Mukoni | Mathematics CV",
    page_icon="📘",
    layout="wide"
)

# --------------------------------------------------
# Custom styling (decorations)
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}
.section {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
.title {
    color: #1f2937;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header section
# --------------------------------------------------
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/7/7e/Blackboard_with_equations.jpg",
        caption="Mathematics & Analytical Thinking",
        use_container_width=True
    )

with col2:
    st.markdown("""
    <div class="section">
        <h1 class="title">Monyal Mukoni</h1>
        <h3>Honours Mathematics Student</h3>
        <p>
        📧 <b>Email:</b> mukonimunyai@gmail.com <br>
        
      
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Profile
# --------------------------------------------------
st.markdown("""
<div class="section">
<h2>👤 Profile</h2>
<p>
I am an Honours Mathematics student with a strong analytical mindset and a careful,
structured approach to problem-solving. Experience tutoring students and working
as an examination assistant has strengthened my ability to communicate clearly,
maintain consistency, and ensure precision when reviewing academic material.
</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Education
# --------------------------------------------------
st.markdown("""
<div class="section">
<h2>🎓 Education</h2>

<b>Bachelor of Science (Honours) in Mathematics</b><br>
Sefako Makgatho Health Sciences University — <i>2025</i><br><br>

<b>Bachelor of Science (Physical Sciences)</b><br>
Sefako Makgatho Health Sciences University — <i>2021–2024</i><br><br>

<b>Relevant Modules:</b>
<ul>
<li>Mathematical Analysis</li>
<li>Complex Analysis</li>
<li>Linear Algebra</li>
<li>Thermodynamics and Electronics</li>
<li>Quantum Mechanics</li>
<li>Solid State Physics</li>
</ul>

<b>Matric:</b> Eqinisweni Secondary School (2015–2019)
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Work Experience
# --------------------------------------------------
st.markdown("""
<div class="section">
<h2>💼 Work Experience</h2>

<b>Examination Assistant (Quality Assurer)</b><br>
Department of Education, Gauteng<br>
<i>25 November 2024 – 18 December 2024</i>

<ul>
<li>Verified accuracy and integrity of examination results</li>
<li>Ensured scripts were fully marked and marks correctly transferred</li>
<li>Identified discrepancies to ensure fairness and consistency</li>
<li>Worked efficiently in a high-pressure environment</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Skills
# --------------------------------------------------
st.markdown("""
<div class="section">
<h2>🧠 Key Skills & Characteristics</h2>

<ul>
<li><b>Self-Motivation & Discipline</b></li>
<li><b>Attention to Detail & Precision</b></li>
<li><b>Critical Thinking & Analytical Reasoning</b></li>
<li><b>Communication & Teamwork</b></li>
<li><b>Time Management</b></li>
</ul>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "<center>© 2026 | Mathematics CV • Built with Streamlit</center>",
    unsafe_allow_html=True
)

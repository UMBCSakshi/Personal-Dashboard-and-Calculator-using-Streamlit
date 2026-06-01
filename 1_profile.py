import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Sakshi Jaju | Profile", page_icon="🎨", layout="wide")

# Main Header Area
col1, col2 = st.columns([1, 3])

with col1:
    # A placeholder for your profile picture/avatar
    st.markdown("### 👩‍💻") 

with col2:
    st.title("Sakshi Jagdish Jaju")
    st.subheader("UI/UX & Branding Designer | Content Creator sakshi_jaju19")
    st.caption("📍 Baltimore, MD | Graduate Student Worker @ UMBC")

st.divider()

# Left Column: Bio & Education | Right Column: Skills & Experience
left_col, right_col = st.columns([2, 1.5])

with left_col:
    st.markdown("### About Me")
    st.write(
        "I am a passionate Human-Centered Computing graduate student at the University of Maryland, Baltimore County (UMBC), "
        "focusing on UI/UX design, visual hierarchy, and creating deeply user-focused digital experiences. "
        "When I'm not designing high-fidelity prototypes, I manage **sakshi.guides**, where I strategize content "
        "and share actionable insights about career growth, web design, and UI/UX."
    )
    
    st.markdown("### Education")
    st.markdown(
        "**M.S. in Human-Centered Computing**  \n"
        "*University of Maryland, Baltimore County (UMBC)*  \n"
        "Specialization in Human-Computer Interaction & User-Centric Design"
    )

    st.markdown("### Recent Milestones")
    st.markdown("- **AI+ Expo Exhibitor (D.C.):** Showcased a custom-built AI Chatbot project.")
    st.markdown("- **DDX Innovation & UX Conference:** Awarded departmental travel funding to attend in NYC.")

with right_col:
    st.markdown("### Core Toolkit")
    
    st.markdown("**Design & Prototyping**")
    st.code("Figma, Canva, Adobe Creative Suite, Scalable Design Systems", language="text")
    
    st.markdown("**Content & Video Editing**")
    st.code("Edits, CapCut, VN Video Editor, Social Media Strategy", language="text")
    
    st.markdown("**Productivity & AI Tools**")
    st.code("Notion, ChatGPT, Microsoft Teams", language="text")
    
    # Simple metric dashboard stats for your content channel
    st.markdown("### Brand Impact")
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric(label="Brand Platform", value="https://sakshiguides.framer.website/")
    with metric_col2:
        st.metric(label="Focus", value="UI/UX & Career")
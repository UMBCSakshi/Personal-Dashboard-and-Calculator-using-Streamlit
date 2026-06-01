import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Design & Content Dashboard", page_icon="📊", layout="wide")

st.title("Performance & Project Dashboard")
st.markdown("Track content creation analytics and active UI/UX design sprints.")

st.divider()

# --- SECTION 1: CONTENT CREATION METRICS (sakshi.guides) ---
st.header("https://sakshiguides.framer.website/ Engagement Analytics")

# Top-level KPI metrics
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric(label="Total Reels Edited", value="42", delta="+5 this month")
kpi2.metric(label="Avg. Engagement Rate", value="8.4%", delta="+1.2%")
kpi3.metric(label="Video Retention Rate", value="68%", delta="稳定")
kpi4.metric(label="Top Platform-Native Tool", value="CapCut")

st.write("")

# Sample chart data for video performance over time
chart_data = pd.DataFrame({
    'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'],
    'UI/UX Tips Views': [1200, 1500, 2300, 2100, 3400, 4100],
    'Career Guides Views': [900, 1100, 1700, 1600, 2800, 3900]
})
chart_data.set_index('Week', inplace=True)

# Display a line chart tracking your two main content pillars
st.subheader("Video Views Growth by Content Pillar")
st.line_chart(chart_data)

st.divider()

# --- SECTION 2: UI/UX PROJECT TRACKER ---
st.header("🎨 Active UI/UX Design Sprints")

# Filter by project status using a sidebar or selectbox
status_filter = st.selectbox("Filter Projects by Status:", ["All Projects", "In Progress", "Completed", "Review Phase"])

# Hardcoded project data mimicking your Notion workflow
projects = [
    {"Project Name": "AI ChatBot Expo Interface", "Toolkit": "Figma, Canva", "Status": "Completed", "Deadline": "May 2026"},
    {"Project Name": "DDX Conference Presentation Deck", "Toolkit": "Figma", "Status": "In Progress", "Deadline": "June 2026"},
    {"Project Name": "Portfolio Case Studies Redesign", "Toolkit": "Figma, Notion", "Status": "Review Phase", "Deadline": "July 2026"},
    {"Project Name": "Short-Form Video Style Guide v2", "Toolkit": "CapCut, VN Editor", "Status": "In Progress", "Deadline": "Ongoing"}
]

df_projects = pd.DataFrame(projects)

# Apply filter logic
if status_filter != "All Projects":
    df_projects = df_projects[df_projects["Status"] == status_filter]

# Display the data frame cleanly
st.dataframe(df_projects, use_container_width=True)

# Interactive Quick Add for a mock project management sync
st.subheader("Quick Add New Sprint Task")
with st.form("new_project_form"):
    new_name = st.text_input("Task/Project Name")
    new_tools = st.text_input("Tools Needed (e.g., Figma, CapCut)")
    new_status = st.selectbox("Initial Status", ["In Progress", "Review Phase"])
    
    submit_button = st.form_submit_button("Log Task to Dashboard")
    if submit_button:
        st.success(f"Successfully logged '{new_name}'! (Data will reset on page refresh unless connected to a database).")
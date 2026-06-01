# Performance & Project Dashboard
A custom, data-driven web application built using Python and Streamlit to monitor content creation analytics, track active UI/UX design sprints, and manage functional utility tools.
This dashboard unifies visual design metrics and backend data processing into a centralized interface, bridging the gap between user experience and engineering.
---

## Features

### 1. Engagement Analytics Tracker
* Displays key performance indicators including total videos edited, average engagement rates, and video retention percentages.
* Integrates automated delta indicators to highlight monthly and weekly growth trends.
* Tracks primary platform-native tools utilized across content pipelines.

### 2. Video Views Growth by Content Pillar
* Features a dynamic line chart tracking audience engagement over a multi-week timeline.
* Segregates data trends into distinct content pillars, specifically mapping Career Guides and UI/UX Tips view counts.

### 3. Integrated Loan Calculator
* Features a standalone financial calculator component within the application.
* Handles reactive user input states and math logic directly through the Streamlit backend.

---

## Tech Stack
* **Framework:** Streamlit (for UI layout and interactive web component rendering)
* **Programming Language:** Python
* **Data Processing:** Pandas / NumPy (for metrics computation and time-series structuring)
* **Data Visualization:** Plotly / Matplotlib (for rendering the interactive line graphs)

---

## Getting Started

### Prerequisites
Ensure you have Python installed on your local system. You will also need `pip` to install the required packages.

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name

```

```

2. Install the required dependencies:
   ```bash
pip install streamlit pandas matplotlib plotly

```

### Running the Application

To launch the dashboard locally, execute the following command in your terminal:

```bash
streamlit run app.py

```

Once running, open your local browser and navigate to the address displayed in your terminal (typically `http://localhost:8501`, as displayed in image_c624a1.png).

---

## Project Structure

```text
├── app.py              # Main Streamlit application entry point
├── requirements.txt    # List of required Python packages
├── README.md           # Project documentation
└── data/               # Local data files for analytics tracking (if applicable)

```

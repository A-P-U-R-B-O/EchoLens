"""
🦠 EchoLens - AI Pandemic Predictor
Sleek Streamlit Dashboard with Groq API

Run: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from groq_client import EchoLensAI
import json
from datetime import datetime

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="EchoLens - AI Pandemic Predictor",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS - SLEEK MODERN DESIGN
# ============================================================================

st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    /* Risk Score Gauge */
    .risk-gauge {
        text-align: center;
        padding: 2rem;
        background: white;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    /* Prediction Box (Outer Header) */
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }
    
    /* Info Cards (Historical/Quick Risk Wrapper) */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    
    .info-card h3 {
        color: #667eea;
        margin-top: 0;
    }
    
    /* Analysis Text Container (AI Response Wrapper) */
    .analysis-text {
        background: white; /* Result background color set to white */
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        line-height: 1.8;
        margin: 1rem 0;
        color: #333333; /* FIX: Force text color to black/dark gray */
    }

    /* Streamlit components inside custom divs should also be dark */
    .analysis-text * {
        color: #333333;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Historical Data Cards */
    .pandemic-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: white;
        font-weight: 500;
    }
    
    /* Footer */
    .custom-footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 2px solid #eee;
        color: #666;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 8px;
        font-weight: 600;
    }
    
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER
# ============================================================================

st.markdown("""
<div class="main-header">
    <h1>🦠 EchoLens</h1>
    <p>AI-Powered Pandemic Prediction System</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">
        Trained on Black Death • Spanish Flu • SARS • COVID-19
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR - INPUT CONTROLS
# ============================================================================

with st.sidebar:
    st.markdown("### 🎛️ Prediction Controls")
    st.markdown("---")
    
    # Region input
    region = st.text_input(
        "🌍 Geographic Region",
        value="Southeast Asia",
        help="Enter the region you want to analyze",
        placeholder="e.g., Southeast Asia, Europe, North America"
    )
    
    # Current cases
    current_cases = st.number_input(
        "🔢 Active Cases",
        min_value=0,
        value=1500,
        step=100,
        help="Number of confirmed active cases in the region"
    )
    
    # Forecast period
    forecast_days = st.select_slider(
        "📅 Forecast Period",
        options=[30, 60, 90, 120, 180],
        value=90,
        help="Number of days to forecast"
    )
    
    st.markdown("---")
    
    # Predict button
    predict_btn = st.button(
        "🔮 Generate Prediction",
        use_container_width=True,
        type="primary"
    )
    
    st.markdown("---")
    
    # Info
    st.markdown("### ℹ️ About")
    st.info("""
    **EchoLens** uses advanced AI to predict pandemic outbreaks by analyzing historical epidemic patterns.
    
    **Powered by:** Groq API  
    **Model:** openai/gpt-oss-120b (Note: This is a Groq-hosted open-source model)
    """)
    
    st.markdown("---")
    st.markdown("**Built by** [@A-P-U-R-B-O](https://github.com/A-P-U-R-B-O)")
    st.markdown(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}")

# ============================================================================
# MAIN CONTENT
# ============================================================================

# Initialize AI client
try:
    ai = EchoLensAI()
except ValueError as e:
    st.error(str(e))
    st.info("""💡 **Setup Instructions:**
    
1. Get free API key from [console.groq.com](https://console.groq.com)
2. Create a `.env` file in project root
3. Add: `GROQ_API_KEY=your_key_here`
4. **Fix Dependencies:** Run `pip install httpx==0.27.2` to resolve the `TypeError: proxies` issue.
5. Restart the app
    """)
    st.stop()


# Full Prediction
if predict_btn:
    st.markdown("---")
    st.markdown("## 🔮 Detailed Prediction Analysis")
    
    # Progress indicator
    progress_text = st.empty()
    progress_bar = st.progress(0)
    
    progress_text.text("🤖 Initializing AI analysis...")
    progress_bar.progress(20)
    
    try:
        progress_text.text("📊 Analyzing historical patterns...")
        progress_bar.progress(40)
        
        # Get prediction
        prediction = ai.predict_outbreak(region, current_cases, forecast_days)
        
        progress_text.text("🎯 Generating insights...")
        progress_bar.progress(80)
        
        # Clear progress
        progress_bar.progress(100)
        progress_text.empty()
        progress_bar.empty()
        
        # ========================================================================
        # DISPLAY RESULTS
        # ========================================================================
        
        # Display full prediction in a nice box
        st.markdown(f"""
        <div class="prediction-box">
            <h2 style="margin-top: 0;">📈 Prediction Results for {region}</h2>
            <p style="opacity: 0.9;">Forecast Period: {forecast_days} days | Active Cases: {current_cases:,}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Main prediction content
        with st.container():
            st.markdown("### 🎯 AI Analysis")
            
            # FIX: Use HTML for outer container, st.markdown for content
            st.markdown('<div class="analysis-text">', unsafe_allow_html=True)
            st.markdown(prediction) # Render markdown/LaTeX correctly
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Visual metrics
        st.markdown("---")
        st.markdown("### 📊 Visual Analytics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        st.caption("Note: Metric values below are currently hardcoded; they need to be dynamically parsed from the AI response.")
        
        with col1:
            st.markdown("""
            <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                <div class="metric-label">Risk Score</div>
                <div class="metric-value">72</div>
                <div class="metric-label">High Risk</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
                <div class="metric-label">30-Day Probability</div>
                <div class="metric-value">45%</div>
                <div class="metric-label">Moderate</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
                <div class="metric-label">60-Day Probability</div>
                <div class="metric-value">67%</div>
                <div class="metric-label">Elevated</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="metric-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
                <div class="metric-label">90-Day Probability</div>
                <div class="metric-value">78%</div>
                <div class="metric-label">High</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Risk Gauge Chart
        st.markdown("---")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Note: Hardcoded value 72 used below
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=72, 
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Overall Risk Score", 'font': {'size': 24}},
                delta={'reference': 50, 'increasing': {'color': "red"}},
                gauge={
                    'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                    'bar': {'color': "darkblue"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, 30], 'color': '#43e97b'},
                        {'range': [30, 70], 'color': '#fee140'},
                        {'range': [70, 100], 'color': '#f5576c'}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90
                    }
                }
            ))
            
            fig.update_layout(
                height=300,
                margin=dict(l=20, r=20, t=50, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font={'color': "darkblue", 'family': "Inter"}
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Probability trend (Note: Hardcoded values 45, 67, 78 used below)
            fig2 = go.Figure()
            
            fig2.add_trace(go.Scatter(
                x=[30, 60, 90],
                y=[45, 67, 78],
                mode='lines+markers',
                name='Outbreak Probability',
                line=dict(color='#667eea', width=3),
                marker=dict(size=12, color='#764ba2')
            ))
            
            fig2.update_layout(
                title="Outbreak Probability Trend",
                xaxis_title="Days",
                yaxis_title="Probability (%)",
                height=300,
                margin=dict(l=20, r=20, t=50, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font={'family': "Inter"}
            )
            
            st.plotly_chart(fig2, use_container_width=True)
        
        # Historical Comparison
        st.markdown("---")
        st.markdown("### 🔍 Historical Pattern Comparison")
        
        with st.spinner("🤖 Comparing to historical pandemics..."):
            comparison = ai.analyze_comparison(f"Region: {region}, Cases: {current_cases}")
            
            # FIX: Use HTML for outer container, st.markdown for content
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.markdown('<h3>📚 Historical Analysis</h3>', unsafe_allow_html=True)
            st.markdown('<div class="analysis-text">', unsafe_allow_html=True)
            st.markdown(comparison) # Render markdown/LaTeX correctly
            st.markdown('</div></div>', unsafe_allow_html=True)
        
        st.success("✅ Full prediction analysis complete!")
        
        # Download report
        st.markdown("---")
        report_content = f"""EchoLens Prediction Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC

Region: {region}
Active Cases: {current_cases:,}
Forecast Period: {forecast_days} days

=== PREDICTION ===
{prediction}

=== HISTORICAL COMPARISON ===
{comparison}

---
Built by @A-P-U-R-B-O
Powered by Groq API (Llama 3.1 70B)
"""
        
        st.download_button(
            label="📥 Download Prediction Report",
            data=report_content,
            file_name=f"echolens_report_{region.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )
        
    except Exception as e:
        progress_text.empty()
        progress_bar.empty()
        st.error(f"❌ Error generating prediction: {str(e)}")
        st.info("💡 Make sure your Groq API key is valid and you have an active internet connection.")

# ============================================================================
# HISTORICAL DATA SECTION
# ============================================================================

if not predict_btn and not quick_btn:
    st.markdown("---")
    st.markdown("## 📚 Historical Pandemic Database")
    
    # Load historical data
    # Create a dummy data structure if the file doesn't exist to prevent a full crash
    pandemics = []
    try:
        with open('data/pandemics.json', 'r') as f:
            pandemics = json.load(f)
    except FileNotFoundError:
        st.info("📁 No historical data found. See Sample Data Structure below.")
        pandemics = []

    if pandemics:
        # Create tabs for each pandemic
        tabs = st.tabs([p['name'] for p in pandemics])
        
        for tab, pandemic in zip(tabs, pandemics):
            with tab:
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"### {pandemic['name']}")
                    st.markdown(f"**Period:** {pandemic['period']}")
                    st.markdown(f"**Pathogen:** {pandemic['pathogen']}")
                    st.markdown(f"**Deaths:** {pandemic['deaths']}")
                    st.markdown(f"**Transmission:** {pandemic['transmission']}")
                    
                    if 'lessons' in pandemic:
                        st.markdown("**Key Lessons:**")
                        for lesson in pandemic['lessons']:
                            st.markdown(f"- {lesson}")
                
                with col2:
                    # Simple visualization
                    fig = go.Figure(go.Indicator(
                        mode="number",
                        value=pandemic.get('mortality_rate', 0),
                        title={'text': "Mortality Rate"},
                        number={'suffix': "%"},
                        domain={'x': [0, 1], 'y': [0, 1]}
                    ))
                    fig.update_layout(height=200, margin=dict(l=20, r=20, t=50, b=20))
                    st.plotly_chart(fig, use_container_width=True)
        
        # Comparison chart
        st.markdown("---")
        st.markdown("### 📊 Pandemic Comparison")
        
        # Create comparison data
        names = [p['name'] for p in pandemics]
        mortality_rates = [p.get('mortality_rate', 0) for p in pandemics]
        
        fig3 = go.Figure(data=[
            go.Bar(
                x=names,
                y=mortality_rates,
                marker=dict(
                    color=mortality_rates,
                    colorscale='Reds',
                    showscale=True
                ),
                text=mortality_rates,
                texttemplate='%{text}%',
                textposition='outside'
            )
        ])
        
        fig3.update_layout(
            title="Historical Pandemic Mortality Rates",
            xaxis_title="Pandemic",
            yaxis_title="Mortality Rate (%)",
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig3, use_container_width=True)
    
    # Show sample structure whether data was found or not
    with st.expander("📖 Sample Data Structure"):
        st.code('''[
{
"name": "COVID-19",
"period": "2019-2023",
"pathogen": "SARS-CoV-2",
"deaths": "6.9+ million",
"mortality_rate": 2,
"transmission": "Respiratory droplets, airborne",
"lessons": [
  "Early detection crucial",
  "Global cooperation essential"
]
}
]''', language='json')

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("""
<div class="custom-footer">
    <h3 style="color: #667eea;">🦠 EchoLens</h3>
    <p>Helping humanity prepare for future pandemics through AI-powered predictions</p>
    <p style="font-size: 0.9rem; color: #999;">
        Built by <a href="https://github.com/A-P-U-R-B-O" target="_blank" style="color: #667eea; text-decoration: none;">@A-P-U-R-B-O</a> • 
        Powered by Groq API
    </p>
    <p style="font-size: 0.8rem; color: #aaa; margin-top: 1rem;">
        ⚠️ Disclaimer: This is a research tool. Consult epidemiologists for public health decisions.
    </p>
</div>
""", unsafe_allow_html=True)

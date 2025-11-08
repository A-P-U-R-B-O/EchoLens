# 🦠 EchoLens - AI Pandemic Predictor

<div align="center">

![EchoLens Banner](https://img.shields.io/badge/EchoLens-Pandemic%20Predictor-blueviolet?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Predict Future Pandemics Using Historical Epidemic Patterns**

*Trained on Black Death • Spanish Flu • SARS • COVID-19*

[Live Demo](https://echolens.onrender.com) • [Documentation](#-features) • [Quick Start](#-quick-start) • [Deploy](#-deployment)

</div>

---

## 📖 Overview

**EchoLens** is an AI-powered pandemic prediction system that analyzes historical epidemic data to forecast future outbreak hotspots and global spread patterns. By learning from humanity's deadliest pandemics, EchoLens helps governments and health organizations prepare infrastructure and save lives.

> 💡 **Core Insight:** Disease patterns repeat when surveillance fails. History teaches us where the next pandemic will strike.

### 🎯 Key Capabilities

- 🔮 **Outbreak Prediction** - Forecast pandemic risk 30-180 days ahead
- 📊 **Risk Assessment** - Real-time risk scores for any geographic region
- 🗺️ **Hotspot Identification** - Pinpoint high-risk locations before outbreaks occur
- 📈 **Spread Forecasting** - Model transmission rates and growth patterns
- 🔍 **Historical Comparison** - Match current situations to past pandemics
- 💡 **Actionable Recommendations** - Immediate, short-term, and long-term strategies

---

## ✨ Features

### 🤖 AI-Powered Intelligence
- **Groq API Integration** - Lightning-fast predictions using OpenAI GPT-OSS 120B model
- **No Training Required** - Uses pre-trained AI knowledge on historical pandemics
- **Real-time Analysis** - Get predictions in seconds, not hours

### 🎨 Beautiful Dashboard
- **Modern UI** - Sleek gradients, smooth animations, professional design
- **Interactive Charts** - Plotly-powered gauges, trend lines, and comparisons
- **Responsive Layout** - Works perfectly on desktop, tablet, and mobile

### 📊 Visual Analytics
- **Risk Score Gauge** - 0-100 risk indicator with color-coded zones
- **Probability Trends** - 30/60/90-day outbreak likelihood charts
- **Historical Database** - Interactive tabs for Black Death, Spanish Flu, SARS, COVID-19
- **Comparison Graphs** - Side-by-side pandemic mortality rate analysis

### ⚡ Dual Analysis Modes
- **Quick Risk Check** - Instant assessment in under 10 seconds
- **Full Prediction** - Comprehensive analysis with detailed recommendations

### 📥 Export & Share
- **Download Reports** - Export predictions as text files
- **Shareable Links** - Send predictions to stakeholders
- **Timestamped Results** - Track prediction accuracy over time

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Groq API key (free from [console.groq.com](https://console.groq.com))

### Installation

```bash
# Clone the repository
git clone https://github.com/A-P-U-R-B-O/echolens.git
cd echolens

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### Configuration

Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Run Locally

```bash
streamlit run app.py
```

Visit: **http://localhost:8501**

---

## 📁 Project Structure

```
echolens/
├── app.py                      # Main Streamlit dashboard
├── groq_client.py              # Groq API client wrapper
├── data/
│   └── pandemics.json          # Historical pandemic database
├── .streamlit/
│   └── config.toml             # Streamlit configuration
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── render.yaml                 # Render.com deployment config
├── Dockerfile                  # Docker containerization
├── runtime.txt                 # Python version specification
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

**Total Files:** 5 core files (minimal and clean!)

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit 1.28+ | Interactive web dashboard |
| **AI Model** | Groq API (Llama 3.1 70B) | Fast LLM inference for predictions |
| **Visualization** | Plotly 5.17+ | Interactive charts and gauges |
| **Backend** | Python 3.11 | Core application logic |
| **Deployment** | Render / Streamlit Cloud | Cloud hosting |

---

## 💡 How It Works

### 1️⃣ Historical Learning
EchoLens analyzes patterns from 4 major pandemics:
- **Black Death (1347-1353)** - 75-200M deaths, 50% mortality
- **Spanish Flu (1918-1920)** - 50-100M deaths, 10% mortality
- **SARS (2002-2004)** - 774 deaths, 10% mortality
- **COVID-19 (2019-2023)** - 6.9M+ deaths, 2% mortality

### 2️⃣ Pattern Recognition
AI identifies similarities between current outbreaks and historical patterns:
- Transmission rates (R0 values)
- Geographic spread patterns
- Population density impacts
- Healthcare infrastructure readiness
- Seasonal and climate factors

### 3️⃣ Risk Calculation
Combines multiple factors to generate risk scores:
```
Risk Score = f(
    current_cases,
    population_density,
    healthcare_capacity,
    historical_patterns,
    geographic_factors,
    seasonal_conditions
)
```

### 4️⃣ Prediction Generation
Outputs actionable forecasts:
- **30/60/90-day probabilities** - Outbreak likelihood percentages
- **Hotspot locations** - High-risk cities and regions
- **Spread patterns** - Expected transmission routes
- **Recommendations** - Preventive actions with timelines

---

## 🎯 Use Cases

### 🏛️ Government & Public Health
- **Infrastructure Planning** - Allocate hospital beds and medical supplies
- **Early Warning Systems** - Detect outbreaks before they spread
- **Resource Distribution** - Optimize vaccine and treatment placement
- **Policy Decisions** - Data-driven lockdown and travel restrictions

### 🏥 Healthcare Organizations
- **Capacity Planning** - Prepare ICU beds and ventilators
- **Staff Allocation** - Deploy medical personnel efficiently
- **Supply Chain** - Stock PPE and medications proactively

### ✈️ Travel & Tourism
- **Risk Advisories** - Issue travel warnings based on predictions
- **Route Planning** - Avoid high-risk regions
- **Insurance Pricing** - Adjust premiums based on outbreak risk

### 🎓 Academic Research
- **Epidemiological Studies** - Analyze pandemic spread patterns
- **Model Validation** - Compare AI predictions to real outcomes
- **Historical Analysis** - Study lessons from past pandemics

---

## 📊 Sample Output

```
🎯 PREDICTION FOR SOUTHEAST ASIA
Generated: 2025-11-08 15:01:49 UTC

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 OVERALL RISK SCORE: 72/100 (HIGH RISK)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 OUTBREAK PROBABILITIES:
  • 30 days: 45% (Moderate Risk)
  • 60 days: 67% (Elevated Risk)
  • 90 days: 78% (High Risk)

🌍 SPREAD PATTERN:
  • Expected R0: 2.8-3.2
  • Primary vector: International air travel
  • Secondary vector: Urban mass transit
  • Geographic direction: West to East coastal cities

🚨 TOP 5 RISK FACTORS:
  1. High population density (15M+ in metro areas)
  2. Limited healthcare infrastructure (2 beds/1000 people)
  3. Major international travel hub (50M+ passengers/year)
  4. Monsoon season increasing transmission
  5. Historical outbreak region (SARS, H1N1 precedents)

📍 TOP 3 HOTSPOT CITIES:
  1. Bangkok, Thailand (Risk: 85/100)
  2. Manila, Philippines (Risk: 78/100)
  3. Ho Chi Minh City, Vietnam (Risk: 72/100)

💡 RECOMMENDATIONS:

Immediate Actions (0-7 days):
  • Increase disease surveillance at airports
  • Activate emergency response teams
  • Stockpile PPE and medical supplies

Short-term Strategies (1-4 weeks):
  • Expand testing capacity by 300%
  • Prepare field hospitals in hotspot cities
  • Launch public awareness campaigns

Long-term Preparation (1-3 months):
  • Improve healthcare infrastructure
  • Establish cross-border coordination protocols
  • Build vaccine distribution networks

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 HISTORICAL COMPARISON:
Most similar to: SARS (2002-2004)
Key similarity: Southeast Asia origin, similar R0 value
Critical difference: Higher population density now
Likely outcome: Containable with aggressive early intervention

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🌐 Deployment

### Deploy to Render.com (Free - Recommended)

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Deploy EchoLens"
   git push origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect repository: `A-P-U-R-B-O/echolens`
   - Render auto-detects `render.yaml`
   - Add environment variable: `GROQ_API_KEY=your_key`
   - Click "Create Web Service"

3. **Live in 2 minutes!** ✅
   - URL: `https://echolens.onrender.com`
   - Auto-deploys on every push

### Deploy to Streamlit Cloud (Easiest)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app" → Select `A-P-U-R-B-O/echolens`
3. Main file: `app.py`
4. Add secret: `GROQ_API_KEY = "your_key"`
5. Click "Deploy"

### Docker Deployment

```bash
# Build image
docker build -t echolens .

# Run container
docker run -p 8501:8501 -e GROQ_API_KEY=your_key echolens

# Access at http://localhost:8501
```

---

## 🔑 Getting Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up / Log in (free account)
3. Navigate to "API Keys"
4. Click "Create API Key"
5. Copy key and add to `.env` file

**Free Tier Includes:**
- 30 requests/minute
- 14,400 requests/day
- Llama 3.1 70B model access

---

## 📈 Roadmap

### v1.0 (Current) ✅
- [x] Historical pandemic database
- [x] Groq API integration
- [x] Risk prediction system
- [x] Beautiful Streamlit dashboard
- [x] Export reports

### v1.1 (Coming Soon) 🚧
- [ ] Real-time WHO/CDC data integration
- [ ] Interactive world map with hotspots
- [ ] Email alerts for high-risk regions
- [ ] Multi-language support (ES, FR, ZH)
- [ ] Mobile app (iOS/Android)

### v2.0 (Future) 🔮
- [ ] Custom ML model training
- [ ] Social media sentiment analysis
- [ ] Climate change impact modeling
- [ ] API endpoints for external integrations
- [ ] Enterprise dashboard with role-based access

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create feature branch:** `git checkout -b feature/AmazingFeature`
3. **Commit changes:** `git commit -m 'Add AmazingFeature'`
4. **Push to branch:** `git push origin feature/AmazingFeature`
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to all functions
- Test locally before submitting PR
- Update README if adding features

---

## 🐛 Known Issues

- **Slow first load on Render free tier** - Cold starts take 30-60 seconds
- **API rate limits** - Groq free tier limited to 30 requests/minute
- **Historical data** - Currently limited to 4 major pandemics

**Workarounds:**
- Upgrade to Render paid plan for faster loading
- Implement request caching to reduce API calls
- Contribute additional pandemic data via PR

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 A-P-U-R-B-O

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## ⚠️ Disclaimer

**Important:** EchoLens is a research and educational tool designed to demonstrate AI applications in epidemiology. It should **NOT** be used as the sole basis for public health decisions.

- ✅ **Use for:** Research, education, preliminary risk assessment
- ❌ **Do NOT use for:** Medical diagnosis, emergency response, policy decisions

**Always consult with:**
- Epidemiologists and infectious disease experts
- Public health authorities (WHO, CDC)
- Local government health departments

Predictions are based on historical patterns and current AI models, which may not account for novel pathogens, mutations, or unprecedented scenarios.

---

## 🙏 Acknowledgments

### Data Sources
- **World Health Organization (WHO)** - Global health data
- **Centers for Disease Control (CDC)** - Epidemic statistics
- **Historical Archives** - Black Death, Spanish Flu records
- **Academic Research** - Peer-reviewed epidemiological studies

### Technology
- **Groq** - Lightning-fast LLM inference
- **Streamlit** - Beautiful web app framework
- **Plotly** - Interactive visualizations
- **Python Community** - Open-source libraries

### Inspiration
> "Those who cannot remember the past are condemned to repeat it."  
> — George Santayana

This project was inspired by the lessons learned from COVID-19 and the need for better pandemic preparedness systems.

---

## 📞 Contact & Support

### Creator
**A-P-U-R-B-O**
- GitHub: [@A-P-U-R-B-O](https://github.com/A-P-U-R-B-O)
- Project: [EchoLens](https://github.com/A-P-U-R-B-O/echolens)

### Support
- 🐛 **Bug Reports:** [Open an issue](https://github.com/A-P-U-R-B-O/echolens/issues)
- 💡 **Feature Requests:** [Start a discussion](https://github.com/A-P-U-R-B-O/echolens/discussions)
- 📧 **Email:** Create an issue for private inquiries

### Community
- ⭐ **Star this repo** if it helps your research
- 🔄 **Share** with public health professionals
- 🤝 **Contribute** to make it better

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/A-P-U-R-B-O/echolens?style=social)
![GitHub forks](https://img.shields.io/github/forks/A-P-U-R-B-O/echolens?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/A-P-U-R-B-O/echolens?style=social)

![GitHub issues](https://img.shields.io/github/issues/A-P-U-R-B-O/echolens)
![GitHub pull requests](https://img.shields.io/github/issues-pr/A-P-U-R-B-O/echolens)
![GitHub last commit](https://img.shields.io/github/last-commit/A-P-U-R-B-O/echolens)

---

## 🌟 Star History

If EchoLens helps you or your organization, please ⭐ star this repository!

---

<div align="center">

### 🦠 EchoLens - Predicting Tomorrow's Pandemics Today

**Built by [@A-P-U-R-B-O](https://github.com/A-P-U-R-B-O)**  
**Powered by Groq API (OpenAI/GPT-OSS 120B)**  
**Last Updated: 2025-11-08**

---

*Helping humanity prepare for future pandemics through AI-powered predictions*

**[⬆ Back to Top](#-echolens---ai-pandemic-predictor)**

</div>

"""
EchoLens - Groq API Client
Fast AI predictions using Groq's lightning-fast inference
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class EchoLensAI:
    """Simple Groq API client for pandemic predictions"""
    
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            raise ValueError("❌ GROQ_API_KEY not found! Add it to .env file")
        
        self.client = Groq(api_key=api_key)
        self.model = "openai/gpt-oss-120b"  # Fast and powerful
    
    def predict_outbreak(self, region, current_cases, forecast_days=90):
        """Predict pandemic outbreak for a region"""
        
        prompt = f"""You are EchoLens, an AI expert trained on historical pandemic data.

HISTORICAL KNOWLEDGE:
- Black Death (1347-1353): Bubonic plague, killed 30-60% of Europe's population
- Spanish Flu (1918-1920): H1N1 virus, 50+ million deaths globally
- SARS (2002-2004): Coronavirus, 10% mortality rate, contained through quarantine
- COVID-19 (2019-2023): SARS-CoV-2, global pandemic, 1-2% mortality

CURRENT SITUATION:
- Region: {region}
- Active Cases: {current_cases:,}
- Forecast Period: {forecast_days} days

PREDICT:
1. **Outbreak Risk Score** (0-100): Overall pandemic risk
2. **30/60/90 Day Probability** (%): Likelihood of major outbreak
3. **Spread Pattern**: Expected transmission rate and growth
4. **Top 5 Risk Factors**: Why this region is vulnerable
5. **Top 3 Hotspot Cities**: Specific locations at highest risk
6. **Recommendations**: 
   - Immediate actions (0-7 days)
   - Short-term (1-4 weeks)
   - Long-term (1-3 months)

Format your response clearly with headers and bullet points.
Be specific with numbers and probabilities.
Base predictions on historical epidemic patterns."""

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are EchoLens, an expert epidemiologist AI specialized in pandemic prediction."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=self.model,
            temperature=0.7,
            max_tokens=2000,
            top_p=1,
            stream=False
        )
        
        return chat_completion.choices[0].message.content
    
    def analyze_comparison(self, current_outbreak):
        """Compare current situation to historical pandemics"""
        
        prompt = f"""Compare this outbreak to historical pandemics:

CURRENT OUTBREAK:
{current_outbreak}

COMPARE TO:
- Black Death (1347-1353)
- Spanish Flu (1918-1920)  
- SARS (2002-2004)
- COVID-19 (2019-2023)

Which historical pandemic does this most resemble and why?
What lessons from that pandemic apply here?
What's the likely outcome based on historical patterns?"""

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a pandemic historian and epidemiologist."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=self.model,
            temperature=0.7,
            max_tokens=1500
        )
        
        return chat_completion.choices[0].message.content
    
    def get_quick_risk(self, region, cases):
        """Get quick risk assessment"""
        
        prompt = f"""Quick pandemic risk assessment for {region} with {cases:,} active cases.
        
Provide ONLY:
1. Risk Score (0-100)
2. Risk Level (Low/Medium/High/Critical)
3. One sentence summary

Be concise."""

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=self.model,
            temperature=0.5,
            max_tokens=200
        )
        
        return chat_completion.choices[0].message.content

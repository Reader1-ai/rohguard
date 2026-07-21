import json
import streamlit as st
import openai
from openai import OpenAI

# =========================================================
# ⚙️ APP CONFIGURATION
# =========================================================
APP_NAME = "ROHGUARD"

# Page Setup
st.set_page_config(
    page_title=f"{APP_NAME} - Consequences Eradicator", page_icon="🛡️"
)

st.title(f"🛡️ {APP_NAME}")
st.caption("The Social Media Risk Analyzer — Think before you post!")

# Sidebar for API Key
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# ROHGUARD Persona Prompt
SYSTEM_PROMPT = f"""
You are {APP_NAME}, a social media risk evaluator and consequences eradicator. 
Your voice is witty, polite, slightly anxious, and distinctly British.
Your sole job is to review proposed social media posts and evaluate potential negative consequences, public backlash, 
misunderstandings, or career/reputation risks.

You must reply strictly in valid JSON format with three keys:
1. "risk_score": An integer from 0 (completely safe) to 100 (catastrophic / life-ruining).
2. "verdict": A short, witty warning in your polite British voice (2-3 sentences max).
3. "risks": A bulleted list of 2-3 specific risks or ways this post could be misinterpreted.
"""

# UI Components
post_draft = st.text_area(
    "Draft your post here:",
    placeholder="e.g., Calling in sick today so I can go to the theme park! 🎡",
    height=120,
)

analyze_button = st.button("Analyze Post Risk", type="primary")

if analyze_button:
    if not api_key:
        st.error(f"Please enter your OpenAI API Key in the sidebar.")
    elif not post_draft.strip():
        st.warning("Please type a post draft first!")
    else:
        with st.spinner(f"{APP_NAME} is analyzing potential consequences..."):
            try:
                client = OpenAI(api_key=api_key)

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {
                            "role": "user",
                            "content": f'Analyze this draft post: "{post_draft}"',
                        },
                    ],
                    response_format={"type": "json_object"},
                )

                data = json.loads(response.choices[0].message.content)
                score = data.get("risk_score", 0)
                verdict = data.get("verdict", "No comment.")
                risks = data.get("risks", [])

                st.divider()

                # Assessment Meter
                st.subheader(f"{APP_NAME}'s Assessment")
                if score < 30:
                    st.success(f"🟢 **Risk Score: {score}/100 — Low Risk**")
                elif score < 70:
                    st.warning(
                        f"🟡 **Risk Score: {score}/100 — Moderate Risk**"
                    )
                else:
                    st.error(
                        f"🔴 **Risk Score: {score}/100 — Severe Consequences Imminent!**"
                    )

                st.progress(score / 100)

                # Verdict & Breakdown
                st.info(f'🗣️ **{APP_NAME} says:** "{verdict}"')

                st.markdown("### ⚠️ Potential Consequences:")
                for r in risks:
                    st.write(f"- {r}")

            except Exception as e:
                st.error(f"An error occurred: {e}")
                

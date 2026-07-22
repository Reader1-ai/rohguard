import random
import time
import nltk
from nltk.corpus import opinion_lexicon
import streamlit as st

# Download the 10,000+ categorized word dictionary dataset
nltk.download("opinion_lexicon", quiet=True)

# Load thousands of pre-categorized dictionary words
POSITIVE_DICTIONARY = set(opinion_lexicon.positive())
NEGATIVE_DICTIONARY = set(opinion_lexicon.negative())

# Extra custom school/slang additions
SLANG_NEGATIVES = {
    "skinner",
    "opp",
    "snitch",
    "cringe",
    "ratio",
    "canceled",
    "cap",
}

# Setup Page
st.set_page_config(
    page_title="ROHGUARD - Consequences Eradicator", page_icon="🛡️"
)
st.title("🛡️ ROHGUARD")
st.caption("The Social Media Risk Analyzer — 10,000+ Word Dictionary Engine")

post_draft = st.text_area(
    "Draft your post here:",
    placeholder="e.g., Type any positive compliment or negative description from the dictionary!",
    height=120,
)

if st.button("Analyze Post Risk", type="primary"):
    if not post_draft.strip():
        st.warning("Please type a post draft first!")
    else:
        with st.spinner("ROHGUARD is scanning 10,000+ dictionary terms..."):
            time.sleep(1.0)

            # Clean and split input text into individual words
            words = [
                word.strip(".,!?\"'()").lower() for word in post_draft.split()
            ]

            # Check matches against the 10,000+ word lists
            matched_positive = [w for w in words if w in POSITIVE_DICTIONARY]
            matched_negative = [
                w
                for w in words
                if w in NEGATIVE_DICTIONARY or w in SLANG_NEGATIVES
            ]

            # ---------------------------------------------------------
            # EVALUATION LOGIC
            # ---------------------------------------------------------
            if matched_positive and not matched_negative:
                score = 0
                verdict = (
                    "Splendid! Your draft matched positive dictionary terms!"
                    " Positivity receives a 100% safety rating (0/100 risk) from"
                    " ROHGUARD."
                )
                risks = [
                    "Zero risk of negative social fallout.",
                    f"Matched positive dictionary terms: {', '.join(matched_positive)}",
                ]
            elif matched_negative:
                score = random.randint(85, 98)
                verdict = (
                    "Goodness gracious! Your draft matched negative terms in the"
                    " dictionary. ROHGUARD strongly advises against publishing this!"
                )
                risks = [
                    (
                        "High risk of social conflict, hurt feelings, or"
                        " disciplinary reports."
                    ),
                    f"Flagged dictionary terms: {', '.join(matched_negative)}",
                ]
            else:
                score = random.randint(10, 25)
                verdict = (
                    "Splendid! This post appears completely neutral and safe to"
                    " publish."
                )
                risks = [
                    "Minimal risk of negative feedback.",
                    "Negligible impact on your reputation.",
                ]

            st.divider()
            st.subheader("ROHGUARD's Assessment")

            if score < 30:
                st.success(f"🟢 **Risk Score: {score}/100 — Low Risk (Safe)**")
            elif score < 70:
                st.warning(f"🟡 **Risk Score: {score}/100 — Moderate Risk**")
            else:
                st.error(
                    f"🔴 **Risk Score: {score}/100 — Severe Consequences"
                    " Imminent!**"
                )

            st.progress(score / 100)
            st.info(f'🗣️ **ROHGUARD says:** "{verdict}"')

            st.markdown("### ⚠️ Potential Consequences:")
            for r in risks:
                st.write(f"- {r}")

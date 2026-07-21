import random
import time
import streamlit as st

# Setup
st.set_page_config(
    page_title="ROHGUARD - Consequences Eradicator", page_icon="🛡️"
)
st.title("🛡️ ROHGUARD")
st.caption("The Social Media Risk Analyzer — Think before you post!")

post_draft = st.text_area(
    "Draft your post here:",
    placeholder="e.g., Sending a challenge that possibly embarrasses my principal",
    height=120,
)

if st.button("Analyze Post Risk", type="primary"):
    if not post_draft.strip():
        st.warning("Please type a post draft first!")
    else:
        with st.spinner("ROHGUARD is analyzing potential consequences..."):
            time.sleep(1.2)  # Simulate processing

            text_lower = post_draft.lower()

            # Smart demo keyword checking
            risky_words = [
                "embarrass",
                "principal",
                "teacher",
                "prank",
                "challenge",
                "sick",
                "boss",
                "skinner",
                "secret",
                "fired",
            ]
            if any(word in text_lower for word in risky_words):
                score = random.randint(75, 95)
                verdict = (
                    "Right! Posting this is an absolute recipe for trouble."
                    " Targeting authority figures or school leadership is"
                    " virtually guaranteed to bring swift disciplinary action!"
                )
                risks = [
                    (
                        "High probability of administrative disciplinary action"
                        " or detention."
                    ),
                    (
                        "Violation of student conduct policies regarding"
                        " disrespect or harassment."
                    ),
                    (
                        "Permanent digital footprint that could impact school"
                        " standing."
                    ),
                ]
            else:
                score = random.randint(10, 25)
                verdict = (
                    "Splendid! This post appears completely harmless and"
                    " safe to publish."
                )
                risks = [
                    "Minimal risk of negative feedback.",
                    "Negligible impact on your reputation.",
                ]

            st.divider()
            st.subheader("ROHGUARD's Assessment")

            if score < 30:
                st.success(f"🟢 **Risk Score: {score}/100 — Low Risk**")
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

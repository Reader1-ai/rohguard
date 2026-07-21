import random
import time
import streamlit as st

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
            time.sleep(1.0)

            text_lower = post_draft.lower()

            # Word triggers + partial matching for typos
            danger_triggers = [
                "embarr",
                "embar",
                "photo",
                "pic",
                "edit",
                "kid",
                "classmate",
                "student",
                "principal",
                "teacher",
                "boss",
                "skinner",
                "prank",
                "challenge",
                "secret",
                "sick",
                "fired",
            ]

            matched_triggers = [
                word for word in danger_triggers if word in text_lower
            ]

            if len(matched_triggers) >= 1:
                score = random.randint(80, 98)
                verdict = (
                    "Goodness gracious! Editing or sharing embarrassing photos of"
                    " classmates or teachers is a massive safety violation."
                    " ROHGUARD strongly advises deleting this draft!"
                )
                risks = [
                    (
                        "High risk of cyberbullying, harassment, or"
                        " disciplinary action from school."
                    ),
                    (
                        "Violation of student privacy and digital conduct"
                        " policies."
                    ),
                    (
                        "Severe harm to personal relationships and digital"
                        " reputation."
                    ),
                ]
            else:
                score = random.randint(5, 20)
                verdict = (
                    "Splendid! This post appears completely harmless and safe"
                    " to publish."
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
                

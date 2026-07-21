import random
import time
import streamlit as st

st.set_page_config(
    page_title="ROHGUARD - Consequences Eradicator", page_icon="🛡️"
)
st.title("🛡️ ROHGUARD")
st.caption("The Social Media Risk Analyzer — Think before you post!,And make sure you type the words properly.NO TPYOS!")

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

            # Expanded trigger list covering insults, shaming, rude critiques, and "honest" blunt phrases
            danger_triggers = [
                # "Honest" / Blunt Disclaimer Phrases
                "honest",
                "truth",
                "no offense",
                "sorry not sorry",
                "just saying",
                "real talk",
                "facts",
                # Blunt / Rude Personality & Behavior Traits
                "annoying",
                "fake",
                "boring",
                "loud",
                "obnoxious",
                "lazy",
                "clueless",
                "cringe",
                "lame",
                "weird",
                "gross",
                "smelly",
                "mean",
                "bad",
                "horrible",
                "terrible",
                "awful",
                "useless",
                # Performance & Intelligence Critiques
                "dumb",
                "stupid",
                "idiot",
                "fail",
                "slow",
                "worst",
                "bad at",
                "sucks",
                # Physical & Shaming Triggers
                "fat",
                "ugly",
                "shame",
                "shaming",
                "bully",
                "insult",
                "mock",
                "tease",
                "roast",
                "hate",
                "expose",
                # Targets & Actions
                "friend",
                "classmate",
                "student",
                "kid",
                "teacher",
                "principal",
                "skinner",
                "boss",
                "photo",
                "pic",
                "edit",
                "embarr",
                "embar",
                "prank",
                "secret",
                "sick",
                "fired",
            ]

            matched_triggers = [
                word for word in danger_triggers if word in text_lower
            ]

            if len(matched_triggers) >= 1:
                score = random.randint(82, 98)
                verdict = (
                    "Goodness gracious! Even if a post is intended as honest feedback,"
                    " publishing blunt or rude criticisms publicly can cause severe offense."
                    " ROHGUARD strongly advises keeping this private!"
                )
                risks = [
                    (
                        "High potential for personal conflict, hurt feelings, or social backlash."
                    ),
                    (
                        "Risk of being reported for cyberbullying or code of conduct violations."
                    ),
                    (
                        "Permanent record of public hostility that could harm your reputation."
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

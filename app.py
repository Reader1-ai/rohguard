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

            # =========================================================
            # 1. COMPLIMENT DICTIONARY (Awards 0/100 Safe Score)
            # =========================================================
            compliments = [
                # Character & Personality
                "awesome",
                "amazing",
                "brilliant",
                "brave",
                "caring",
                "creative",
                "friendly",
                "funny",
                "generous",
                "great",
                "helpful",
                "honest",
                "kind",
                "legend",
                "nice",
                "polite",
                "smart",
                "sweet",
                "talented",
                "wonderful",
                "thoughtful",
                "supportive",
                "inspiring",
                "respectful",
                "welcoming",
                "clever",
                "patient",
                "humble",
                "loyal",
                "trustworthy",
                "charming",
                "energetic",
                "hardworking",
                # Physical & Appearance Compliments
                "gorgeous",
                "handsome",
                "pretty",
                "cute",
                "stylish",
                "neat",
                # Positive Reinforcement
                "best",
                "goat",
                "slay",
                "hero",
                "role model",
                "star",
                "genius",
                "mastermind",
                "champion",
                "winner",
            ]

            # =========================================================
            # 2. MASSIVE BAD DESCRIPTIONS & INSULTS DICTIONARY
            # =========================================================
            bad_descriptions = [
                # Category A: Physical & Appearance Insults
                "ugly",
                "fat",
                "gross",
                "smelly",
                "weird",
                "skinny",
                "hideous",
                "nasty",
                "unhygienic",
                "crusty",
                "musty",
                "dusty",
                "awkward",
                # Category B: Behavioral & Personality Traits
                "naughty",
                "rude",
                "mean",
                "fake",
                "annoying",
                "obnoxious",
                "lazy",
                "clueless",
                "cringe",
                "lame",
                "boring",
                "loud",
                "bossy",
                "greedy",
                "selfish",
                "sneaky",
                "dishonest",
                "horrible",
                "terrible",
                "awful",
                "useless",
                "dramatic",
                "petty",
                "jealous",
                "stubborn",
                "spoiled",
                "childish",
                "toxic",
                "obnoxious",
                # Category C: Intelligence & Capability Critiques
                "dumb",
                "stupid",
                "idiot",
                "slow",
                "worst",
                "sucks",
                "fail",
                "failure",
                "clumsy",
                "loser",
                "fool",
                "brainless",
                "ignorant",
                "incompetent",
                # Category D: Slang, Shaming & Internet Terminology
                "opp",
                "snitch",
                "clown",
                "trash",
                "garbage",
                "cap",
                "fraud",
                "poser",
                "freak",
                "bozo",
                "npc",
                "mid",
                "flop",
                "canceled",
                "ratio",
                # Category E: Direct Actions & Harassment Triggers
                "shame",
                "shaming",
                "bully",
                "insult",
                "mock",
                "tease",
                "roast",
                "hate",
                "expose",
                "prank",
                "embarr",
                "embar",
                "leak",
                "secret",
                "rumor",
                "gossip",
                "photoshop",
                # Category F: School Disruption & Authority Figures
                "skinner",
                "principal",
                "teacher",
                "boss",
                "fight",
                "steal",
                "cheat",
                "detention",
                "suspended",
                "fired",
            ]

            # ---------------------------------------------------------
            # EVALUATION LOGIC
            # ---------------------------------------------------------
            matched_compliments = [w for w in compliments if w in text_lower]
            matched_bad = [w for w in bad_descriptions if w in text_lower]

            if matched_compliments and not matched_bad:
                score = 0
                verdict = (
                    "Splendid! This is a lovely compliment! Positivity receives"
                    " a 100% safety rating from ROHGUARD."
                )
                risks = [
                    "Zero risk of negative fallout.",
                    "High probability of making someone's day brighter!",
                ]
            elif matched_bad:
                score = random.randint(85, 98)
                verdict = (
                    "Goodness gracious! Describing someone using negative terms,"
                    " insults, or public critiques can cause severe conflict."
                    " ROHGUARD strongly advises deleting this draft!"
                )
                risks = [
                    (
                        "High potential for personal conflict, hurt feelings, or"
                        " social backlash."
                    ),
                    (
                        "Risk of being reported for cyberbullying or code of"
                        " conduct violations."
                    ),
                    (
                        "Permanent record of public hostility that could harm your"
                        " reputation."
                    ),
                ]
            else:
                score = random.randint(10, 25)
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

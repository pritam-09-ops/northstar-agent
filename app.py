import streamlit as st
import time

# --- SETUP ---
st.set_page_config(page_title="Northstar Sales Agent", page_icon="⚡", layout="wide")
st.markdown("""
<style>
    .stApp { background-color: #f0f2f5; }
    .stChatMessage { background: white; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    h1 { color: #2b579a; font-family: 'Segoe UI', sans-serif; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg", width=50)
    st.markdown("### 🟢 Agent Active")
    st.caption("User: **Alex Chen (Sales Lead)**")
    st.success("📧 Outlook: Connected")
    st.success("☁️ Salesforce: Connected")
    st.warning("🛡️ Governance: Active")

# --- STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi Alex. I detected a high-priority **RFP from Acme Corp**. \n\nSalesforce data indicates this is a **Tier 1 Opportunity**. Shall I start the proposal process?"}
    ]
if "step" not in st.session_state:
    st.session_state.step = "init"

# --- CHAT ---
st.title("Northstar Proposal Agent")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- LOGIC ---
if st.session_state.step == "init":
    if st.button("Yes, begin drafting", type="primary"):
        st.session_state.messages.append({"role": "user", "content": "Yes, begin drafting."})
        st.session_state.step = "reasoning"
        st.rerun()

if st.session_state.step == "reasoning":
    with st.chat_message("assistant"):
        with st.status("🧠 **Orchestrating Context...**", expanded=True):
            st.write("📥 Reading email requirements...")
            time.sleep(1)
            st.write("☁️ Checking Pricing Rules in Salesforce...")
            time.sleep(1)
            st.error("⚠️ **Conflict Detected:** Client asks for 20% discount (Max allowed: 15%)")
        
        response = "I have paused the draft. **Policy Conflict Detected.**\n\nThe client requested 20%, but your limit is 15%. How should I proceed?"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.step = "decision"
        st.rerun()

if st.session_state.step == "decision":
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Use Standard 15%"):
            st.session_state.messages.append({"role": "user", "content": "Use Standard 15%."})
            st.session_state.step = "done"
            st.rerun()
    with c2:
        if st.button("Request VP Approval"):
            st.session_state.messages.append({"role": "user", "content": "Request VP Approval."})
            st.session_state.step = "action"
            st.rerun()

if st.session_state.step == "action":
    with st.chat_message("assistant"):
        st.success("✅ **Approval Requested**")
        st.write("I have sent an Adaptive Card to **Jordan (VP Sales)** via Microsoft Teams. I will notify you when approved.")
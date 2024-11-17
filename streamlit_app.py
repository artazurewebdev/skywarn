import streamlit as st

st.title("SkyWarn")
st.write("Presented by the International Weather Administration")

warningtype = st.radio("Warning Type", ["Tornado", "Thunderstorm", "Damage", "Wind Gust"])

if warningtype == "Tornado":
    st.subheader("Tornado Report")

    tornadotype = st.selectbox("Tornado Type", ["Rope", "Dust Devil", "Funnel", "Cone", "Sidewinder", "Wedge", "Multivortex"])

    reportcoords = st.text_input("Coordinates of Sighting")

    if "show_popup" not in st.session_state:
        st.session_state["show_popup"] = False

    if st.button("Detect Coordinates"):
        st.session_state["show_popup"] = True

    if st.session_state["show_popup"]:
        if st.button("Close"):
            st.session_state["show_popup"] = False
    
    with st.container():
        if st.session_state["show_popup"]:
            if st.button("Find Location"):
                st.success("Coordinates Determined")
            st.markdown(
                """
                <div style="background-color: darkgray; padding: 20px; border: 1px solid black; border-radius: 10px;">
                    <h4>Allow Location Tracking</h4>
                    <p>We do not share your data</p>
                    <button onclick="document.querySelector('button[title=\\"Close Popup\\"]').click()">Approve</button>
                </div>
                """,
                unsafe_allow_html=True,
            )

if warningtype == "Thunderstorm":
    st.subheader("Thunderstorm Report")

if warningtype == "Damage":
    st.subheader("Damage Report")

if warningtype == "Wind Gust":
    st.subheader("Wind Gust Report")

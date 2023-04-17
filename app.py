# install streamlit: pip install streamlit
# run: stramlit run app.py

import streamlit as st

# Define function for symmetric encryption
def symmetric_encryption():
    st.write("## Discussion:")
    st.write("Insert here")
    st.write("## Application:")
    st.write("Insert here")
    pass

# Define function for asymmetric encryption
def asymmetric_encryption():
    st.write("## Discussion:")
    st.write("Insert here")
    st.write("## Application:")
    st.write("Insert here")
    pass

# Define function for hashing
def hashing():
    st.write("## Discussion:")
    st.write("Insert here")
    st.write("## Application:")
    st.write("Insert here")
    pass

# Main Streamlit app
def main():
    st.title("Cryptographic Application")
    st.write("## Introduction:")
    st.write("Insert here")
    st.write("## Project Objectives:")
    st.write("Insert here")
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Symmetric Cryptography", "Asymmetric Cryptography", "Hashing"])
    with tab1:
        symmetric_encryption()
    with tab2:
        asymmetric_encryption()
    with tab3:
        hashing()



    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
        }
        </style>
        """
    , unsafe_allow_html=True)

    # You can customize the footer content here
    st.markdown(
        """
        <div class="footer">
            Created by: Member1 Member2 Member3 - BSCS 3A/3B
        </div>
        """
    , unsafe_allow_html=True)

if __name__ == "__main__":
    main()
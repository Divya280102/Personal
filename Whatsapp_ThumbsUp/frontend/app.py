import streamlit as st
import sys
sys.path.append(r'C:\Users\divya\Desktop\Personal\Whatsapp_ThumbsUp\backend')

from thumbs_up_counter import count_thumbs_up_emojis_for_date

def main():

    st.markdown(
        """
        <style>
            body {
                background-color: #FFB6C1; /* Replace with your desired background color */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Count your Thumbs Up 👍")
    
    # File Upload
    uploaded_file = st.file_uploader("Upload a Chat Text File (.txt)", type=["txt"])
    
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        
        # User Input: Target Date
        target_date = st.text_input("Enter the Target Date (dd/mm/yyyy):")
        
        if st.button("Count Thumbs Up Emojis"):
            if target_date:
                thumbs_up_count = count_thumbs_up_emojis_for_date(text, target_date)
                st.write(f"Total Thumbs Up Emojis Found on {target_date}: {thumbs_up_count}")



    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 0; right: 0; background-color: #f8f8f8; text-align: center;">
            <p>Made with ❤️ by divya</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    

if __name__ == "__main__":
    main()

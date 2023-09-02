import streamlit as st
import sys
sys.path.append(r'C:\Users\divya\Desktop\Whatsapp_ThumbsUp\backend')

import toml
config = toml.load("config.toml")

import os
import re
from thumbs_up_counter import process_file, count_thumbs_up_emojis_for_date  # Updated import

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
    uploaded_file = st.file_uploader("Upload a Chat Text File (.txt or .zip)", type=["txt", "zip"])

    # User Input: Target Date
    target_date = None

    if uploaded_file is not None:
        file_extension = os.path.splitext(uploaded_file.name)[-1].lower()

        if file_extension == '.zip':
            # Display date input for zip file
            target_date = st.text_input("Enter the Target Date (dd/mm/yyyy):")

        elif file_extension == '.txt':
            # Display date input for text file
            target_date = st.text_input("Enter the Target Date (dd/mm/yyyy):")

        if target_date is not None and st.button("Count Thumbs Up Emojis"):
            if file_extension == '.zip':
                thumbs_up_count = process_file(uploaded_file, target_date)
            elif file_extension == '.txt':
                text = uploaded_file.read().decode("utf-8")
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




# import streamlit as st
# import sys
# sys.path.append(r'C:\Users\divya\Desktop\Whatsapp_ThumbsUp\backend')


# from thumbs_up_counter import count_thumbs_up_emojis_for_date

# def main():

#     st.markdown(
#         """
#         <style>
#             body {
#                 background-color: #FFB6C1; /* Replace with your desired background color */
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     st.title("Count your Thumbs Up 👍")
    
#     # File Upload
#     uploaded_file = st.file_uploader("Upload a Chat Text File (.txt)", type=["txt"])
    
#     if uploaded_file is not None:
#         text = uploaded_file.read().decode("utf-8")
        
#         # User Input: Target Date
#         target_date = st.text_input("Enter the Target Date (dd/mm/yyyy):")
        
#         if st.button("Count Thumbs Up Emojis"):
#             if target_date:
#                 thumbs_up_count = count_thumbs_up_emojis_for_date(text, target_date)
#                 st.write(f"Total Thumbs Up Emojis Found on {target_date}: {thumbs_up_count}")



#     st.markdown(
#         """
#         <div style="position: fixed; bottom: 0; left: 0; right: 0; background-color: #f8f8f8; text-align: center;">
#             <p>Made with ❤️ by divya</p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
    
    

# if __name__ == "__main__":
#     main()

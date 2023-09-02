import zipfile
import re

# Function to count thumbs-up emojis in a text string for a specific date
def count_thumbs_up_emojis_for_date(text_content, target_date):
    thumbs_up_emoji = '👍'
    thumbs_up_count = 0
    
    # Split the text into individual messages based on line breaks
    messages = text_content.split('\n')
    
    for message in messages:
        # Use regular expressions to find the date in the message (dd/mm/yyyy format)
        date_match = re.search(r'\d{2}/\d{2}/\d{4}', message)
        
        if date_match:
            message_date = date_match.group(0)
            
            # Check if the message date matches the target date
            if message_date == target_date:
                thumbs_up_count += message.count(thumbs_up_emoji)

    return thumbs_up_count

def process_file(uploaded_file, target_date):
    file_name = uploaded_file.name
    thumbs_up_count = 0

    try:
        if file_name.endswith('.zip'):
            # Open the zip file
            with zipfile.ZipFile(uploaded_file, 'r') as zip_file:
                found_txt_file = False

                # Iterate through the files in the archive
                for file_name in zip_file.namelist():
                    if file_name.endswith('.txt'):
                        found_txt_file = True

                        # Extract and read the .txt file
                        with zip_file.open(file_name) as text_file:
                            # Read the content of the text file
                            text_content = text_file.read().decode('utf-8')

                            if target_date:
                                thumbs_up_count = count_thumbs_up_emojis_for_date(text_content, target_date)

                            return thumbs_up_count

                if not found_txt_file:
                    return "No .txt file found in the zip archive."
        elif file_name.endswith('.txt'):
            # Read the standalone .txt file
            text_content = uploaded_file.read().decode('utf-8')

            if target_date:
                thumbs_up_count = count_thumbs_up_emojis_for_date(text_content, target_date)

            return thumbs_up_count, file_name
        else:
            return "Invalid file format. Please provide a .txt file or a .zip archive."

    except Exception as e:
        return f"An error occurred: {str(e)}"




# import re

# def count_thumbs_up_emojis_for_date(text, target_date):
#     thumbs_up_emoji = '👍'
#     thumbs_up_count = 0
    
#     # Split the text into individual messages based on line breaks
#     messages = text.split('\n')
    
#     for message in messages:
#         # Use regular expressions to find the date in the message (dd/mm/yyyy format)
#         date_match = re.search(r'\d{2}/\d{2}/\d{4}', message)
        
#         if date_match:
#             message_date = date_match.group(0)
            
#             # Check if the message date matches the target date
#             if message_date == target_date:
#                 thumbs_up_count += message.count(thumbs_up_emoji)

#     return thumbs_up_count

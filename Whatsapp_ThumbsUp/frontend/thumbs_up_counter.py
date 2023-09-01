import re

def count_thumbs_up_emojis_for_date(text, target_date):
    thumbs_up_emoji = '👍'
    thumbs_up_count = 0
    
    # Split the text into individual messages based on line breaks
    messages = text.split('\n')
    
    for message in messages:
        # Use regular expressions to find the date in the message (dd/mm/yyyy format)
        date_match = re.search(r'\d{2}/\d{2}/\d{4}', message)
        
        if date_match:
            message_date = date_match.group(0)
            
            # Check if the message date matches the target date
            if message_date == target_date:
                thumbs_up_count += message.count(thumbs_up_emoji)

    return thumbs_up_count

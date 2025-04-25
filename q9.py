import re

def tamil_tokenizer(text):
    tokens = []
    tokens.extend(re.findall(r'[.,?!;:\-\(\)\[\]\{\}\'\"।॥]', text)) 

    tokens.extend(re.findall(r'\b\d{1,2}[/\-.]\d{1,2}[/\-.]\d{2,4}\b', text)) 
    tokens.extend(re.findall(r'\b\d{1,2}[/\-.]\d{1,2}[/\-.]\d{2,4}\b', text)) 
    tokens.extend(re.findall(r'\b\d{1,2} (ஜனவரி|பிப்ரவரி|மார்ச்|ஏப்ரல்|மே|ஜூன்|ஜூலை|ஆகஸ்ட்|செப்டம்பர்|அக்டோபர்|நவம்பர்|டிசம்பர்) \d{4}\b', text)) #Tamil month names. Add more variations

    tokens.extend(re.findall(r'https?://\S+', text))

    tokens.extend(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z]{2,}\b', text))

    tokens.extend(re.findall(r'\b\d+(?:[.,]\d+)?\b', text)) 
    tokens.extend(re.findall(r'\b\d{1,3}(?:,\d{3})*\b', text))  
    tokens.extend(re.findall(r'\b\d+/\d+\b', text))

    tokens.extend(re.findall(r'@[A-Za-z0-9_]+', text))
    tokens.extend(re.findall(r'#[A-Za-z0-9_]+', text))

    tokens.extend(re.findall(r'[\u0B80-\u0BFF]+', text))

    return tokens



text = "இன்று தேதி 02/03/2024.  எனது மின்னஞ்சல் example@gmail.com. நான் @user மற்றும் #tag பயன்படுத்துகிறேன்.  எண்கள் 33.15 மற்றும் 1,23,456.  வலைத்தளங்கள் google.com மற்றும் https://www.example.com.  வணக்கம், எப்படி இருக்கிறீர்கள், சாப்பிட்டீர்களா?" #Example Tamil text
tokens = tamil_tokenizer(text)
print(tokens)
import re

def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)     # Remove @menções
    text = re.sub(r"#", "", text)        # Remove o símbolo #
    text = re.sub(r"[^\w\s]", "", text)  # Remove pontuações
    return text.strip().lower()

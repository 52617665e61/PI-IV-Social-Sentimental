
from transformers import pipeline
from utils.preprocessing import clean_text

classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    cleaned = clean_text(text)
    result = classifier(cleaned)[0]
    label = result["label"]
    
    if "1" in label or "2" in label:
        return "negativo"
    elif "4" in label or "5" in label:
        return "positivo"
    else:
        return "neutro"

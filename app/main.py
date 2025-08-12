from core.sentiment import analyze_sentiment
from modules.twitter.fetcher import fetch_tweets

def main():
    tweets = fetch_tweets("#PI4")
    for tweet in tweets:
        result = analyze_sentiment(tweet)
        print(f"Tweet: {tweet}")
        print(f"Sentimento: {result}")
        print("-" * 40)

if __name__ == "__main__":
    main()
from app.core.sentiment import analyze_sentiment
from app.modules.twitter.fetcher import fetch_tweets

def main():
    tema = input("Digite o tema para buscar nas redes sociais: ")
    tweets = fetch_tweets(tema)

    print("\n🔍 Resultados da Análise de Sentimento:\n")
    for tweet in tweets:
        sentimento = analyze_sentiment(tweet)
        print(f"Texto: {tweet}")
        print(f"Sentimento: {sentimento}")
        print("-" * 40)

if __name__ == "__main__":
    main()

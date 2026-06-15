import spacy

from app.utils.text_cleaner import clean_context

from vaderSentiment.vaderSentiment import (
    SentimentIntensityAnalyzer
)

from transformers import pipeline



nlp = spacy.load(
    "en_core_web_sm"
)

vader_analyzer = (
    SentimentIntensityAnalyzer()
)

bert_pipeline = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    truncation=True,
    max_length=512
)



POSITIVE_THRESHOLD = 0.10

NEGATIVE_THRESHOLD = -0.10

CHUNK_SIZE = 4

#chunking function 

def split_text(
    text,
    chunk_size=CHUNK_SIZE
):

    doc = nlp(text)

    sentences = [

        sent.text.strip()

        for sent in doc.sents

        if sent.text.strip()
    ]

    chunks = []

    for i in range(

        0,

        len(sentences),

        chunk_size
    ):

        chunk = " ".join(

            sentences[
                i:i + chunk_size
            ]
        )

        chunks.append(
            chunk
        )

    return chunks


# bert score function

def get_bert_score(
    chunk
):

    result = bert_pipeline(
        chunk
    )[0]

    label = result["label"].lower()

    confidence = result["score"]

    if label == "positive":

        return confidence

    elif label == "negative":

        return -confidence

    return 0

#main function to analyze sentiment

def analyse_sentiment(
    context
):
    
    if not context:

        return {

            "score": 0,

            "sentiment": 0
        }
    

    cleaned_context = clean_context(
        context
    )

    if not cleaned_context:

        return {

            "score": 0,

            "sentiment": 0
        }

    chunks = split_text(
        cleaned_context
    )

    scores = []

    positive_chunks = 0

    negative_chunks = 0

    neutral_chunks = 0

    for chunk in chunks:

        vader_score = (

            vader_analyzer
            .polarity_scores(
                chunk
            )["compound"]

        )

        bert_score = get_bert_score(
            chunk
        )

        final_score = round(

            (
                0.5 * vader_score
            )
            +
            (
                0.5 * bert_score
            ),
            4
        )

        scores.append(
            final_score
        )

        if final_score > POSITIVE_THRESHOLD:

            positive_chunks += 1

        elif final_score < NEGATIVE_THRESHOLD:

            negative_chunks += 1

        else:

            neutral_chunks += 1

    average_score = round(

        sum(scores)
        /
        len(scores),
        4
    )

    if negative_chunks > positive_chunks:

        sentiment = -1

    elif positive_chunks > negative_chunks:

        sentiment = 1

    else:

        sentiment = 0

    return {

        "score": average_score,
        "context": context,
        "sentiment": sentiment
    }


def calculate_aggregate_sentiment(
    sentiments
):
    
    if not sentiments:
        return {
            "average_score": 0.0,
            "sentiment": 0,
            "total_chats": 0,
            "positive_count": 0,
            "negative_count": 0,
            "neutral_count": 0
        }
    
    total_chats = len(sentiments)
    scores = []
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    for sentiment in sentiments:
        scores.append(sentiment.score)
        
        if sentiment.sentiment == 1:
            positive_count += 1
        elif sentiment.sentiment == -1:
            negative_count += 1
        else:
            neutral_count += 1
    
    average_score = round(
        sum(scores) / len(scores),
        4
    )
    
    if negative_count > positive_count:
        overall_sentiment = -1
    elif positive_count > negative_count:
        overall_sentiment = 1
    else:
        overall_sentiment = 0
    
    return {
        "average_score": average_score,
        "sentiment": overall_sentiment,
        "total_chats": total_chats,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "neutral_count": neutral_count
    }
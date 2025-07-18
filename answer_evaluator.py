from textblob import TextBlob
import re

def evaluate_answer(answer, question):
    feedback = []

    # Grammar and sentiment
    blob = TextBlob(answer)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Word count
    word_count = len(answer.split())
    feedback.append(f"📝 Your answer has **{word_count} words**.")

    # Sentiment analysis
    if polarity > 0.3:
        feedback.append("🙂 The tone of your answer is positive and confident.")
    elif polarity < -0.3:
        feedback.append("😟 The tone of your answer seems negative.")
    else:
        feedback.append("😐 The tone is neutral.")

    # Subjectivity
    if subjectivity > 0.6:
        feedback.append("🔍 Your answer is quite subjective. Try being more factual.")
    else:
        feedback.append("✅ Your answer is objective and to the point.")

    # Keyword matching
    keywords = re.findall(r'\b\w+\b', question.lower())
    missing_keywords = [kw for kw in keywords if kw not in answer.lower()]
    if missing_keywords and len(missing_keywords) < 5:
        feedback.append(f"📌 You may consider including these terms: {', '.join(missing_keywords[:3])}.")

    return "\n\n".join(feedback)

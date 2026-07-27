# classifier.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# -----------------------------
# Training Dataset
# -----------------------------

emails = [

    "Amazon order shipped package delivery",
    "Flipkart purchase invoice",
    "Your shopping order is delivered",

    "HDFC bank transaction alert",
    "SBI account statement",
    "ICICI banking OTP transaction",

    "TCS interview invitation",
    "Infosys job offer letter",
    "Recruitment drive notification",

    "Exam hall ticket released",
    "University exam timetable",
    "Semester result announcement",

    "You won lottery prize",
    "Claim free money reward",
    "Congratulations you won",

    "Microsoft security alert",
    "Password changed successfully",
    "Two step verification enabled"
]


categories = [

    "Purchases",
    "Purchases",
    "Purchases",

    "Banking",
    "Banking",
    "Banking",

    "Jobs",
    "Jobs",
    "Jobs",

    "Examinations",
    "Examinations",
    "Examinations",

    "Spam",
    "Spam",
    "Spam",

    "Important",
    "Important",
    "Important"
]


# -----------------------------
# Create AI Model
# -----------------------------

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(emails)


model = MultinomialNB()

model.fit(
    X,
    categories
)


# -----------------------------
# Classification Function
# -----------------------------

def classify_email(subject, body):

    text = str(subject) + " " + str(body)


    vector = vectorizer.transform(
        [text]
    )


    prediction = model.predict(
        vector
    )[0]


    probability = model.predict_proba(
        vector
    )


    confidence = max(probability[0]) * 100


    return prediction, round(confidence, 2)
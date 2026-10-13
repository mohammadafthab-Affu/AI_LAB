
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training messages
messages = [
    "Win a free prize now",
    "Claim your free reward",
    "Congratulations you won cash",
    "Get a special offer today",
    "Please attend the meeting",
    "Can we meet after class",
    "Your assignment is due Friday",
    "Please send me the notes"
]

# Labels
labels = [
    "Spam", "Spam", "Spam", "Spam",
    "Not Spam", "Not Spam", "Not Spam", "Not Spam"
]

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train the model
model = MultinomialNB()
model.fit(X, labels)

# Test a new message
new_message = ["Win cash and get a free prize"]
X_test = vectorizer.transform(new_message)

prediction = model.predict(X_test)

print("Message:", new_message[0])
print("Classification:", prediction[0])

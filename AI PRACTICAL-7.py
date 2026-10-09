
from sklearn.naive_bayes import BernoulliNB

# Training data
X = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [0, 0, 0]
]

# Labels
y = [
    'Flu', 'Flu', 'Flu',
    'Cold', 'Cold', 'Cold'
]

# Create and train the model
model = BernoulliNB()
model.fit(X, y)

# Predict for patient 1
patient1 = [[1, 1, 1]]
prediction1 = model.predict(patient1)

print("Patient 1 Diagnosis:", prediction1[0])

# Display probabilities
probabilities = model.predict_proba(patient1)

for diagnosis, probability in zip(model.classes_, probabilities[0]):
    print(diagnosis, "=", round(probability, 2))

# Predict for patient 2
patient2 = [[0, 1, 0]]
prediction2 = model.predict(patient2)

print("Patient 2 Diagnosis:", prediction2[0])

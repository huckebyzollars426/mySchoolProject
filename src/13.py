import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# Preprocess text data
vectorizer = TfidfVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(train_df['text'])
y_train = train_df['label']
X_test = vectorizer.transform(test_df['text'])

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics

data = pd.read_csv(r'spam.csv' ,encoding =' latin-1')
print(data.head())
print(data.columns)
#remove extra columns from csv file
data = data[['v1', 'v2']]
print(data.columns)
#assign new name to v1 & v2 coloum
data.columns =['label','message']
print(data.columns)
print(data.head())

# assign binary value to label ham =0,spam=1
data['label'] = data['label'].map({'ham':0 , 'spam':1})
print(data.head())

X_train, X_test, y_train, y_test= train_test_split(data['message'],data['label'],test_size=0.3,random_state=42)


# extract the feature vector
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print(vectorizer.get_feature_names_out())



# 6. Train the Naive Bayes Classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 7. Make Predictions
y_pred = model.predict(X_test_tfidf)

# 8. Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

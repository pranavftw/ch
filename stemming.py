
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download necessary NLTK data files
#nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')




def preprocess_text(text):
    # Initialize the Porter Stemmer
    #stemmer = PorterStemmer()
    lemma = nltk.wordnet.WordNetLemmatizer()
    # Define English stop words
    stop_words = set(stopwords.words('english'))

    # Tokenize the text
    words = word_tokenize(text,language='english', preserve_line=True)
    print(words)

    # Remove stop words and perform stemming
   # preprocessed_words = [stemmer.stem(word) for word in words if word.lower() not in stop_words and word.isalpha()]
    preprocessed_words = [lemma.lemmatize(word) for word in words if word.lower() not in stop_words and word.isalpha()]

    return ' '.join(preprocessed_words)


# Example text
text = """
Natural language processing (NLP) is a field of artificial intelligence (AI) 
that focuses on the interaction between computers and humans through natural language. 
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language.
"""

# Preprocess the text
preprocessed_text = preprocess_text(text)

print("Original Text:")
print(text)
print("\nPreprocessed Text:")
print(preprocessed_text)
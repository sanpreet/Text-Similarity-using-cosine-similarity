# importing nltk as well as string library
import nltk, string
# removing warnings
import warnings
warnings.filterwarnings("ignore")
# for feature extraction import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# sent_tokenize() uses a pre-trained model from nltk_data/tokenizers/punkt/english.pickle
nltk.download('punkt') 

# creating class based code
class DocumentSimilarity:
# whenever the constructor is created, firstly this function is called	
	def __init__(self):
		self.stemmer = nltk.stem.porter.PorterStemmer()
		self.remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
# stemming which is an important part of nlp preprocessing
	def stem_tokens(self, tokens):
		return [self.stemmer.stem(item) for item in tokens]

# remove punctuation, lowercase, stem
	def normalize(self, text):
		return self.stem_tokens(nltk.word_tokenize(text.lower().translate(self.remove_punctuation_map)))
# similary being checked using cosine similarity
	def cosine_sim(self, text1, text2):
		vectorizer = TfidfVectorizer(tokenizer=self.normalize, stop_words='english')
		tfidf = vectorizer.fit_transform([text1, text2])
		return ((tfidf * tfidf.T).A)[0,1]

# object of the class is created which can access the variables and member function of the class
object_document_similar = DocumentSimilarity()



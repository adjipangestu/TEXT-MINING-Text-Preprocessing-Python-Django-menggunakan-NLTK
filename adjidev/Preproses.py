import nltk 
import string 
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize 

#lowercase
def text_lowercase(text): 
    return text.lower()

# Remove numbers 
def remove_numbers(text): 
    result = re.sub(r'\d+', '', text) 
    return result 

# remove whitespace from text 
def remove_whitespace(text): 
    return  " ".join(text.split()) 

# remove punctuation 
def remove_punctuation(text): 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator)

# remove stopwords function 
def remove_stopwords(text): 
    stop_words = set(stopwords.words("english")) 
    word_tokens = word_tokenize(text) 
    filtered_text = [word for word in word_tokens if word not in stop_words] 
    return filtered_text 

# lemmatize string 
lemmatizer = WordNetLemmatizer()
def lemmatize_word(text): 
    stop_words = set(stopwords.words("english")) 
    stop_words.update(('one','two','and','I','A','And','So','arnt','This','When','It','many','Many','so','cant','Yes','yes','No','no','These','these'))
    word_tokens = word_tokenize(text) 
    # provide context i.e. part-of-speech 
    lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens if word not in stop_words] 
    new_sentence = ' '.join(lemmas)
    return new_sentence
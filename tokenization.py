import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

print(sent_tokenize("Today is our first NLP lab . we are studying tokenization"))
print(word_tokenize("Tokenization is a process of dividing strings"))
import transformers
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
text="This"
print(tokenizer.tokenize(text))
def sub_tokenize(sentence):
   
    characters = [char for char in sentence if char != ' ']
    return characters

sentence = "blue bird"
sub_tokens = sub_tokenize(sentence)
print(sub_tokens) 

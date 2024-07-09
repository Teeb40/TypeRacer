import nltk
from nltk.corpus import brown
import random
import pygame
# Download necessary NLTK data
nltk.download('brown')
nltk.download('punkt')
pygame.init()
# Tokenize the text from the Brown corpus
tokens = brown.words()
bigrams = list(nltk.bigrams(tokens))
cfd = nltk.ConditionalFreqDist(bigrams)

# Function to generate a random sentence using bigrams
def generate_sentence(cfd, start_word, length=10):
    word = start_word
    sentence = [word.capitalize()]
    for _ in range(length - 1):
        word = random.choice(list(cfd[word].keys()))
        sentence.append(word)
    return ' '.join(sentence) + '.'

# Function to generate a random paragraph
def generate_paragraph(cfd=cfd, sentence_count=5, sentence_length=20):
    return ' '.join(generate_sentence(cfd, random.choice(list(cfd.keys())), sentence_length) for _ in range(sentence_count))


from itertools import chain

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped


def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)


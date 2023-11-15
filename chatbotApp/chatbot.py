from email import message
import random
import json
import pickle
import numpy as np
import nltk


from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open(r'C:\Users\bipin\OneDrive\Desktop\Chatbot\chatbotProject\chatbotApp\intents.json').read())

# loads trained models
words = pickle.load(open(r'C:\Users\bipin\OneDrive\Desktop\Chatbot\chatbotProject\chatbotApp\words.pkl', 'rb'))
classes = pickle.load(open(r'C:\Users\bipin\OneDrive\Desktop\Chatbot\chatbotProject\chatbotApp\classes.pkl', 'rb'))
model = load_model(r'C:\Users\bipin\OneDrive\Desktop\Chatbot\chatbotProject\chatbotApp\chatbot_model.h5')

# clean up the sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

# change the cleaned word to numpy array
def bag_of_words (sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# searching for the best matching class
def predict_class (sentence):
    bow = bag_of_words (sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = .50
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes [r[0]], 'probability': str(r[1])})
    return return_list

# giving response baesd on selected class
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice (i['responses'])
            break
    return result

# main function recieves input
def question(message):
    try:
        ints = predict_class (message)
        result = get_response(ints,intents)
        return result
    except:
        return "try something else"





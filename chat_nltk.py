import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('nps_chat')

import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, how about you?', 'Doing great, and you?']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me Codealpha Bot.']),
    (r'quit', ['Bye!', 'Goodbye!']),
]
def nltk_chatbot():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk_chatbot()


from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import datetime
from chatterbot.logic import LogicAdapter

# chatbot = ChatBot(
#     'Alexa',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     database_uri='sqlite:///database.sqlite3'
# )

chatbot = ChatBot(
    'Alexa',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
],
    database_uri='sqlite:///database.sqlite3'
    read_only=True
)

#chatbot = ChatBot("Alexa")
#print(chatbot)

# conversation = [
#     "Hello",
#     "Hi There",
#     "How are you doing",
#     "I am doing great.",
#     "That is good to hear",
#     "Thank You",
#     "You are welcome."
# ]
# trainer = ListTrainer(chatbot)
# trainer.train(conversation)

trainer = ChatterBotCorpusTrainer(chatbot)
 trainer.train(
     "chatterbot.corpus.english"
     
 )
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir!")

    elif hour>=12 and hour<18:
        print("Good Afternoon Sir!")   

    else:
        print("Good Evening Sir!")
    print("I am Niki, How may i help you ?")
	
wishMe()

while True:
	message = input('you:')
	reply = chatbot.get_response(message)
	print('Niki:',reply)
	if message.strip() == 'Bye' or message.strip() == 'bye':
		print('Niki: Bye')
		break
		

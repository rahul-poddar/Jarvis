from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting the Jarvis : please wait amoment...")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting the Jarvis : please wait few second...")
from Main import MainTaskExecution


def MainExecution():

    Speak("Hello Sir!")
    Speak("I'm HackZero, How can I help you!")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Welcome Back!! >>")
        MainExecution()
    else:
        pass

ClapDetect()
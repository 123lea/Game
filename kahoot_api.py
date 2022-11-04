from http.client import NON_AUTHORITATIVE_INFORMATION
import string
from tkinter import NONE
import api_utils

api = api_utils.API()
broker = api_utils.PubSub()


@api.POST("/api/join")
def join(request, player_name: str):
    broker.publish("new_player", player_name)

@api.POST("/api/start_question")
def start_question(request):
    broker.publish("start_question", None)

@api.POST("/api/answer")
def answer(request, player_name:str, answer:int):
    broker.publish("answer", {"player_name":player_name, "answer": answer})

@api.POST("/api/answer2")
def answer2(request, player_name:str, answer2:int):
    broker.publish("answer2", {"player_name":player_name, "answer2": answer2})

@api.POST("/api/end_question")
def end_question(request, correct_answer:int):
    broker.publish("end_question", correct_answer)


@api.GET("/api/messages")
def messages(request):
    return broker.streaming_response(request)

api_utils.run(api)



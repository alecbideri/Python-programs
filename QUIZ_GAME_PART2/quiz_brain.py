from data import question_data
from question_model import question


def get_questiona():
    return (question(item["text"], item["answer"]) for item in question_data)

import json

file = "match_data.json"

def parse_questions():
    questions = {}
    data = json.load(open(file, "r"))
    game_id = data["game_id"]

    raw_questions = data["questions"].split("\n")

    for qas in raw_questions:
        qa = qas.split("\t")
        q = qa[0]
        a = qa[1]
        questions[q] = a

    return questions, game_id

def reverse(din):
    return {q: r for r, q in din.items()}
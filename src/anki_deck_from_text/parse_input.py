
def question_answer_split(line, separator):
    line = line.lstrip("- ")
    answer, question = line.split(separator)
    return question, answer


def generate_question_answer_dict(input, separator):
    cards_details = dict()
    with open(input, encoding="utf-8") as FileObj:
        for line in FileObj:
            line = line.strip()
            if not line.startswith("-"):
                continue

            question, answer = question_answer_split(
                line=line,
                separator=separator
            )
            cards_details[question] = answer
    return cards_details

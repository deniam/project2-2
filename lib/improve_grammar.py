def check_sentence_grammar(text):
    if text == "":
        raise Exception("This string is empty.")
    return text[0].isupper() and text[-1] in ".?!"
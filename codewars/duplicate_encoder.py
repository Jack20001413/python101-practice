def duplicate_encoder(word):
    text = word.lower()
    return "".join(["(" if text.count(char) == 1 else ")" for char in text ])


original_text = "y GRXlEynRGri(mZepUCoESBpVvyWWot vsO"
result = duplicate_encoder(original_text)
print(result)
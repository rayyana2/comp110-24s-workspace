def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx < len(my_words):
        print(my_words[letter_idx])
    else:
        print("Index too high")
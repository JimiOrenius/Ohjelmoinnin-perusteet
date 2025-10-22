DELIMITER = ','

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)

def analyseWords(words_string):
    if not words_string:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return
    
    word_list = words_string.split(DELIMITER)
    word_count = len(word_list)
    char_count = sum(len(word) for word in word_list)
    avg_length = char_count / word_count
    
    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))

def main():
    print("Program starting.")
    collected = collectWords()
    analyseWords(collected)
    print("Program ending.")

main ()
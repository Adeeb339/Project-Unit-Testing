def string_reverser(text):
    
    if not text:
        return 0
    return text[::-1]
def word_counter(text):
    
    word=text.split()
    return len(word)
if __name__ == "__main__":   
    print(string_reverser("Hello"))
    print(word_counter("Hello i am adeeb"))
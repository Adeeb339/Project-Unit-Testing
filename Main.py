def string_reverser(text):
    text=input("Enter a string: ")
    if not text:
        return 0
    return text[::-1]
if __name__ == "__main__":   
    print(string_reverser("Hello"))
import time

def typing_speed_test(text):
    print("Type the following text as fast as you can:")
    print(text)
    input("Press enter when you're ready to start...")
    start_time=time.time()
    user_input=input("Start typing....")
    end_time=time.time()
    elapsed_time=end_time-start_time
    words=text.split()
    word_count = len(words)
    characters = len(" ".join(words))
    wpm = word_count / (elapsed_time / 60)
    accuracy = calculate_accuracy(text, user_input)
    
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Word count: {word_count}")
    print(f"Character count: {characters}")
    print(f"Typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original_text,user_text):
    original_text=original_text.lower()
    user_text=user_text.lower()
    correct_chars=sum(1 for c1,c2 in zip(original_text,user_text)if c1==c2)
    accuracy=(correct_chars/len(original_text))*100
    return accuracy

if __name__  ==  "__main__" :
    text = "This is your typing test.Type as fast as you can .It will display yor accuracy , the time you taken in this test."
    typing_speed_test(text)

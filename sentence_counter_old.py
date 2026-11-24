user_input_sentence = None
user_input_sentence_inside = None

print("This program will count how many characters you have in a sentence.")

while True:
    print("Type exit to be released from the program.\n")
    user_input_sentence = input("Enter your sentence: ")
    user_character_count_sentence = 0 # this thing should be inside the while loop

    if user_input_sentence.strip() == "": # I have tried putting None here but it still is keeping printing the there are 0 characters.
        print("\n\nPlease enter a sentence.\nCannot be blank.\n")
        continue
    if user_input_sentence.lower() == "exit":
        print("Have a great day.")
        break

    for user_character_count in user_input_sentence:
        user_character_count_sentence += 1
    print("Your sentence is :\n", user_input_sentence,)
    print("\n\nThere are", user_character_count_sentence, "characters.") # is outside for the for loop so it doesn't keep printing while it's counting and will only print when the counting has finished.
    print("\n\nTry again.")
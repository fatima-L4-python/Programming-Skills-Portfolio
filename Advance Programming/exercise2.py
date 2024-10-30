import random

#list of jokes
jokes = [
    "Why did the chicken cross the road?To get to the other side.",
    "What happens if you boil a clown?You get a laughing stock.",
    "Why did the car get a flat tire?Because there was a fork in the road!",
    "How did the hipster burn his mouth?He ate his pizza before it was cool.",
    "What did the janitor say when he jumped out of the closet?SUPPLIES!!!!",
    "Why does the golfer wear two pants?Because he's afraid he might get a 'Hole-in-one.'",
    "What did the buffalo say when his kid went to college?Bison.",
    "Why shouldn't you tell secrets in a cornfield?Too many ears.",
    "Why did the donut go to the dentist?To get a filling.",
    "Why don't scientists trust Atoms?They make up everything."
]

def tell_joke():
    while True:
        joke = random.choice(jokes) # it will select a random joke
        setup, punchline = joke.split('?') # it will split setup and punchline
        
        print(f"Setup: {setup}?") # for displaying setup
        input("Press Enter to see the punchline...")
        # for displaying punchline
        print(f"Punchline: {punchline}")
        
        # Asks if the user wants another joke
        another = input("\nWould you like to hear another joke? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

# Main program loop
if __name__ == "__main__": # checks if the script is being run directly
    print("Welcome! Ask 'Alexa tell me a Joke' to get started.") 
    while True: # creates an infinite loop that continuously waits for user input
        command = input("Enter your command: ").strip().lower() # makes sure the input is consistently organised
        if command == "alexa tell me a joke":
            tell_joke() # checks id the command is written correctly if yes it will give the output
        else:
            print("Unknown command. Please try again.") # if not it will show this

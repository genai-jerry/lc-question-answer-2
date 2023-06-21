import os
import openai

# A function that returns persona to be set for the chat. Use the type provided as input to determine the personality prompt that should be passed to OpenAI
def get_personality_prompt(type):
    # use type argument to generate different types of personalities
    if type == 1:
        # return a personality prompt for a friendly chat
        return "I am a very friendly person. I love to talk about movies and books."
    elif type == 2:
        # return a personality prompt for a professional chat
        return "I am a very professional person. I love to talk about my work and my hobbies."
    else:
        # return a personality prompt for a neutral chat
        return "I am a very neutral person. I love to talk about my work and my hobbies."

# a function to extract the choices from the OpenAI completion response
def get_choices(response):
    # get the choices from the response
    choices = response['choices']
    choice_data = ''
    for c in choices:
        choice_data = choice_data + c['text']
    return choice_data
    
# A function that returns the response from OpenAI
def get_response(training_set, prompt, type=1):
    # Using the openai library, call the completion endpoint and pass the prompt as input
    prompt = get_personality_prompt(type) + training_set + prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    return get_choices(response)

# A function to take inputs from the console. The function should append each input to an array and keep asking till users enter "quit"
def input_training_data():
    data = ''
    input_data = ''
    while input_data != 'quit':
        var = input("Enter Training Prompt: ")
        print(var)
        if var != 'quit':
            data = data + ' ' + var
        else:
            input_data = var
    return data

# A function that will take the prompt as input from the user
def input_prompt():
    var = input("Please enter your prompt: ")
    return var

def input_personality():
    var = input("What sort of personality do you want. 1. Friendly, 2. Professional, 3. Neutral. Make your choice")
    return var

# read the API key from the environment variable
var = input("Please enter your openAI key: ")
openai.api_key = var
print(openai.api_key)

training_set = input_training_data()
print(training_set)
prompt = input_prompt()
personality_type = input_personality()

response = get_response(training_set, prompt, personality_type)
print(response)



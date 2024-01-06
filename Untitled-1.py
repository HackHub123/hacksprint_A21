def medical_chatbot(user_input):
     user_input = user_input.lower()
     if 'headache' in user_input:
        return "it could be due to various reason.havey you had enough water today?"
     elif'fever' in user_input:
        return"Fever might indicate an infection.Have you measured your temperature?"
     elif 'symptom' in user_input:
        return"I'm not a doctor, but i can try to help.what symptoms are you experiencing?"
     else:
        return"I'm not sure how to respond.it's best to consult a healthcare professional."
user_input = input("user:")
response = medical_chatbot(user_input)
print("chatbot:", response)
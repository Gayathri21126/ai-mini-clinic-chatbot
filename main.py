import re

def preprocess_input(user_input):

    user_input = user_input.lower()
    user_input = re.sub(r'[^a-zA-Z\s]', '', user_input)
    return user_input


def detect_symptom(user_input):

    if "fever" in user_input:
        return "fever"
    elif "cold" in user_input or "cough" in user_input:
        return "cold"
    elif "headache" in user_input:
        return "headache"
    elif "stomach" in user_input:
        return "stomach"
    else:
        return "unknown"


def generate_response(symptom):

    responses = {
        "fever": "You may be experiencing a fever. Stay hydrated, rest well, and monitor your temperature. Consult a doctor if it exceeds 38°C.",
        "cold": "It sounds like a cold or cough. Drink warm fluids and get adequate rest. Seek medical advice if symptoms persist.",
        "headache": "For headaches, ensure hydration and proper rest. If severe or frequent, consider consulting a healthcare professional.",
        "stomach": "For stomach discomfort, avoid heavy foods and stay hydrated. If pain persists, please consult a doctor.",
        "unknown": "I'm not sure about your symptoms. Could you describe them in more detail?"
    }

    return responses[symptom]


def chatbot():
    print("AI Mini Clinic Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Describe your symptoms: ")

        if user_input.lower() == "exit":
            print("Take care! Stay healthy.")
            break

        cleaned_input = preprocess_input(user_input)
        symptom = detect_symptom(cleaned_input)
        response = generate_response(symptom)

        print("Bot:", response)
        print()


if __name__ == "__main__":
    chatbot()

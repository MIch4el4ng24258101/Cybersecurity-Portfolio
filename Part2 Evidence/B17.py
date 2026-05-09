import re

dangerous_patterns = [
    r"ignore .*instructions",
    r"reveal .*system prompt",
    r"you are now",
    r"disable .*safety",
    r"bypass .*rules",
    r"print .*confidential",
    r"forget .*previous",
    r"act as .*dan"
]

def detect_prompt_injection(user_input):
    for pattern in dangerous_patterns:
        if re.search(pattern, user_input.lower()):
            return True
    return False

def main():
    print("AI Prompt Injection Defence System")
    print("--------------------------------")

    while True:
        user_input = input("Enter prompt: ")

        if user_input.lower() == "exit":
            break

        if detect_prompt_injection(user_input):
            print("BLOCKED: Possible prompt injection detected.\n")
        else:
            print("SAFE: Prompt accepted.\n")

if __name__ == "__main__":
    main()
def create_question(question: str, choices: list, correct_answer: str):
    print(question)
    for i in range(len(choices)):
        print(f"{i+1}. {choices[i]}")

    user_input = input(": ")
    if user_input == correct_answer:
        print("You are correct!")
    else:
        print("You are wrong!!")


# print("What is Kazuya PEWGF frame?")
# print("1. 13")
# print("2. 14")
# print("3. 15")
# print("4. 16")

create_question("What is Kazuya PEWGF frame?", ["13", "14", "bob", "lars", "Jin"], "13")
create_question("What is the fastest Lars stading launcher?", ["13", "14", "15", "16", "17"], "14")
create_question("What is the fastest Lars stading launcher?", ["13", "14", "15", "16", "17"], "14")


def main():
    question = input("Who are you? ").strip().title()
    hi(question)


def hi(to="Student"):
    print("hi,", to)

main()




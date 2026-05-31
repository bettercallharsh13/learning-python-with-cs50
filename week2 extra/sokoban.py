def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "undo":
            history.pop()
        elif action == "restart":
            history.clear()
        else:
            history.append(action)

        print(history)


main()

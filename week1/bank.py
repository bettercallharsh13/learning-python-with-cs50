text = input("Greeting : ").lower()

if "hello" in text:
    print("$0")
elif text.startswith("h") and "hello" not in text:
    print("$20")
else:
    print("$100")

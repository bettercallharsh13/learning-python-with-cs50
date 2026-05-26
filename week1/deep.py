answer = input("what is the answer to hte great question of life, the universe, and everything? :").strip().lower()

answer = answer.replace("-"," ")

if answer == "42" and "forty two":
    print("yes")
else:
    print("no")



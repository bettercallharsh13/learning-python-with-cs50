
hindi_marks = int(input("enter your score of hindi :"))
english_marks = int(input("enter your scoreof english :"))
maths_marks = int(input("enter your score of maths :"))
physics_marks = int(input("enter your score of physics :"))
chemistry_marks = int(input("enter your score of chemistry :"))

x = float((hindi_marks + english_marks + maths_marks + physics_marks + chemistry_marks) / 5)
y = float((maths_marks + physics_marks + chemistry_marks) / 3)

if 33 <= hindi_marks <= 100 and 33 <= english_marks <= 100 and 33 <= physics_marks < 100 and 33 <= chemistry_marks <= 100 and 33 <= maths_marks <= 100:

    print(f"congrades you are got pass with {x}%")
    print(f"your main subject score is {y}%")


elif x <= 33:
    print("you are in fail ")

def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text



def main():
    x = input("enter your text")
    print(convert(x))


main()

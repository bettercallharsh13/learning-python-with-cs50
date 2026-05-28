distance = {"f1" : 200,
            "f2" : 220,
            "f3" : 230,
            "f4" : 240}

def main():
    for x in distance.values():
        print(f"{x} au is {convert(x)}m")




def convert(au):
    return au * 200000


main()

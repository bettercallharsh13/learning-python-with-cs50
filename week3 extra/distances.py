distances = {
    "harsh 1" : "84",
    "amit 4" : "80",
    "manjeet 3" : "77",
    "kapil 4" : "90",
    "somraj 5" : "33"
    }

def main():

     name = input("Enter your name : ")

     try:
          au = float(distances[name])
     except KeyError:
          print(f"{name} is not in list")
     except ValueError:
          print(f"can't convert '{distances[name]}' to a float")
          return

     m = convert(au)
     print(f"{m}m away")

def convert(au):
     return au * 100000


main()

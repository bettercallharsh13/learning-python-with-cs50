def main():
    space = {"name" : "harsh" , "distance" : 40}
    print(create_report(space))


def create_report(space):
    return f"""

    name: {space["name"]}
    distane: {space["distance"]}
    """

main()


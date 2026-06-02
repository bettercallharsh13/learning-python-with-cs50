def main():
    pace = get_pace(miles=33.3, minutes=0)
    print(f"you need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Invalid value")
    return minutes / miles


main()

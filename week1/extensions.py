text = input("enter your file name : ").strip().lower()

if text.endswith(".jpg") or text.endswith(".jpeg"):
    print("image/jpeg")

elif text.endswith(".pdf") or text.endswith(".PDF"):
    print("application/pdf")

elif text.endswith(".png"):
    print("image/png")

elif text.endswith("txt"):
    print("text/plain")

elif text.endswith(".gif"):
    print("image/gif")

elif text.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")

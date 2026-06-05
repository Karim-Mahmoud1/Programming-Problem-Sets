Filename = input("Filename: ").strip().lower()

if Filename.endswith(".gif"):
    print("image/gif")
elif Filename.endswith(".jpg"):
    print("image/jpeg")
elif Filename.endswith(".jpeg"):
    print("image/jpeg")
elif Filename.endswith(".png"):
    print("image/png")
elif Filename.endswith(".pdf"):
    print("application/pdf")
elif Filename.endswith(".txt"):
    print("text/txt")
elif Filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
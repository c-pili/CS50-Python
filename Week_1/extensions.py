file = input("File name: ").lower().

match file:
    case ".gif":
        print("image/gif")

    case ".jpg":
        print("image/jpeg")

    case ".jpeg":
        print("image/jpeg")

    case ".png":
        print("image/png")

    case ".pdf":
        print("application/pdf")

    case ".txt":
        print("application/txt")

    case ".zip":
        print("application/zip")




file = input("File name: ").lower()

name, file = file.split(".")

match file:
    case "gif":
        print("image/gif")

    case "jpg":
        print("image/jpeg")

    case "jpeg":
        print("image/jpeg")

    case "png":
        print("image/png")

    case "pdf":
        print("application/pdf")

    case "txt":
        print("text/plain")

    case "zip":
        print("application/zip")

    case "bin":
        print("application/octet-stream")




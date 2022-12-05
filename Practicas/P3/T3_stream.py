import os


def task3(input_path: str, ip: str):
    command = f"ffmpeg -re -i {input_path} -c copy -f flv" \
              f" rtmp://{ip}/live/sample"
    os.system(command)


if __name__ == "__main__":
    path = ""
    print("Type the path to the file that you want to stream: ")

    valid_path = False
    while not valid_path:
        path = input("Path: ")
        valid_path = os.path.isfile(path)
        if not valid_path:
            print("File not found, try again.")

    ip = input("Enter the local IP address of your computer"
               " (so that you can access the stream from other"
               " devices in your network), e.g: 192.168.1.38: ")
    task3(path, ip)

import os

ENCRYPTION_KEY = "121a0fca0f1b475b8910297fa8e0a07e" + \
                 ":a0a1a2a3a4a5a6a7a8a9aaabacadaeaf"


def create_mpd(path: str, encrypt=False):
    # Fragment the input file
    os.system(f"mp4fragment {path} fragmented_file.mp4")
    # Encrypt (using the automatic encryption by MPEG DASH) and generate
    # MPD presentation
    if encrypt:
        os.system(f"mp4dash "
                  f"--encryption-key={ENCRYPTION_KEY} fragmented_file.mp4")
    if not encrypt:
        os.system(f"mp4dash fragmented_file.mp4")


if __name__ == "__main__":
    path = ""
    print("Type the path to the file that you want to fragment,"
          " encrypt and dash.")
    valid_path = False
    while not valid_path:
        path = input("Path: ")
        valid_path = os.path.isfile(path)
        if not valid_path:
            print("File not found, try again.")
    option = ""
    while option not in ("0", "1"):
        option = input("Type 1 to encrypt the file, type 0 not to encrypt: ")
        create_mpd(path, option == "1")

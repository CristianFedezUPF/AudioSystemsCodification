def run_length_encoder(sequence):
    """ Encodes a sequence with run-length encoding.

        Input:
            sequence (String): String to be encoded
    """
    output = ""
    temp = sequence[0]
    counter = 0
    for character in sequence:
        if character == temp:
            counter += 1
        else:
            output += str(counter) + temp
            counter = 1
            temp = character
    output += str(counter) + temp
    return output


def run_length_decoder(sequence):
    """ Decodes a sequence that was encoded with run-length encoding.

        Input:
            sequence (String): String to be decoded
    """
    output = ""
    for length, character in zip(sequence[0::2], sequence[1::2]):
        output += int(length)*character
    return output


sample = "aaaaabbbbcaaaabbbdddddddmmmmmmzzzzzzlllllllallooooolls"
print("\nOriginal sequence: ")
print(sample + "\n")

encoded = run_length_encoder(sample)
print("Encoded sequence with a run-length encoder: ")
print(encoded + "\n")

decoded = run_length_decoder(encoded)
print("Decoded sequence with a run-length decoder: ")
print(decoded)

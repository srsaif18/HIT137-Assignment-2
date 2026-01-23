# Group Members:
# Mou Rani Biswas - 398778
# MD Saifur Rahman - 398921
# Nahid Hasan Sangram - 395231
# Mohammed Rifatul Alam - 399533
#
# HIT137 Assignment 2
# Question 1 – Part 3: Decryption + verification

def get_shifts():
    while True:
        try:
            shift1 = int(input("Enter shift1: ").strip())
            shift2 = int(input("Enter shift2: ").strip())
            return shift1, shift2
        except ValueError:
            print("Please enter valid integers.")


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def shift_alpha(ch, shift, base):
    """Shift character within full alphabet (wrap around)."""
    return chr(base + (ord(ch) - base + shift) % 26)


def encrypt_text(text, shift1, shift2):
    encrypted = []
    for ch in text:
        if 'a' <= ch <= 'z':
            # a-m: forward by shift1*shift2, n-z: backward by shift1+shift2
            shift = (shift1 * shift2) if ('a' <= ch <= 'm') else -(shift1 + shift2)
            encrypted.append(shift_alpha(ch, shift, ord('a')))

        elif 'A' <= ch <= 'Z':
            # A-M: backward by shift1, N-Z: forward by shift2^2
            shift = (-shift1) if ('A' <= ch <= 'M') else (shift2 ** 2)
            encrypted.append(shift_alpha(ch, shift, ord('A')))

        else:
            encrypted.append(ch)

    return ''.join(encrypted)


def decrypt_text(text, shift1, shift2):
    decrypted = []
    for ch in text:
        if 'a' <= ch <= 'z':
            # reverse of encryption shifts
            shift = -(shift1 * shift2) if ('a' <= ch <= 'm') else (shift1 + shift2)
            decrypted.append(shift_alpha(ch, shift, ord('a')))

        elif 'A' <= ch <= 'Z':
            # reverse of encryption shifts
            shift = (shift1) if ('A' <= ch <= 'M') else -(shift2 ** 2)
            decrypted.append(shift_alpha(ch, shift, ord('A')))

        else:
            decrypted.append(ch)

    return ''.join(decrypted)


def main():
    shift1, shift2 = get_shifts()

    raw_text = read_file("raw_text.txt")

    # Encrypt and write encrypted file
    encrypted_text = encrypt_text(raw_text, shift1, shift2)
    write_file("encrypted_text.txt", encrypted_text)

    # Read encrypted file, decrypt, and write decrypted file
    encrypted_from_file = read_file("encrypted_text.txt")
    decrypted_text = decrypt_text(encrypted_from_file, shift1, shift2)
    write_file("decrypted_text.txt", decrypted_text)

    # Verification
    if decrypted_text == raw_text:
        print("✅ Decryption successful: decrypted_text.txt matches raw_text.txt")
    else:
        print("❌ Decryption failed: decrypted_text.txt does NOT match raw_text.txt")


if __name__ == "__main__":
    main()

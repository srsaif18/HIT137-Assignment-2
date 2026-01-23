# Group Members:
# Mou Rani Biswas - 398778
# MD Saifur Rahman - 398921
# Nahid Hasan Sangram - 395231
# Mohammed Rifatul Alam - 399533
#
# HIT137 Assignment 2
# Question 1 – Part 2: Implement encryption logic

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
        # Lowercase letters
        if 'a' <= ch <= 'z':
            if 'a' <= ch <= 'm':
                shift = shift1 * shift2        # forward
            else:
                shift = -(shift1 + shift2)     # backward
            encrypted.append(shift_alpha(ch, shift, ord('a')))

        # Uppercase letters
        elif 'A' <= ch <= 'Z':
            if 'A' <= ch <= 'M':
                shift = -shift1                # backward
            else:
                shift = shift2 ** 2            # forward (square)
            encrypted.append(shift_alpha(ch, shift, ord('A')))

        # Other characters remain unchanged
        else:
            encrypted.append(ch)

    return ''.join(encrypted)


def main():
    shift1, shift2 = get_shifts()

    raw_text = read_file("raw_text.txt")

    encrypted_text = encrypt_text(raw_text, shift1, shift2)
    write_file("encrypted_text.txt", encrypted_text)

    print("✅ Q1 Part 2 complete: encrypted_text.txt created.")


if __name__ == "__main__":
    main()

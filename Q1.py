# Group Members:
# Mou Rani Biswas - 398778
# MD Saifur Rahman - 398921
# Nahid Hasan Sangram - 395231
# Mohammed Rifatul Alam - 399533

def get_shifts():
    while True:
        try:
            shift1 = int(input("Enter shift1: ").strip())
            shift2 = int(input("Enter shift2: ").strip())
            return shift1, shift2
        except ValueError:
            print("Please enter valid integers.")


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def encrypt_text_placeholder(text, shift1, shift2):
    return text  # commit 1 placeholder


def main():
    shift1, shift2 = get_shifts()
    raw_text = read_file("raw_text.txt")

    encrypted = encrypt_text_placeholder(raw_text, shift1, shift2)
    write_file("encrypted_text.txt", encrypted)

    print("✅ Commit 1 complete: encrypted_text.txt created (placeholder).")


if __name__ == "__main__":
    main()

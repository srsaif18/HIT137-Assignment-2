# q1_encrypt.py
# HIT137 Assignment 2 - Question 1 (Commit 1)
# Goal: read raw_text.txt, ask for shift keys, create encrypted_text.txt (placeholder encryption)
 
def get_shifts():
    """Ask the user for shift1 and shift2 and return them as integers."""
    while True:
        try:
            shift1 = int(input("Enter shift1 (number): ").strip())
            shift2 = int(input("Enter shift2 (number): ").strip())
            return shift1, shift2
        except ValueError:
            print("Please enter valid whole numbers (e.g., 3, 10).")
 
 
def read_file(path):
    """Read and return the full content of a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 
 
def write_file(path, content):
    """Write content to a text file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
 
 
def encrypt_text_placeholder(text, shift1, shift2):
    """
    Placeholder encryption for Commit 1.
    For now: returns the text unchanged.
    In Commit 2, we will implement the real shifting rules.
    """
    return text
 
 
def main():
    shift1, shift2 = get_shifts()
 
    raw_text = read_file("raw_text.txt")
 
    encrypted_text = encrypt_text_placeholder(raw_text, shift1, shift2)
 
    write_file("encrypted_text.txt", encrypted_text)
 
    print("✅ Commit 1 done: encrypted_text.txt created (placeholder encryption).")
 
 
if __name__ == "__main__":
    main()
 

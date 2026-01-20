"""
Group 13 Members: 
1. Nahid Hasan Sangram
2. Mou Rani Biswas  
3. Md Saifur Rahman
4. Mohammed Rifatul Alam

Our thinking Process:
1. First, understand the encryption rules
2. Need to handle different cases: lowercase (a-m vs n-z) and uppercase (A-M vs N-Z)
3. Implement wrap-around for alphabet shifts (z→a or a→z)
4. Create three main functions: encrypt, decrypt, and verify
5. The decryption should reverse the encryption logic exactly

Prompts Used for help:
1. "Implement Caesar cipher with different shifts based on letter position in alphabet"
2. "Adding wrap-around functionality for alphabet shifts"
3. "file comparison function to verify encryption/decryption"
4. "Handle edge cases: non-alphabet characters, negative shifts, large shifts"
"""

import os

def get_shifted_char(char, shift1, shift2, encrypt_mode=True):
    """
    Encrypt or decrypt a single character based on the rules.
    encrypt_mode=True for encryption, False for decryption
    """
    if not char.isalpha():
        return char
    
    is_lower = char.islower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if is_lower:
        index = alphabet.index(char.lower())
        
        # Check if in first half (a-m)
        if index < 13:  # a-m (0-12)
            if encrypt_mode:
                shift = shift1 * shift2
                new_index = (index + shift) % 26
            else:
                # Reverse the encryption: shift backward by shift1*shift2
                shift = shift1 * shift2
                new_index = (index - shift) % 26
        else:  # n-z (13-25)
            if encrypt_mode:
                shift = shift1 + shift2
                new_index = (index - shift) % 26
            else:
                # Reverse the encryption: shift forward by shift1+shift2
                shift = shift1 + shift2
                new_index = (index + shift) % 26
        
        return alphabet[new_index] if is_lower else alphabet[new_index].upper()
    
    else:  # Uppercase
        index = alphabet.index(char.lower())
        
        # Check if in first half (A-M)
        if index < 13:  # A-M (0-12)
            if encrypt_mode:
                shift = shift1
                new_index = (index - shift) % 26
            else:
                # Reverse the encryption: shift forward by shift1
                shift = shift1
                new_index = (index + shift) % 26
        else:  # N-Z (13-25)
            if encrypt_mode:
                shift = shift2 ** 2
                new_index = (index + shift) % 26
            else:
                # Reverse the encryption: shift backward by shift2²
                shift = shift2 ** 2
                new_index = (index - shift) % 26
        
        return alphabet[new_index].upper()

def encrypt_file(input_file, output_file, shift1, shift2):
    """Encrypt the content of input_file and write to output_file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        encrypted_chars = []
        for char in content:
            encrypted_chars.append(get_shifted_char(char, shift1, shift2, encrypt_mode=True))
        
        encrypted_content = ''.join(encrypted_chars)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encrypted_content)
        
        print(f"Encryption complete! Encrypted file saved as '{output_file}'")
        return True
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return False
    except Exception as e:
        print(f"Error during encryption: {e}")
        return False

def decrypt_file(input_file, output_file, shift1, shift2):
    """Decrypt the content of input_file and write to output_file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        decrypted_chars = []
        for char in content:
            decrypted_chars.append(get_shifted_char(char, shift1, shift2, encrypt_mode=False))
        
        decrypted_content = ''.join(decrypted_chars)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decrypted_content)
        
        print(f"Decryption complete! Decrypted file saved as '{output_file}'")
        return True
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return False
    except Exception as e:
        print(f"Error during decryption: {e}")
        return False

def verify_files(file1, file2):
    """Compare two files to check if they are identical."""
    try:
        with open(file1, 'r', encoding='utf-8') as f1, \
             open(file2, 'r', encoding='utf-8') as f2:
            content1 = f1.read()
            content2 = f2.read()
        
        if content1 == content2:
            print("✓ SUCCESS: Decryption verified! The decrypted file matches the original.")
            return True
        else:
            print("✗ FAILURE: Decryption failed! The decrypted file does NOT match the original.")
            
            # Optional: Show first difference
            for i, (c1, c2) in enumerate(zip(content1, content2)):
                if c1 != c2:
                    print(f"First difference at position {i}: '{c1}' vs '{c2}'")
                    break
            
            return False
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False

def main():
    """Main program execution."""
    print("=== Text Encryption/Decryption Program ===")
    print("Rules:")
    print("- Lowercase a-m: shift forward by shift1 × shift2")
    print("- Lowercase n-z: shift backward by shift1 + shift2")
    print("- Uppercase A-M: shift backward by shift1")
    print("- Uppercase N-Z: shift forward by shift2²")
    print("- Non-alphabet characters remain unchanged")
    print()
    
    # Get user input for shift values
    try:
        shift1 = int(input("Enter shift1 value (integer): "))
        shift2 = int(input("Enter shift2 value (integer): "))
    except ValueError:
        print("Error: Please enter valid integer values for shifts.")
        return
    
    # File names
    input_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found in the current directory.")
        return
    
    print("\n" + "="*50)
    print("Step 1: Encrypting raw_text.txt...")
    encrypt_success = encrypt_file(input_file, encrypted_file, shift1, shift2)
    
    if not encrypt_success:
        return
    
    print("\n" + "="*50)
    print("Step 2: Decrypting encrypted_text.txt...")
    decrypt_success = decrypt_file(encrypted_file, decrypted_file, shift1, shift2)
    
    if not decrypt_success:
        return
    
    print("\n" + "="*50)
    print("Step 3: Verifying decryption...")
    verify_files(input_file, decrypted_file)
    
    print("\n" + "="*50)
    print("Process completed!")
    
    # Show sample of each file
    if os.path.exists(encrypted_file) and os.path.exists(decrypted_file):
        print("\nSample output:")
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                original_sample = f.read(100)
            
            with open(encrypted_file, 'r', encoding='utf-8') as f:
                encrypted_sample = f.read(100)
            
            with open(decrypted_file, 'r', encoding='utf-8') as f:
                decrypted_sample = f.read(100)
            
            print(f"Original (first 100 chars):\n{original_sample}")
            print(f"\nEncrypted (first 100 chars):\n{encrypted_sample}")
            print(f"\nDecrypted (first 100 chars):\n{decrypted_sample}")
        except:
            pass

if __name__ == "__main__":
    main()
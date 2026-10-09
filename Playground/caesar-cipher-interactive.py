# ==============================================================
# CAESAR CIPHER — Complete Interactive Version
# ==============================================================
# This program:
#   1. Takes YOUR TEXT + SHIFT NUMBER to ENCRYPT
#   2. Takes ENCRYPTED TEXT + SAME SHIFT to DECRYPT
#   3. Keeps numbers, spaces, symbols unchanged
#   4. Preserves uppercase/lowercase
# ==============================================================


def caesar(text, shift, encrypt=True):
    """
    Core Caesar Cipher function — used by both encrypt and decrypt.

    Parameters:
        text    -- the string to process
        shift   -- number of positions to move (1–25)
        encrypt -- True = encode, False = decode
    """

    # --- INPUT VALIDATION ---
    # Shift must be an integer
    if not isinstance(shift, int):
        return '⚠️ Shift must be an integer value.'
    # Shift must be between 1–25 (avoids full-cycle shifting)
    if shift < 1 or shift > 25:
        return '⚠️ Shift must be a number between 1 and 25.'

    # --- DEFINE THE ALPHABET ---
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # --- FOR DECRYPTION: REVERSE THE SHIFT ---
    if not encrypt:
        shift = - shift  # e.g. shift=3 → becomes -3 (moves backward)

    # --- CREATE THE SHIFTED ALPHABET ---
    # Example: shift=3 → abcdef... becomes defgh...abc
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # --- CREATE TRANSLATION TABLE ---
    # Maps lowercase → shifted-lower, AND uppercase → shifted-uppercase
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # --- APPLY THE TRANSLATION ---
    # Numbers, spaces, symbols NOT in table → stay exactly the same
    result = text.translate(translation_table)

    return result


def encrypt(text, shift):
    """Helper: Encrypt text with given shift"""
    return caesar(text, shift, encrypt=True)


def decrypt(text, shift):
    """Helper: Decrypt text with given shift"""
    return caesar(text, shift, encrypt=False)


# ==============================================================
# 🎮 INTERACTIVE MAIN PROGRAM
# ==============================================================

if __name__ == "__main__":

    print("===== CAESAR CIPHER TOOL =====\n")

    # ---------- ENCRYPTION SECTION ----------
    print("--- 🔒 ENCRYPT TEXT ---")
    plain_text = input("Enter text to encrypt: ")

    # Safe way to get shift number
    while True:
        try:
            shift_input = input("Enter shift number (1–25): ")
            shift_value = int(shift_input)
            if 1 <= shift_value <= 25:
                break
            print("❌ Please enter a number between 1 and 25!")
        except ValueError:
            print("❌ That's not a valid whole number! Try again.")

    encrypted_result = encrypt(plain_text, shift_value)
    print(f"\n✅ Encrypted: {encrypted_result}")

    # ---------- DECRYPTION SECTION ----------
    print("\n--- 🔓 DECRYPT TEXT ---")
    cipher_text = input("Enter text to decrypt: ")

    # Use same shift number (or let user enter again)
    while True:
        try:
            shift_decrypt_input = input(
                "Enter the SAME shift number used to encrypt: ")
            shift_decrypt_value = int(shift_decrypt_input)
            if 1 <= shift_decrypt_value <= 25:
                break
            print("❌ Please enter a number between 1 and 25!")
        except ValueError:
            print("❌ That's not a valid whole number! Try again.")

    decrypted_result = decrypt(cipher_text, shift_decrypt_value)
    print(f"\n✅ Decrypted: {decrypted_result}")

    print("\n===== DONE =====")

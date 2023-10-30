from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import os
import getpass

# Anahtar oluştur (RSA için)
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    with open("private_key.pem", "wb") as key_file:
        key_file.write(private_key)
    
    public_key = key.publickey().export_key()
    with open("public_key.pem", "wb") as key_file:
        key_file.write(public_key)

# Anahtarları yükle (RSA için)
def load_keys():
    if os.path.exists("private_key.pem") and os.path.exists("public_key.pem"):
        private_key = RSA.import_key(open("private_key.pem").read())
        public_key = RSA.import_key(open("public_key.pem").read())
        return private_key, public_key
    else:
        return None, None

# Metni RSA ile şifrele
def rsa_encrypt_text(public_key, text):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_text = cipher.encrypt(text.encode())
    return encrypted_text

# Metni RSA ile çöz
def rsa_decrypt_text(private_key, encrypted_text):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    return decrypted_text

# Metni AES ile şifrele
def aes_encrypt_text(key, text):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    encrypted_text = nonce + ciphertext + tag
    return encrypted_text

# Metni AES ile çöz
def aes_decrypt_text(key, encrypted_text):
    nonce = encrypted_text[:16]
    ciphertext = encrypted_text[16:-16]
    tag = encrypted_text[-16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_text = cipher.decrypt_and_verify(ciphertext, tag).decode()
    return decrypted_text

# Ana menüyü göster
def show_menu(private_key, public_key, aes_key):
    while True:
        print("\nMain Menu:")
        print("1. Encrypt Text and Save")
        print("2. Decrypt Encrypted Text")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            title = input("Enter the title of the encrypted text: ")
            text = input("Enter the text you want to encrypt: ")
            
            # Encrypt the text using AES
            encrypted_text = aes_encrypt_text(aes_key, text)
            
            # Save the encrypted text to a file with the .protext extension
            filename = title + ".protext"
            with open(filename, "wb") as file:
                file.write(encrypted_text)
            
            print("Encrypted text title:", title)
            print("Encrypted text saved as", filename)

        elif choice == '2':
            filename = input("Enter the name of the file to decrypt: ")
            try:
                with open(filename, "rb") as file:
                    encrypted_text = file.read()
                    decrypted_text = aes_decrypt_text(aes_key, encrypted_text)
                    print("Decrypted text:")
                    print(decrypted_text)
            except FileNotFoundError:
                print("File not found.")

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

# Anahtar oluşturun veya yükleyin (RSA için)
private_key, public_key = load_keys()
if private_key is None or public_key is None:
    generate_keys()
    private_key, public_key = load_keys()
    print("RSA keys generated and saved.")

# AES anahtar oluşturun (256 bitlik bir anahtar)
aes_key = get_random_bytes(32)

# Master şifresini kontrol et
failed_attempts = 0
while True:
    if os.path.exists("master_password.txt"):
        with open("master_password.txt", "rb") as password_file:
            encrypted_data = password_file.read()
            decrypted_data = rsa_decrypt_text(private_key, encrypted_data)
            saved_username, master_password = decrypted_data.split('\n')
            entered_username = input("Enter your username: ")
            entered_password = getpass.getpass("Enter your master password: ")
            if entered_username == saved_username and entered_password == master_password:
                print("Login successful.")
                print(f"Username: {saved_username}")
                show_menu(private_key, public_key, aes_key)
                break
            else:
                failed_attempts += 1
                print("Incorrect username or password. Please try again.")
                if failed_attempts >= 4:
                    print("Too many incorrect attempts. Exiting...")
                    break
    else:
        print("No master password found. Please create a master password.")
        username = input("Enter your username: ")
        master_password = getpass.getpass("Enter a master password: ")
        encrypted_data = f"{username}\n{master_password}"
        encrypted_data = rsa_encrypt_text(public_key, encrypted_data)
        with open("master_password.txt", "wb") as password_file:
            password_file.write(encrypted_data)
        print("Master password set.")

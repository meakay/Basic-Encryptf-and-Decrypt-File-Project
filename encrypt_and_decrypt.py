from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()
    else:
        key = generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
        return key

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as f:  # Şifrelenmiş dosyayı orijinal dosyanın yanına kaydet
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as f:
        f.write(decrypted_data)

def main():
    key_file = "encryption_key.key"
    key = load_key(key_file)

    while True:
        choice = input("Ne yapmak istersiniz? (encrypt/decrypt/exit): ").lower()
        
        if choice == 'encrypt':
            file_path = input("Şifrelemek istediğiniz dosyanın yolunu girin: ")
            encrypt_file(file_path, key)
            print("Dosya başarıyla şifrelendi.")
        elif choice == 'decrypt':
            file_path = input("Çözmek istediğiniz dosyanın yolunu girin: ")
            decrypt_file(file_path, key)
            print("Dosya başarıyla çözüldü.")
        elif choice == 'exit':
            break
        else:
            print("Geçersiz bir seçenek girdiniz.")

if __name__ == "__main__":
    main()

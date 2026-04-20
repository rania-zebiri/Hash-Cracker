import hashlib

def crack_hash(target_hash, wordlist_path, hash_type):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for line in file:
                word = line.strip()
                if hash_type == 'md5':
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                
                if hashed_word == target_hash:
                    print(f"\n[+] Password Found: {word}")
                    return word
        print("\n[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("[!] Error: Wordlist file not found.")

def main():
    print("--- CTF Hash Cracker ---")
    h = input("Enter hash to crack: ").strip()
    w = input("Enter wordlist path: ").strip()
    t = input("Enter type (md5, sha1, sha256): ").lower()
    crack_hash(h, w, t)

if __name__ == "__main__":
    main()
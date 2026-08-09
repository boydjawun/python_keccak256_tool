from Crypto.Hash import keccak #pip install pycryptodome
import pyfiglet #pip install pyfiglet

def keccak256(word: str) -> str:
    k = keccak.new(digest_bits=256)
    k.update(word.encode())
    return k.hexdigest()

def main():
    print(pyfiglet.figlet_format("keccak256", font="doom")) #figlet banner

    user_input = input("Enter a word to hash with Keccak256: ").strip() #.strip() removes leading and trailing whitespace
    hashed = keccak256(user_input)
    print(f"keccak256 hash: {hashed}")

if __name__ == "__main__":
    main()
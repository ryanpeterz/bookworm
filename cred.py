import openai
import keyring

user = "ryanpeterz"

def main(cred: str):
    openai.organization = keyring.get_password(cred, "org")
    openai.api_key = keyring.get_password(cred, "key")


main(keyring.get_password("cred", user))


if __name__ == "__main__":
    print(f"cred: {keyring.get_password('cred', user)}")


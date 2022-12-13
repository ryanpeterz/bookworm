import openai
import keyring

def main(cred: str):
    openai.organization = keyring.get_password(cred, "org")
    openai.api_key = keyring.get_password(cred, "key")

main("bookworm")

if __name__ == "__main__":
    raise NotImplementedError(
        "Guided credential storage not yet implemented :/")


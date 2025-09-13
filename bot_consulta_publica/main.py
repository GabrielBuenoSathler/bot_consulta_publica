import os
from dotenv import load_dotenv


def main():
    load_dotenv()  # take variables from .env.
    my_var = os.getenv("MY_VAR")
    print("rodando meu codigo")
    print(f"MY_VAR = {my_var}")


main()

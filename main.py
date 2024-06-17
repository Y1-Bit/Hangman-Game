from colorama import init

from constants import STAGES
from game import Hangman


def get_wordlist() -> list[str]:
    with open("nouns.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()


def main() -> None:
    init(autoreset=True)
    word_list: list[str] = get_wordlist()
    hangman = Hangman(word_list, STAGES)
    hangman.launch()


if __name__ == "__main__":
    main()

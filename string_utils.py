def is_palindrome(text: str) -> bool:
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))


def count_vowels(text: str) -> int:
    return sum(1 for c in text.lower() if c in "aeiou")

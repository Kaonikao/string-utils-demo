from string_utils import is_palindrome, reverse_words, count_vowels


def test_is_palindrome_true():
    assert is_palindrome("A man a plan a canal Panama")


def test_is_palindrome_false():
    assert not is_palindrome("hello world")


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"


def test_count_vowels():
    assert count_vowels("Hello World") == 3

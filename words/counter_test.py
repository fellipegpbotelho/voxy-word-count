from .counter import count_words


def test_count_words_one():
    result = count_words(text="word")

    assert result == 1


def test_count_words_two():
    result = count_words(text="word word")

    assert result == 2


def test_count_words_many():
    result = count_words(text="word word word word word word word word word word")

    assert result == 10


def test_count_words_ignore_spaces():
    result = count_words(text="word            word")

    assert result == 2

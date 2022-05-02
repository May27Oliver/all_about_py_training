from typing import List, Callable

# Callable[[ParamType1, ParamType2, .., ParamTypeN], ReturnType]


def edit_story(words: List[str], func: Callable[[str], str]):
    for word in words:
        print(func(word))


def enliven(word: str):
    return word.capitalize()+'!'


stairs = ['thud', 'meow', 'thud', 'hiss']

edit_story(stairs, lambda word: word.capitalize() + '!')

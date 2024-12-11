import requests
from googletrans import Translator
from googletrans import LANGUAGES


def parts_of_language():
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def translate_joke(text, language):
    translator = Translator()
    translated = translator.translate(text, src='en', dest=language)
    return translated.text


if __name__ == '__main__':
    lang = input("На каком языке хотите шутку?")
    try:
        for i in range(3):
            joke = get_joke()
            joke_ask =joke["setup"]
            joke_answer=joke["punchline"]

            print(translate_joke(f'{joke_ask}\n{joke_answer}', lang), "\n")
    except ConnectionError:
        print("Check your Internet")
    except ValueError:
        print("Make sure language wrote correct this is list of parts of languages:","\n")
        parts_of_language()
import requests
from googletrans import Translator



def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    response.raise_for_status()
    something = response.json()
    return something

def translate_to_russian(text,language):
    translator = Translator()
    translated = translator.translate(text, src='en', dest=language)
    return translated.text
if __name__ == '__main__':

    try:
        lang = input("На каком языке хотите шутку?")
        print(translate_to_russian(get_joke()["setup"],lang),
              translate_to_russian(get_joke()["punchline"],lang),"\n",translate_to_russian(get_joke()["setup"],lang),
              translate_to_russian(get_joke()["punchline"],lang),"\n",translate_to_russian(get_joke()["setup"],lang),
              translate_to_russian(get_joke()["punchline"],lang),sep="\n")
    except:
        print("Error check your Internet or make sure language wrote correct")

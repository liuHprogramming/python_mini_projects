from googletrans import Translator

translator = Translator()

language = {
            "bn": "Bangla",
            "en": "English",
            "ko": "Koren",
            "fr": "French",
            "de": "German",
            "he": "Hebrew",
            "hi": "Hindi",
            "it": "Italian",
            "ja": "Japanese",
            'la': "Latin",
            "ms": "Malay",
            "ne": "Nepali",
            "ru": "Russian",
            "ar": "Arabic",
            "zh": "Chinese",
            "es": "Spanish"
}

allow = True    # Variable to control correct language code input
while allow:    # control if the language code input is valid

    user_code = input("Please give us the code of language you want to translate, "
                     "enter 'opinion' if you want to see the code list.")

    if user_code == 'opinion':
        print("The code list is\n")

        for key, val in language.items():
            print(f"{key} -> {val}")
            print("\n")

    else:   # validating the input
        for lan_code in language:
            if lan_code == user_code:
                print("The language code you have gived is valid!")
                allow = False

        if allow:
            print("The language code you have gived is not valid!")

while True:  # start translate loop
    string = input("Please give us the text you want to translate: ")

    if string == 'close':
        print("Have a nice day!")
        break

    translated = translator.translate(string, dest=user_code)

    # print translated text
    print(f"{language[user_code]}->Translation: {translated.text}")
    # print pronunciation
    print(f"Pronunciation: {translated.pronunciation}")

    for key, val in language.items():   # checking if the source language is on the language list dict and printing it
        if key == translated.src:   # if user language code is equal to source language code
            print(f"Translated from: {val}\n")


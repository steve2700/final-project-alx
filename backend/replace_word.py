import requests

def replace_words(text, word):
    # Make a request to the Datamuse API to get synonyms for the word
    url = f"https://api.datamuse.com/words?rel_syn={word}"
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the synonyms from the API response
        synonyms = [result['word'] for result in response.json()]

        # Replace the word with a random synonym in the text
        replaced_text = text.replace(word, synonyms[0]) if synonyms else text
        return replaced_text
    else:
        print("Error occurred during the API request:", response.status_code)

def main():
    text = input("Enter some text: ")
    word = input("Enter the word to replace: ")
    replaced_text = replace_words(text, word)
    print("Replaced text:", replaced_text)

if __name__ == "__main__":
    main()


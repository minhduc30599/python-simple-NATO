import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_word = input('Input your word: ').upper()
    try:
        output_list = [data_dict[letter] for letter in user_word]
    except KeyError:
        print('Your input is invalid')
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()

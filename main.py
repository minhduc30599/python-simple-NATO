import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_word = input('Input your word: ').upper()
output_list = [data_dict[letter] for letter in user_word]
print(output_list)

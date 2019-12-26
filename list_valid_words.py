def prepare_word_list(input_list):

    def open_list_path(file_path):
        with open(file_path, 'r') as raw:
            results = raw.readlines()
        return results

    def remove_newlines(input_list):
        stripped_data = map(
                lambda x: x.strip(),
                input_list)
        return stripped_data

    results = remove_newlines(open_list_path(input_list))
    return results


# now, take the last two letters of each word

# compare those to the list of accepted 2 letter words
# if the last two letters are a valid word, return the WHOLE word
def compare_word_endings(word, ending_distance, list_path):
    letter_list = prepare_word_list(list_path)

    def bite_word(word, distance_from_end):
        return word[distance_from_end:]

    def match_word_closure(word_1):
        def f(word_2):
            if word_1 == word_2:
                return True
            else:
                return False
        return f

    def find_two_letter_ending_matches(word, ending_distance, word_list):
        results = filter(
                match_word_closure(bite_word(word, ending_distance)),
                word_list)
        if list(results):
            return True
        else:
            return False

    return find_two_letter_ending_matches(word, ending_distance, letter_list)


def main(english_list_path):
    valid_list = prepare_word_list(english_list_path)
    return valid_list


word_data_path = "./word_source/example.txt"
# if the last 2 letters of the word are ALSO on the list of words,
# then save that word in another data set

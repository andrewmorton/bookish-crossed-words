from functools import partial


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

    return remove_newlines(open_list_path(input_list))


def compare_word_endings(ending_distance, list_path, word):
    letter_list = prepare_word_list(list_path)

    def bite_word(word, distance_from_end):
        return word[
                distance_from_end[0]:
                distance_from_end[1]:
                distance_from_end[2]]

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


def write_list_to_file(filename, item_list):
    with open(filename, 'w') as filehandle:
        filehandle.writelines("%s\n" % item for item in item_list)


def main():
    words_data_path = "./word_source/words.txt"
    two_letter_word_path = "./word_source/2_letter_words.txt"
    valid_2_letter_file = "./valid_2_letter_endings.txt"

    english_list = prepare_word_list(words_data_path)

    filter_function = partial(
            compare_word_endings,
            [-2, None, None],
            two_letter_word_path)

    results = filter(filter_function, english_list)
    write_list_to_file(valid_2_letter_file, results)
    print(f"Wrote items to {valid_2_letter_file}")

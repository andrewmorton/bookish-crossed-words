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


def write_list_to_file(filename, item_list):
    with open(filename, 'w') as filehandle:
        filehandle.writelines("%s\n" % item for item in item_list)


def compare_words(ending_distance, letter_list, word):

    if list(filter(lambda x: True if "\n" in x else False, letter_list)):
        raise SyntaxError("Letter list cannot contain newline characters")

    def bite_word(distance_from_end, word):
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

    def find_letter_matches(ending_distance, word_list, word):
        results = filter(
                match_word_closure(bite_word(ending_distance, word)),
                word_list)
        if list(results):
            return True
        else:
            return False

    return find_letter_matches(
            ending_distance,
            letter_list,
            word)


def main(input_word_list, compare_to_list, word_chunk, output_file):

    if not list(input_word_list) or not list(compare_to_list):
        raise SyntaxError("""Find word matches main requires
                lists for input and compare""")
    else:
        word_list = prepare_word_list(input_word_list)
        comparison_list = prepare_word_list(compare_to_list)

        filter_function = partial(
                compare_words,
                ending_distance=word_chunk,
                letter_list=comparison_list)

        results = filter(filter_function, word_list)
        write_list_to_file(output_file, results)
        print(f"Wrote items to {output_file}")


# Calling main function to search for words that end in a valid 2 letter word
# main(
#         "./word_source/words.txt",
#         "./word_source/2_letter_words.txt",
#         [-2, None, None],
#         "./valid_2_letter_words.txt")

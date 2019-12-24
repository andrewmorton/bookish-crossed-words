word_data_path = "./word_source/example.txt"


def prepare_word_list(input_list):

    def create_word_list(file_path):
        with open(file_path, 'r') as raw:
            results = raw.readlines()
        return results

    def remove_newlines(input_list):
        stripped_data = map(
                lambda x: x.strip(),
                input_list)
        return stripped_data

  results = remove_newlines(create_word_list(input_list))
  return results


    # now, take the last two letters of each word
  
    # compare those to the list of accepted 2 letter words
    # if the last two letters are a valid word, return the WHOLE word
def last_two_letters(word):
    return word[-2:]



def main(dataset):
    valid_list = prepare_word_list(dataset)
    return valid_list


# if the last 2 letters of the word are ALSO on the list of words,
    # then save that word in another data set

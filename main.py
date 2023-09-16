import string
book_location = "books/Frankenstein.txt"
with open(book_location) as f:
    file_contents = f.read()
    # capture the number of indivdual words in the text
    words = file_contents.split()
    letter_count = {}
    lower_words = []
    # Convert the text to lower case for comparison
    for word in words:
        lower_words.append(word.lower())
    
    # join character list to a lower case string
    new_words = ''.join(lower_words)

    # create a dictionary of the alphabet for comparison to count
    # the appearances in the text

    letters = dict.fromkeys(string.ascii_lowercase, 0)
    for letter in new_words:
        if letter in letters :
            letters[letter] += 1
    # sort the letters
    sorted_list = sorted(letters.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_list)



    # Create the output from the report
    print(f"--- Begin report of {book_location} ---")
    print(f"{len(words)} words found in the document")
    print()
    for result in converted_dict:
        print(f"The '{result}' character was found {converted_dict[result]} times")
    
    print('--- End report ---')



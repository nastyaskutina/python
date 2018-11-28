
def clear_text(text, trash_items):
    text = text.strip(trash_items)
    return text
    #while len(text) > 0 and text[0] in trash_items: #очистка левой части
        #text = text[:1]

def get_words(text):
    trash_items = '.,?!-_/@#$%^&*()[]{}+\'";:»«<>\\—'
    tokens = text.split()
    good_tokens = []
    for token in tokens:
        clean_token = clear_text(token, trash_items)
        if clean_token != '':
            clean_token = clean_token.lower()
            good_tokens.append(clean_token)
    return good_tokens
    #print(tokens)
def find_quotes(input_word, all_quotes, all_quotes_words):

    result = []
    for i, quote in enumerate(all_words)

def main():

    filename = 'C:\\Users\\student\\Desktop\\quotes.txt'

    all_quotes = []
    all_quotes_words = []

    DASH = '—'

    with open(filename, encoding='utf-8') as fid:
        for line in fid:
            parts = line.split(DASH)
            quote = parts[0].strip()
            quote_words = get_words(quote)

            all_quotes.append(quote)
            all_quotes_words.append(quote_words)

    while True:
        input_word = input('введите слово: ')
        if input_word == '':
            break
        input_word = input_word.strip().lower()
        found = find_quotes(input_word, all_quotes, all_quotes_words)
        if
    
                
    '''print('слово "разум" содержится в ', len(list_of_authors), ' цитате(-ах)')
    print(', '.join(list_of_authors))'''
            
if __name__ == '__main__':
    main()

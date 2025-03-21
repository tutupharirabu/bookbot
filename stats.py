def count_words(text):
  counting = len(text.split())
  return counting

def count_character(text):
  character_dict = {}
  
  for character in text:
    character = character.lower()
    if character in character_dict:
      character_dict[character] += 1
    else:
      character_dict[character] = 1
  
  return character_dict

def print_report(path, book_name):
  word_count = count_words(book_name)
  character_count = count_character(book_name)

  print('============ BOOKBOT ============')
  print(f'Analyzing book found at {path}...')
  print('----------- Word Count ----------')
  print(f'Found {word_count} total words')
  print('--------- Character Count -------')
  sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
  for character, count in sorted_characters:
    if character.isalpha():
      print(f'{character}: {count}')
  print('============= END ===============')
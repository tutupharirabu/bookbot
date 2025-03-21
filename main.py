import sys
from stats import count_words, count_character, print_report

def get_book_text(path):
  with open(path) as file:
    return file.read()
  
def main():
  if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    return sys.exit(1)
  
  text= get_book_text(sys.argv[1])
  print_report(sys.argv[1], text)

main()
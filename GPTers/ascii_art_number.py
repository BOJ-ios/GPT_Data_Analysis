import time
import os

# ASCII Art for numbers 0-9
numbers = {
    '0': '''
    000
   0   0
  0     0
  0     0
  0     0
  0     0
   0   0
    000
''',
    '1': '''
     1
    11
   111
     1
     1
     1
   1111
''',
    '2': '''
    222
   2   2
      2
     2
   2
   2
   2
   22222
''',
    '3': '''
    3333
       3
       3
    3333
       3
       3
       3
    3333
''',
    '4': '''
      44
     4 4
    4  4
   4444444
       4
       4
       4
       4
''',
    '5': '''
    5555
    5
    5
    555
       5
       5
       5
    555
''',
    '6': '''
    6666
   6
   6
    6666
   6   6
   6   6
   6   6
    666
''',
    '7': '''
   777777
        7
       7
      7
     7
    7
''',
    '8': '''
    888
   8   8
   8   8
    888
   8   8
   8   8
   8   8
    888
''',
    '9': '''
    9999
    9  9
    9  9
    9999
       9
       9
       9
'''
}


def display_number(number_str):
    """Display ASCII art for a given number."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(numbers[number_str])


# Main function to display numbers 0 to 9 in sequence
if __name__ == "__main__":
    for i in range(10):
        display_number(str(i))
        time.sleep(1)

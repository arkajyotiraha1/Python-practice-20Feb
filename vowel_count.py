
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def count_vowels(s:str):
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
    return count
s = input("Enter a string:")
vowel_count = count_vowels(s)
logging.info(f"Number of vowels in string '{s}': {vowel_count}")

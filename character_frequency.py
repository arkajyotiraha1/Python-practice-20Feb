import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def count_characters(s:str) -> dict:
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
s = input("Enter a string:")
character_frequency = count_characters(s)
logging.info(f"Character frequency for string '{s}': {character_frequency}")

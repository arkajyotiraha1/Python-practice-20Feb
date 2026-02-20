import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def reverse_string(s:str) -> str:
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
s = input("Enter a string:")
reversed_s = reverse_string(s)
logging.info(f"Reversed string for input '{s}': {reversed_s}")



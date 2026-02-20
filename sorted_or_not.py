
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_sorted(l:list) -> bool:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            logging.info(f"List is not sorted: {l[i]} > {l[i + 1]} at index {i}")
            return False
    logging.info(f"List is sorted: {l}")
    return True
l = eval(input("Enter a list of numbers:"))
is_sorted(l)

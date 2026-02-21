import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def find_missing_number(lst:list, n:int) -> int:
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    missing_number = expected_sum - actual_sum
    return missing_number
n = int(input("Enter the value of n:")) 
lst = eval(input("Enter a list of numbers from 1 to n:"))
missing_number = find_missing_number(lst, n)
logging.info(f"Missing number in list {lst} with n={n}: {missing_number}")


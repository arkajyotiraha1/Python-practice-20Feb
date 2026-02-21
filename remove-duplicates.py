mport logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def remove_duplicates(lst:list) -> list:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
lst = eval(input("Enter a list:"))
unique_lst = remove_duplicates(lst)
logging.info(f"Original list: {lst}")

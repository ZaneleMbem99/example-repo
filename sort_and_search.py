def sequencial_search(target, items):
    for i in range(len(items)):
        if items[i] == target:
            return i

    return None


items_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_item = 9
results = sequencial_search(target_item, items_list)


if results is not None:
    print(f"Item {target_item} found at index {results}.")
else:
    print(f"Item {target_item} not found in the list.")

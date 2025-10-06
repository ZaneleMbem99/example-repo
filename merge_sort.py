def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left_half = arr[:len(arr)//2]
    right_half = arr[len(arr)//2:]
    # Recursion
    merge_sort(left_half)
    merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0  # left array idx
    right_index = 0  # right array idx

    while left_index < len(left) and right_index < len(right):
        if len(left[left_index]) > len(right[right_index]):
            merged.append(left[left_index])
            left_index += 1

        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


list1 = ["sisi",
         "boy",
         "Nicky",
         "aseza",
         "masiye",
         "mother",
         "brother",
         "cousins",
         "father",
         "grandfather"
         ]
list2 = ["potatoes",
         "brocolli",
         "bread",
         "lettuce",
         "pizza",
         "KFC",
         "apple",
         "yoghurt",
         "mince",
         "beef"
         ]
list3 = ["face",
         "hands",
         "toes",
         "head",
         "stomach",
         "eyes",
         "glutes",
         "legs",
         "ears",
         "heart"
         ]

merged_list = list1 + list2 + list3
print(merge_sort(merged_list))

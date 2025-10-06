
family = ["sisi",
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
food = ["potatoes",
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
body = ["face",
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

merged_list = family + food + body

sorted_list = sorted(merged_list, key=len, reverse=True)
print(sorted_list)

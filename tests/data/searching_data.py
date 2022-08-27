SORTED_COLLECTION = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NONEXIST_RETURN_VALUE = -1

searching_data = {
    "exist_value": [wanted_value := 4, SORTED_COLLECTION.index(wanted_value)],
    "nonexist_value": [wanted_value := 15, NONEXIST_RETURN_VALUE],
    "first_element": [wanted_value := 1, SORTED_COLLECTION.index(wanted_value)],
    "last_element": [wanted_value := 10, SORTED_COLLECTION.index(wanted_value)],
}

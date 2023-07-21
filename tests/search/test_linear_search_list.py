import src.search.linear_search_list as linear_search_list


def test_linear_search():
    myList = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]

    assert linear_search_list.linear_search(myList, 69)
    assert linear_search_list.linear_search(myList, 1337)
    assert linear_search_list.linear_search(myList, 69420)
    assert linear_search_list.linear_search(myList, 69421) is False
    assert linear_search_list.linear_search(myList, 1)
    assert linear_search_list.linear_search(myList, 0) is False

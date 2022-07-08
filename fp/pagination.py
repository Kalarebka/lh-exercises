# Write function that paginates given input and prints out given page, sample input has to have at least 100 elements
# Function takes as parameters: input, max elements on page, page_number

result = list(range(100))

# Page numbers start at 1?
# Only list input or any container?


def paginate(data: list, max_elements_on_page: int, page_number: int):
    page_start = (page_number - 1) * max_elements_on_page
    page_end = page_start + max_elements_on_page
    page = data[page_start:page_end]
    return page

print(paginate(result, 8, 1))
print(paginate(result, 8, 11))
print(paginate(result, 8, 12))
print(paginate(result, 8, 13))
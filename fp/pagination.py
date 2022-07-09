# Write function that paginates given input and prints out given page, sample input has to have at least 100 elements
# Function takes as parameters: input, max elements on page, page_number

# Assumptions:
# Page numbers start at 1?
# Only list input?


def paginate(data: list, max_elements_on_page: int, page_number: int) -> list:
    page_start = (page_number - 1) * max_elements_on_page
    page_end = page_start + max_elements_on_page
    page = data[page_start:page_end]
    return page

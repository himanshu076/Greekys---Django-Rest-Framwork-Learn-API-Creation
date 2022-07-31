from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = 'p'     # Change the vapue of "Page" to "p"
    page_size_query_param = 'records'    # client can change the per oage records
    max_page_size = 10
    last_page_strings = 'end'    # 'override the "last" to "end"
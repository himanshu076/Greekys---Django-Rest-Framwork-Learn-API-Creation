from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'name'
    cursor_query_param = 'cu'    # Override the 'curser' to 'cu'
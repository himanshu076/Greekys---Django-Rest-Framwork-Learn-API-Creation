from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'    # Override the 'limit' to 'mylimit'
    offset_query_param = 'myoffser'    # Override the 'offset' to 'myoffset'
    max_limit = 6
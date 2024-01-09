from django.shortcuts import render
from rest_framework import filters, viewsets


from .models import Blog
from .seriaizers import BlogSerializer


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    http_method_names = ["get", "post", "delete", "patch", "put"]
    serializer_class = BlogSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ["published"]
    search_fields = ["title", "body"]
    ordering_fields = [
        "created_at",
    ]

    def get_queryset(self):
        return set.queryset.filter(name="sam")
    
    '''
    The error in the code was intentional, as we have filtered the queryset 
    using a field (name) that is not defined in the Blog model, which will 
    result in a FieldError exception being raised.
    '''
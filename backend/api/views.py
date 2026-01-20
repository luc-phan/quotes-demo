from rest_framework import permissions, viewsets

from .models import Quote
from .serializers import QuoteSerializer

# Create your views here.


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all().order_by('-created_at')
    serializer_class = QuoteSerializer
    # Only authenticated users can post/edit, others can just read
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

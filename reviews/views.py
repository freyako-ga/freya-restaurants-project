from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers.common import ReviewSerializer
from utils.decorators import handle_exceptions
from utils.permissions import IsOwnerOrReadOnly
from .serializers.populated import PopulatedReviewSerializer

class ReviewCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        
        review_to_create = ReviewSerializer(data=request.data)
        if review_to_create.is_valid():
            review_to_create.save()
            populated_review = PopulatedReviewSerializer(review_to_create.validated_data)

            return Response(populated_review.data, status=201)
        return Response(review_to_create.errors, status=400)

class ReviewDestroyView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    @handle_exceptions
    def delete(self, request, pk):
        try:
            review_to_delete = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'Review not found'}, status=404)
        
        self.check_object_permissions(request, review_to_delete)
        review_to_delete.delete()
        return Response(status=204)
    

    # class ReviewUpdateView(APIView):
    # permission_classes = [IsAuthenticated]

    # @handle_exceptions
    # def put(self, request, pk):
    #     try:
    #         review = Review.objects.get(pk=pk)
    #     except Review.DoesNotExist:
    #         raise NotFound("Review not found")
    #     if review.owner != request.user:
    #         return Response({'detail': 'Permission denied'}, status=403)
    #     review_to_update = ReviewSerializer(review, data=request.data, partial=True)
    #     if review_to_update.is_valid():
    #         review_to_update.save()
    #         populated_review = PopulatedReviewSerializer(review_to_update.validated_data)
    #         return Response(populated_review.data, status=200)
    #     return Response(review_to_update.errors, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurant
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


from .serializers.common import RestaurantSerializer
from .serializers.populated import PopulatedRestaurantSerializer
from utils.decorators import handle_exceptions
from utils.permissions import IsOwnerOrReadOnly





# Create your views here.

# Path for this view: /books
class RestaurantListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # Index Route
    @handle_exceptions
    def get(self, request):
        restaurants = Restaurant.objects.all() # Model.find() equivalent
        serialized_restaurants = PopulatedRestaurantSerializer(restaurants, many=True) 
        return Response(serialized_restaurants.data)

    # Create Route
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        restaurant_to_create = RestaurantSerializer(data=request.data)

        if restaurant_to_create.is_valid():
            restaurant_to_create.save()
            return Response(restaurant_to_create.data, 201)
        
        print('Validation error:', restaurant_to_create.errors)
        return Response(restaurant_to_create.errors, 400)
        
        
        # Path for this view: /restaurants/<int:id>/
class RestaurantRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    # Retrieve
    # Method: GET
    @handle_exceptions
    def get(self, request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        serialized_restaurant = PopulatedRestaurantSerializer(restaurant)
        return Response(serialized_restaurant.data)

    # Update
    # Method: PUT
    @handle_exceptions
    def put(self, request, pk):
        restaurant_to_update = Restaurant.objects.get(pk=pk)
        self.check_object_permissions(request, restaurant_to_update)

        serialized_restaurant = RestaurantSerializer(restaurant_to_update, data=request.data, partial=True)
        if serialized_restaurant.is_valid():
            serialized_restaurant.save()
            return Response(serialized_restaurant.data)
        return Response(serialized_restaurant.errors, 400)

    # Destroy
    # Method: DELETE
    @handle_exceptions
    def delete(self, request, pk):
        restaurant_to_delete = Restaurant.objects.get(pk=pk)
        self.check_object_permissions(request, restaurant_to_delete)
            
        restaurant_to_delete.delete()
        return Response(status=204)
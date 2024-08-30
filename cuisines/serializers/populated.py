from .common import CuisineSerializer
from restaurants.serializers.common import RestaurantSerializer

class PopulatedCuisineSerializer(CuisineSerializer):
    restaurants = RestaurantSerializer(many=True)
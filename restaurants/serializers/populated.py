from .common import RestaurantSerializer
from cuisines.serializers.common import CuisineSerializer
from jwt_auth.serializers.common import UserSerializer
from reviews.serializers.populated import PopulatedReviewSerializer

class PopulatedRestaurantSerializer(RestaurantSerializer):
    reviews = PopulatedReviewSerializer(many=True)
    cuisines = CuisineSerializer(many=True)
    owner = UserSerializer()
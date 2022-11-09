from rest_framework.serializers import ModelSerializer

from booker.models import TypeCoworking, Place, Reservation


class TypeSerializer(ModelSerializer):
    class Meta:
        model = TypeCoworking
        fields = ('name', 'price',)


class DetailSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = ('place_no', 'type_place', 'is_prepared',)


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'comment', 'place', 'checkin_date',)

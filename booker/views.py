from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from booker.models import TypeCoworking, Place, Reservation
from booker.serializers import TypeSerializer, DetailSerializer, \
    ReservationSerializer


def is_available_place(self, categorize):
    type_place = TypeCoworking.objects.filter(name=categorize)
    queryset = Place.objects.filter(
        type_place=type_place.first().id,
        is_prepared=True
    )
    return queryset


class CreateCategories(APIView):
    serializer_class = TypeSerializer
    queryset = TypeCoworking.objects.all()

    def post(self, request):
        # необходимо добавить проверку на name
        data = {
            "name": request.data.get('name'),
            "price": request.data.get('price'),
        }

        serializer = TypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatePlace(APIView):
    serializer_class = TypeSerializer
    queryset = Place.objects.all()

    def post(self, request):
        # необходимо добавить проверку на type_place
        data = {
            "place_no": request.data.get('place_no'),
            "type_place": request.data.get('type_place'),
        }

        serializer = DetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCategories(APIView):
    serializer_class = TypeSerializer
    queryset = TypeCoworking.objects.all()

    def post(self, request):
        data = {
            "name": request.data.get('name'),
            "price": request.data.get('price'),
        }

        serializer = TypeSerializer(data=data)
        if serializer.is_valid():
            TypeCoworking.objects.filter(
                name=request.data.get('name')
            ).update(price=request.data.get('price'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Categories(APIView):
    serializer_class = TypeSerializer
    queryset = TypeCoworking.objects.all()

    def get(self, request):
        types_coworking = TypeCoworking.objects.all()
        serializer = TypeSerializer(types_coworking, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Detail(APIView):
    serializer_class = DetailSerializer
    queryset = Place.objects.all()

    def get(self, request):
        detail_coworking = is_available_place(
            self,
            request.query_params.get("type", None)
        )
        serializer = DetailSerializer(detail_coworking, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AvailablePlace(APIView):
    serializer_class = DetailSerializer
    queryset = Place.objects.all()

    def get(self, request):
        places_by_type = is_available_place(
            self,
            request.query_params.get("type", None)
        )
        date = request.query_params.get("date", None)
        copy_places_by_type = places_by_type
        for place in places_by_type:
            is_booked = Reservation.objects.filter(
                place=place.id,
                checkin_date=date
            )
            if len(is_booked) != 0:
                copy_places_by_type = copy_places_by_type.exclude(
                    place_no=place
                )

        serializer = DetailSerializer(copy_places_by_type, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationRoom(APIView):

    def post(self, request):
        place_name = request.data.get('place')
        if len(Place.objects.filter(place_no=place_name)) != 0:
            place_number = (Place.objects.filter(
                place_no=place_name
            )).first().id
            if len(Reservation.objects.filter(
                    place=place_number,
                    checkin_date=request.data.get('checkin_date')
            )) == 0:
                data = {
                    "name": request.data.get('name'),
                    "email": request.data.get('email'),
                    "phone": request.data.get('phone'),
                    "comment": request.data.get('comment'),
                    "place": place_number,
                    "checkin_date": request.data.get('checkin_date'),
                }

                serializer = ReservationSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        serializer.data, status=status.HTTP_201_CREATED
                    )

        return Response(status=status.HTTP_400_BAD_REQUEST)



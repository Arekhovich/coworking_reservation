from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from booker.models import TypeCoworking, Place, Reservation


class RestTest(APITestCase):
    def setUp(self):
        self.name_type1 = "free"
        self.price1 = "100"
        self.price1_new = "123"

    def create_categories(self):
        data = {
            "name": self.name_type1,
            "price": self.price1,
        }
        url = reverse('add-categories')
        new_type = self.client.post(url, data=data)
        self.assertEqual(new_type.status_code, status.HTTP_201_CREATED)

    def create_place(self):
        data_place = {
            "place_no": "A101",
            "type_place": 1
        }
        new_place = self.client.post(reverse('add-place'), data=data_place)
        self.assertEqual(new_place.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(list(Place.objects.values())), 1)


    def test_add_and_get_categories(self):
        self.create_categories()
        all_types = self.client.get(reverse('categories'))
        self.assertEqual(all_types.status_code, status.HTTP_200_OK)
        self.assertEqual(len(all_types.json()), len(list(TypeCoworking.objects.values())))

    def test_update_price(self):
        self.create_categories()
        new_data = {
            "name": self.name_type1,
            "price": self.price1_new,
        }
        new_price = self.client.post(reverse('update-price'), data=new_data)
        self.assertEqual(new_price.status_code, status.HTTP_201_CREATED)
        self.assertEqual(float(self.price1_new), list(TypeCoworking.objects.values())[0]["price"])

    def test_bookroom(self):
        self.create_categories()
        self.create_place()
        data_reservation = {
            "name": "Test",
            "email": "test@test.com",
            "phone": "+45454545",
            "comment": "test",
            "place": "A101",
            "checkin_date": "2022-11-15"
        }
        new_reservation = self.client.post(reverse('book-room'), data=data_reservation)
        self.assertEqual(new_reservation.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(list(Reservation.objects.values())), 1)

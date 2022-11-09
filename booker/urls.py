from django.urls import path
from booker.views import Categories, Detail, ReservationRoom, \
    AvailablePlace, UpdateCategories, CreateCategories, CreatePlace


urlpatterns = [
    path("addcategories", CreateCategories.as_view(), name="add-categories"),
    path("categories", Categories.as_view(), name="categories"),
    path("updateprice", UpdateCategories.as_view(), name="update-price"),
    path("addplace", CreatePlace.as_view(), name="add-place"),
    path("typedetails", Detail.as_view(), name="room-of-type"),
    path("availableplace", AvailablePlace.as_view(), name="available-place"),
    path("bookroom", ReservationRoom.as_view(), name="book-room"),
]
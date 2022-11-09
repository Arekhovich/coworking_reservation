## Coworking Reservation

An example Django REST framework project for managing the reservation of workplaces in a coworking

### Features and API Endpoints
* Create types of workplaces (fix, free, room) with price.

**/addcategories**

* Create places for every type with own number.

**/addplace**

* Update price for the type.

**/updateprice**

* Get all available places by the type.

**/availableplace** with query param "type"

* Get all available places by the type and date.

**/availableplace** with query param "type" and "date"

* Book place.

**/bookroom**

### Install 

    pip install -r requirements.txt

### Usage

    python manage.py runserver

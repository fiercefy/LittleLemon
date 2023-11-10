from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
from datetime import datetime


class MenuTest(TestCase):

    def test_create_item(self):
        item = Menu.objects.create(title="Fried Chicken", price=Decimal('80'), inventory=100)
        self.assertEqual(str(item), "Fried Chicken : 10")

    def test_default_inventory(self):
        item = Menu.objects.create(title="Steak", price=Decimal('100'))
        self.assertEqual(item.inventory, 5)

class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="John Wick",
            number_of_guests=4,
            booking_date=datetime(2023, 10, 24, 19, 0)
        )
        expected_str = "John Wick for 4 guests on 2023-10-24 19:00:00"
        self.assertEqual(str(booking), expected_str)

    def test_default_number_of_guests(self):
        booking = Booking.objects.create(
            name="James Ford",
            number_of_guests = 5,
            booking_date=datetime(2023, 6, 24, 19, 0)
        )
        self.assertEqual(booking.number_of_guests, 5)

        
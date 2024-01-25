from django.test import TestCase
from ticket.models import Ticket


# Create your tests here.
class TicketTestCase(TestCase):
    def setUp(self):
        Ticket.objects.create(
            url="https://auto.ria.com/auto_honda_civic_35220475.html",
            title="Honda Civic 2017",
            price_usd=15000,
            odometer=100000,
            username="John Doe",
            phone_number="+380123456789",
            image_url="https://auto.ria.com/demo/img/preview.svg",
            images_count=10,
            car_number="AA1234AA",
            car_vin="12345678912345678"
        )

    def test_ticket_exists(self):
        ticket = Ticket.objects.get(url="https://auto.ria.com/auto_honda_civic_35220475.html")
        self.assertEqual(ticket.title, "Honda Civic 2017")
        self.assertEqual(ticket.price_usd, 15000)
        self.assertEqual(ticket.odometer, 100000)
        self.assertEqual(ticket.username, "John Doe")
        self.assertEqual(ticket.phone_number, "+380123456789")
        self.assertEqual(ticket.image_url, "https://auto.ria.com/demo/img/preview.svg")
        self.assertEqual(ticket.images_count, 10)
        self.assertEqual(ticket.car_number, "AA1234AA")
        self.assertEqual(ticket.car_vin, "12345678912345678")

    def test_ticket_not_exists(self):
        self.assertFalse(Ticket.objects.filter(url="https://auto.ria.com/auto_honda_civic_35220476.html").exists())

    def test_ticket_create(self):
        Ticket.objects.create(
            url="https://auto.ria.com/auto_honda_civic_35220476.html",
            title="Honda Civic 2017",
            price_usd=15000,
            odometer=100000,
            username="John Doe",
            phone_number="+380123456789",
            image_url="https://auto.ria.com/demo/img/preview.svg",
            images_count=10,
            car_number="AA1234AA",
            car_vin="12345678912345678"
        )
        self.assertTrue(Ticket.objects.filter(url="https://auto.ria.com/auto_honda_civic_35220476.html").exists())

"""This file should have our order classes in it."""
from random import randint
from datetime import datetime, day


class AbstractMelonOrder(object):
    """Parent class for melon orders."""

    shipped = False


    def __init__(self, species, qty):
        self.species = species
        self.qty = qty


    def get_base_price(self):

        splurge_base_price = randint(5,9)
        
        total_prices = splurge_base_price

        if datetime.hour >= 8 and datetime.hour <= 11 and 
        date.day >= 0 and date.day <= 4:
            total_prices += 4

        return total_prices


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        
        if self.species == "Christmas":
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    tax = 0.08
    order_type = "domestic"



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def __init__(self, country_code):
        self.country_code = country_code

    def get_total(self):
        get_total_international = super(InternationalMelonOrder,
            self).get_total()

        if self.qty < 10:
            get_total_international += 3

        return get_total_international

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True

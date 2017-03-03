"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Parent class for melon orders.
    """

    def __init__(self, species, qty, order_type, tax, country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code


    def get_total(self):
        """Calculate price."""

        base_price = 5

        if self.species == "Christmas":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, 
            qty, "domestic", 0.08)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, 
            qty, "international", 0.17, country_code)

    def get_total(self):
        get_total_international = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            get_total_international += 3

        return get_total_international

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

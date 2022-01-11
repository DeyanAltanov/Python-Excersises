class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f"{customer.id}: {customer.name} of age {customer.age} has {len(customer.rented_dvds)} rented DVD's ({', '.join(dvd.name for dvd in customer.rented_dvds)})\n"
        for dvd in self.dvds:
            if dvd.is_rented:
                rented = 'rented'
            else:
                rented = 'not rented'
            result += f"{dvd.id}: {dvd.name} ({dvd.creation_month} {dvd.creation_year}) has age restriction {dvd.age_restriction}. Status: {rented}\n"
        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if MovieWorld.customer_capacity() > len(self.customers) and customer not in self.customers:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if MovieWorld.dvd_capacity() > len(self.dvds) and dvd not in self.dvds:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                if dvd.is_rented:
                    for customer in self.customers:
                        if dvd not in customer.rented_dvds:
                            return "DVD is already rented"
                        elif dvd in customer.rented_dvds:
                            return f"{customer.name} has already rented {dvd.name}"
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.age_restriction > customer.age:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        else:
                            dvd.is_rented = True
                            customer.rented_dvds.append(dvd)
                            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"
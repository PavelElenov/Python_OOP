import calendar


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date = date.split('.')
        creation_year, creation_month = int(date[2]), calendar.month_name[int(date[1])]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        status = "rented" if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}." \
               f" Status: {status}"

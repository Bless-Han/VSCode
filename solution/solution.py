class Hat:

    houses = ["SY", "CC", "JL"]
    
    @classmethod
    def get_houses(cls):
        return cls.houses

print(Hat.get_houses())


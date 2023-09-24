class City:
    count = 0
    def __init__(self, name, region, country, population, index):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.index = index
        City.count += 1


    def __str__(self):
        return f"City{self.name, self.population, self.index}"

    def get_count_cities(self):
        return City.count



s1 = City("If", "West", "UA", 250, 76000)
s2 = City("Kyiv", "North", "UA", 3000, 10010)
s3 = City("Lviv", "Side", "UA", 800, 74000)

lst = [s1, s2, s3]
for s in lst:
    print(s)

print(f"{s1.get_count_cities()}")
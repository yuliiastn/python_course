class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other):
        return Country(
            f'{self.name} {other.name}',
            self.population + other.population
        )


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(
    f"Name: {bosnia_herzegovina.name}, "
    f"Population: {bosnia_herzegovina.population:_}"
    )

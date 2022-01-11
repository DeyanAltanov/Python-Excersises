countries = input().split(', ')
capitals = input().split(', ')

print(*[f"{country} -> {capital}" for country, capital in dict(zip(countries, capitals)).items()], sep='\n')
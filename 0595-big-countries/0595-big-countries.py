import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_country = world.loc[(world["area"] >= 3000000) | (world["population"] >= 25000000)]
    big_country = big_country[["name", "population", "area"]]
    return big_country
    
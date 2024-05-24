#Amra Ibrahim
#CSMC 254
#diagrams
# diagrams.py

def deck_area_calc(pool_width_param, pool_height, deck_width):
    # Calculate the area of the deck around the pool
    deck_area = 2 * (pool_width_param + pool_height) * deck_width
    return deck_area

# Example usage:
pool_width = 20  # feet
pool_height = 10  # feet
deck_width = 5  # feet
deck_area = deckCalc(pool_width, pool_height, deck_width)
print("Deck area:", deck_area, "square feet")

# diagrams.py
def tileCalc(tile_size, floor_width, floor_height):
    # Convert floor dimensions from feet to inches
    floor_width_inches = floor_width * 12
    floor_height_inches = floor_height * 12

    # Calculate the number of tiles needed to cover the entire area
    tiles_needed = (floor_width_inches // tile_size) * (floor_height_inches // tile_size)
    return tiles_needed

# Example usage:
tile_size = 12  # inches (1 square foot)
floor_width = 10  # feet
floor_height = 15  # feet
tiles_needed = tileCalc(tile_size, floor_width, floor_height)
print("Tiles needed:", tiles_needed)

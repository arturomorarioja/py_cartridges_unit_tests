# The minimum order quantity is 5. There is a 20% discount for orders of 100 or more printer cartridges.
def calculate_discount(cartridges):
    cartridges = int(cartridges)
    if cartridges < 5:
        raise ValueError('The minimum order quantity is 5.')
    if cartridges >= 100:
        return 0.20
    return 0.0
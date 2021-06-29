hex_values = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}

def to_hex(x):
    if x <= 0:
        return None
    remainder = x % 16
    return to_hex((x//16) + hex_values[remainder])


def hex_color(red,green,blue):
    red_hex = to_hex(red)
    green_hex = to_hex(green)
    blue_hex = to_hex(blue)

    result = '#'
    result.append(red_hex)
    result.append(green_hex)
    result.append(blue_hex)

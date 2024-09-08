roman_numerals = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

def to_roman(val: int) -> str:
    roman_string = ''
    for k in roman_numerals.keys():
        q, r = divmod(val, k)
        roman_string += roman_numerals[k] * q
        val = r
    return roman_string

print(to_roman(1940))
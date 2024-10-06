class RomanNumerals:
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

    @staticmethod
    def is_valid_range(val: int) -> bool:
        return 1 <= val < 4000

    @staticmethod
    def to_roman(val: int) -> str:
        if not RomanNumerals.is_valid_range(val):
            return f'{val} is not in the range from 1 to 4000'

        roman_string = ''
        for k in RomanNumerals.roman_numerals.keys():
            q, r = divmod(val, k)
            roman_string += RomanNumerals.roman_numerals[k] * q
            val = r
        return roman_string

    @staticmethod
    def from_roman(roman_num: str) -> int:
        dec_num = 0
        for k, v in roman_numerals.items():
            while roman_num.startswith(v):
                i = roman_num.find(v)
                dec_num += k
                roman_num = roman_num[i+len(v):]
        return dec_num

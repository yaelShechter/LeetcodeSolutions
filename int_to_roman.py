int_to_roman_dict = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

def int_to_roman(num: int) -> str:
    output = ""
    for int_key in int_to_roman_dict:
        while num >= int_key:
            output += int_to_roman_dict[int_key]
            print(int_key)
            num -= int_key
    return output

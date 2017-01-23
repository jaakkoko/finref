import math
from string import ascii_uppercase


def fi_validate(reference):
    """ Validate reference number and return a boolean.
    Keyword arguments:
        reference -- reference number as a string
    """
    # Make sure the reference is all digits.
    if not reference.isdigit():
        return False
    # Get checksum from the last number of the reference. 
    checksum  = int(reference[-1])
    # Remove checksum from the reference string.
    reference = reference[:-1]
    # Reverse the reference.
    reference = reference[::-1]
    # Multipliers for base value calculation.
    mod = [7,3,1]
    # Calculate base values by multiplying each digit.
    base_values = []
    mod_index = 0
    for number in reference:
        # Restart mod index
        if mod_index > 2:
            mod_index = 0
        # Multiply value and add to base values.
        base_values.append(int(number) * mod[mod_index])
        mod_index += 1
    # Calculate base value from the sum of base values. 
    base = int(sum(base_values))
    # Get next tenth number up from base.
    next = int(math.ceil(base / 10.0)) * 10
    # Substract next number up from the base number to get the result.
    result = next - base
    # Reference is valid if result matches checksum.
    return result == checksum

def rf_validate(s):
    print "rf_validate %s" % s

    return False

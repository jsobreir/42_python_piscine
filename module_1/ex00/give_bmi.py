import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate bmi values given by a list of heights and weights.

    Args:
        Height: list[int | float]: List of heights in meters.
        Weight. list[int | float]: List of weights in lbs.
    
    Return:
        list[int | float]: List of calculated BMI values.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists must be the same length.")
        return [w/(h**2) for w, h in zip(weight, height)]
    except Exception as e:
        print("An error occured", e)
        return []

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compares each BMI value in a list to a given limit.

    Args:
        bmi: list[int | float]: list of bmi values.
        limit (int): limit to compare each bmi value to.

    Returns:
        list[bool]: list of booleans. True if the value is higher than limit, else false.
    """
    try:
        ret =  []
        if not isinstance(limit, int):
            raise TypeError
        for x in bmi:
            if not isinstance(x, (int, float)):
                raise TypeError("BMI must be either an int or a float")
            if x > limit:
                ret.append(True)
            else:
                ret.append(False)
        return ret
    except Exception as e:
        print("An error occured", e)
        return[]
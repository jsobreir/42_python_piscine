def all_thing_is_obj(object: any) -> int:
    objt_type = type(object)
    match objt_type:
        case t if t is list:
            print("List:", objt_type)
        case t if t is tuple:
            print("Tuple:", objt_type)
        case t if t is set:
            print("Set:", objt_type)
        case t if t is dict:
            print("Dict:", objt_type)
        case t if t is str:
            if object == "Toto":
                print("Toto is in the kitchen:", objt_type)
            elif object == "Brian":
                print("Brian is in the kitchen:", objt_type)
            else:
                print("Type not found")
        case _:
            print("Type not found")
    return 42

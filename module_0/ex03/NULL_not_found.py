def NULL_not_found(object: any) -> int:
	objt_type = type(object)
	match object:
		case None:
			print("Nothing: None", objt_type)
		case float() as  f if f != f:
			print("Cheese: nan", objt_type)
		case False:
				print("Fake:", objt_type)
		case int():
			print("Zero: 0", objt_type)
		case str() as s if s == "":
			print("Empty:", objt_type)
		case _:
			print("Type not found")
			return 1
	return 0
def validate_pin(pin):
	### Determines if a pin is numbers only with a length of 4 or 6 only
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)
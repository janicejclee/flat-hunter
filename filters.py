def meets_requirements(flat, min_bedrooms):
    return flat["bedrooms"] >= min_bedrooms

def filter_flats(flats, min_bedrooms):
    return [flat for flat in flats if meets_requirements(flat, min_bedrooms)] 
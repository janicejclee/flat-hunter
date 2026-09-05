
def anchored_scoring(value, low_anchor, high_anchor):
    if value <= low_anchor:
        return 10
    else:
        slope = 5 / (high_anchor - low_anchor)
        return max(10 - slope * (value - low_anchor), 0)

def min_max_function(value, min_val, max_val):
    if max_val == min_val:
        return 5
    else:
        return 10 * (value - min_val) / (max_val - min_val)

def get_min_max(flats, key):
    return min(flat[key] for flat in flats), max(flat[key] for flat in flats)
        
def boolean_lookup(value, preferred_value):
    if value == preferred_value:
        return 10
    else:
        return 0

def normalise_weights(weights):
    total = sum(weights.values())
    return {key: value / total for key, value in weights.items()}
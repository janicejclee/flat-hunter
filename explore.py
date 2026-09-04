def main():
    flats = [
        {
            "name": "Flat A",
            "price": 400,
            "commute": 10,
            "size": 588,
            "bills_included": True,
            "furnished": True
        },
        {
            "name": "Flat B",
            "price": 280,
            "commute": 30,
            "size": 420,
            "bills_included": False,
            "furnished": False

        },
        {
            "name": "Flat C",
            "price": 420,
            "commute": 12,
            "size": 620,
            "bills_included": False,
            "furnished": True
        },
        {
            "name": "Flat D",
            "price": 350,
            "commute": 20,
            "size": 588,
            "bills_included": False,
            "furnished": True
        },
        {
            "name": "Flat E",
            "price": 320,
            "commute": 40,
            "size": 500,
            "bills_included": True,
            "furnished": True
        }
    ]
    budget_min = 300
    budget_max = 400
    commute_max = 30
    prefer_bills_included = False
    prefer_furnished = True
    weights = {"price": 4, "commute": 5, "size": 2, "bills_included": 1, "furnished": 4}

    min_val, max_val = get_min_max(flats, "size")
    normalised_weights = normalise_weights(weights)

    for flat in flats:
        scores = {
            "price": anchored_scoring(flat["price"], budget_min, budget_max),
            "commute": anchored_scoring(flat["commute"], 0, commute_max),
            "size": min_max_function(flat["size"], min_val, max_val),
            "bills_included": boolean_lookup(flat["bills_included"], prefer_bills_included),
            "furnished": boolean_lookup(flat["furnished"], prefer_furnished)
        }
        total_score = sum(normalised_weights[key] * scores[key] for key in scores)
     
        print(flat["name"])
        for key, value in scores.items():
            print(f"{key} score: {value}")
        print(f"total score: {total_score}")


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


main()


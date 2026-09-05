from normalise import anchored_scoring, min_max_function, boolean_lookup, get_min_max, normalise_weights

def score_flat(flat, budget_min, budget_max, commute_max, prefer_bills_included, prefer_furnished, min_val, max_val, normalised_weights):
    scores = {
        "price": anchored_scoring(flat["price"], budget_min, budget_max),
        "commute": anchored_scoring(flat["commute"], 0, commute_max),
        "size": min_max_function(flat["size"], min_val, max_val),
        "bills_included": boolean_lookup(flat["bills_included"], prefer_bills_included),
        "furnished": boolean_lookup(flat["furnished"], prefer_furnished)
    }
    total_score = sum(normalised_weights[key] * scores[key] for key in scores)

    return scores, total_score
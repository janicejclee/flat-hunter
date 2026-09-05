from data import flats, budget_min, budget_max, commute_max, prefer_bills_included, prefer_furnished, weights, min_bedrooms
from filters import filter_flats
from normalise import get_min_max, normalise_weights
from scoring import score_flat

def main():
    filtered_flats = filter_flats(flats, min_bedrooms)

    min_val, max_val = get_min_max(filtered_flats, "size")
    normalised_weights = normalise_weights(weights)

    for flat in filtered_flats:
        scores, total_score = score_flat(flat, budget_min, budget_max, commute_max, prefer_bills_included, prefer_furnished, min_val, max_val, normalised_weights)
        print(flat["name"])
        for key, value in scores.items():
            print(f"{key} score: {value}")
        print(f"total score: {total_score}")

main()
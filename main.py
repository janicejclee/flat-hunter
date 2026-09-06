from data import flats, budget_min, budget_max, commute_max, prefer_bills_included, prefer_furnished, weights, min_bedrooms
from filters import filter_flats
from normalise import get_min_max, normalise_weights
from scoring import score_flat

def main():
    filtered_flats = filter_flats(flats, min_bedrooms)

    min_val, max_val = get_min_max(filtered_flats, "size")
    normalised_weights = normalise_weights(weights)

    for flat in filtered_flats:
        breakdown, total_score = score_flat(flat, budget_min, budget_max, commute_max, prefer_bills_included, prefer_furnished, min_val, max_val, normalised_weights)
        print(flat["name"])
        for criteria, value in breakdown.items():
            print(f"{criteria}")
            print(f"score: {value["score"]}")
            print(f"weight: {value["weight"]}")
            print(f"contribution: {value["contribution"]}")
        print(f"total score: {total_score}")

main()
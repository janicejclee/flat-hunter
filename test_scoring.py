from scoring import score_flat

def test_score_flat():
    flat = {
        "name": "Flat A",
        "price": 350,
        "commute": 15,
        "size": 500,
        "bills_included": False,
        "furnished": True
    }
    budget_min = 300
    budget_max = 400
    commute_max = 30
    prefer_bills_included = False
    prefer_furnished = True
    min_val = 400
    max_val = 600
    normalised_weights = {"price": 0.2, "commute": 0.2, "size": 0.2, "bills_included": 0.2, "furnished": 0.2}

    expected_breakdown = {
        "price": {"score": 7.5, "weight": 0.2, "contribution": 1.5}, 
        "commute": {"score": 7.5, "weight": 0.2, "contribution": 1.5},
        "size": {"score": 5, "weight": 0.2, "contribution": 1},
        "bills_included": {"score": 10, "weight": 0.2, "contribution": 2},
        "furnished": {"score": 10, "weight": 0.2, "contribution": 2} 
        }
    expected_total_score = 8

    breakdown, total_score = score_flat(flat, budget_min, budget_max, commute_max, prefer_bills_included, prefer_furnished, min_val, max_val, normalised_weights)

    assert breakdown == expected_breakdown
    assert total_score == expected_total_score
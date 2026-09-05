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

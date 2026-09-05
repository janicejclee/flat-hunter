from filters import meets_requirements

def test_meets_requirements_exact():
    flat = {"name": "Flat A", "bedrooms": 2}
    min_bedrooms = 2
    expected_output = True
    output = meets_requirements(flat, min_bedrooms)
    assert output == expected_output

def test_meets_requirements_below():
    flat = {"name": "Flat B", "bedrooms": 1}
    min_bedrooms = 2
    expected_output = False
    output = meets_requirements(flat, min_bedrooms)
    assert output == expected_output

def test_meets_requirements_above():
    flat = {"name": "Flat C", "bedrooms": 3}
    min_bedrooms = 2
    expected_output = True
    output = meets_requirements(flat, min_bedrooms)
    assert output == expected_output
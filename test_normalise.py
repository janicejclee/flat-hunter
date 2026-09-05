from normalise import anchored_scoring, min_max_function, get_min_max, boolean_lookup, normalise_weights

def test_anchored_scoring_low_anchor():
    value = 300
    low_anchor = 300
    high_anchor = 400
    expected_score = 10 
    score = anchored_scoring(value, low_anchor, high_anchor)
    assert score == expected_score

def test_anchored_scoring_between_anchors():
    value = 350
    low_anchor = 300
    high_anchor = 400
    expected_score = 7.5
    score = anchored_scoring(value, low_anchor, high_anchor)
    assert score == expected_score

def test_anchored_scoring_high_anchor():
    value = 400
    low_anchor = 300
    high_anchor = 400
    expected_score = 5
    score = anchored_scoring(value, low_anchor, high_anchor)
    assert score == expected_score

def test_anchored_scoring_past_high_anchor():
    value = 420
    low_anchor = 300
    high_anchor = 400
    expected_score = 4
    score = anchored_scoring(value, low_anchor, high_anchor)
    assert score == expected_score

def test_anchored_scoring_far_past_high_anchor():
    value = 500
    low_anchor = 300
    high_anchor = 400
    expected_score = 0
    score = anchored_scoring(value, low_anchor, high_anchor)
    assert score == expected_score

def test_min_max_function_between():
    value = 480
    min_val = 400
    max_val = 600
    expected_score = 4
    score = min_max_function(value, min_val, max_val)
    assert score == expected_score

def test_min_max_function_min():
    value = 400
    min_val = 400
    max_val = 600
    expected_score = 0
    score = min_max_function(value, min_val, max_val)
    assert score == expected_score

def test_min_max_function_max():
    value = 600
    min_val = 400
    max_val = 600
    expected_score = 10
    score = min_max_function(value, min_val, max_val)
    assert score == expected_score

def test_min_max_function_equal():
    value = 500
    min_val = 500
    max_val = 500
    expected_score = 5
    score = min_max_function(value, min_val, max_val)
    assert score == expected_score

def test_get_min_max():
    sample = [
        {
            "name": "Flat A",
            "size": 588
        },
        {
            "name": "Flat B",
            "size": 400
        },
        {
            "name": "Flat C",
            "size": 600
        }
    ]
    expected_min, expected_max = 400, 600
    min_val, max_val = get_min_max(sample, "size")
    assert (min_val, max_val) == (expected_min, expected_max)

def test_boolean_lookup_match():
    value = True
    preferred_value = True
    expected_score = 10
    score = boolean_lookup(value, preferred_value)
    assert score == expected_score

def test_boolean_lookup_differ():
    value = False
    preferred_value = True
    expected_score = 0
    score = boolean_lookup(value, preferred_value)
    assert score == expected_score

def test_normalise_weights():
    sample = {"a": 2, "b": 2}
    expected_output = {"a": 0.5, "b": 0.5}
    output = normalise_weights(sample)
    assert output == expected_output

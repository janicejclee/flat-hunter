def result_table(result):

    # Print header row
    print(f"{'':<15}", end="")
    for flat in result:
        print(f"{flat["name"]:<15}", end="")
    print()

    # Print total score
    print(f"{'total score':<15}", end="")
    for flat in result:
        print(f"{flat["total_score"]:<15.2f}", end="")
    print()

    # Sort criterias by weight (highest first)
    sorted_criteria = sorted(result[0]["breakdown"], key = lambda criteria: result[0]["breakdown"][criteria]["weight"], reverse=True)

    for criteria in sorted_criteria:
        # 1. Print header line
        print()
        print(f"{criteria} (weight: {result[0]["breakdown"][criteria]["weight"]})")

        # 2. Score row
        print(f"{'score':<15}", end="")
        for flat in result:
            print(f"{flat["breakdown"][criteria]["score"]:<15.2f}", end="")
        print()

        # 3. Raw value row
        print(f"{criteria:<15}", end="")
        for flat in result:
            print(f"{flat["flat"][criteria]:<15}", end="")
        print()

        # 4. Contribution row
        print(f"{'contribution':<15}", end="")
        for flat in result:
            print(f"{flat["breakdown"][criteria]["contribution"]:<15.2f}", end="")
        print()


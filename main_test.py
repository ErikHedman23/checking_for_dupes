from main import *

run_cases = [
    (
        [
            "golden retriever",
            "bulldog",
            "golden retriever",
            "bulldog",
            "beagle",
            "bulldog",
            "beagle",
            "beagle",
            "golden retriever",
            "golden retriever",
            "poodle",
            "golden retriever",
            "golden retriever",
        ],
        ["beagle", "bulldog", "golden retriever", "poodle"],
    )
]

submit_cases = run_cases + [
    (["golden retriever", "golden retriever", "golden retriever"], ["golden retriever"]),
    (
        ["golden retriever", "bulldog", "beagle", "poodle"],
        ["beagle", "bulldog", "golden retriever", "poodle"],
    ),
    (["beagle", "beagle", "beagle"], ["beagle"]),
    (["poodle", "poodle", "poodle"], ["poodle"]),
    ([], []),
    (["bulldog", "bulldog", "bulldog"], ["bulldog"]),
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * dogs: {input}")
    print(f"Expecting: {expected_output}")
    result = remove_duplicates(input)
    if isinstance(result, list):
        result.sort()
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

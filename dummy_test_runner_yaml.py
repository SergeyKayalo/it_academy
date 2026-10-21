import datetime
import yaml
import sys
from pathlib import Path


def dummy_test(data):

    if data <= 5:
        return True
    else:
        return False

results = []
tests = [
(dummy_test(5), True),
(dummy_test(7), True),
(dummy_test(6), False),
(dummy_test(2), True),
(dummy_test(4), False),
(dummy_test(8), True),
(dummy_test(1), False),
]

passed = 0
errors = 0
count = 0
for result, expected in tests:
    count += 1
    try:
        assert result == expected
    except AssertionError as e:
        print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
              f"но фактический результат {result}")
        results.append({"test": count, "result": result, "expected": expected, "test_result": "error"})
        errors += 1
        continue
    print("Тест прошёл!")
    results.append({"test": count, "result": result, "expected": expected, "test_result": "passed"})
    passed += 1

results_total = {
    "total_passed": passed,
    "total_errors": errors,
    "total_count": count,
    "datetime" : datetime.datetime.now().isoformat(),
    "results" : results
}
#print(results_total)
BASE = Path(__file__).parent
TEST_RESULT = BASE / "dummy_test_results.yaml"
with TEST_RESULT.open("w", encoding="utf-8") as f:
    yaml.dump(results_total, f, indent=2, allow_unicode=True)



import datetime
from pathlib import Path
import xml.etree.ElementTree as ET


def dummy_test(data):

    if data <= 5:
        return True
    else:
        return False

tests = [
(dummy_test(5), True),
(dummy_test(7), True),
(dummy_test(6), False),
(dummy_test(2), True),
(dummy_test(4), False),
(dummy_test(8), True),
(dummy_test(1), False),
]

root = ET.Element("test_results")
results_el = ET.SubElement(root, "results")

passed = 0
errors = 0
count = 0

for result, expected in tests:
    count += 1

    test_el = ET.SubElement(results_el, "test")
    test_el.set("id", str(count))
    test_el.set("result", str(result))
    test_el.set("expected", str(expected))

    try:
        assert result == expected
    except AssertionError:
        print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
              f"но фактический результат {result}")
        test_el.set("test_result", "error")
        errors += 1
        continue

    print("Тест прошёл!")
    test_el.set("test_result", "passed")
    passed += 1

ET.SubElement(root, "total_passed").text = str(passed)
ET.SubElement(root, "total_errors").text = str(errors)
ET.SubElement(root, "total_count").text = str(count)
ET.SubElement(root, "datetime").text = datetime.datetime.now().isoformat()

BASE = Path(__file__).parent
TEST_RESULT = BASE / "dummy_test_results.xml"
with TEST_RESULT.open("wb") as f:
    f.write(ET.tostring(root, encoding="utf-8"))
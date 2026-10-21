from pathlib import Path
import yaml

BASE = Path(__file__).parent
TEST_RESULT = BASE / "test_results.yaml"
USERS = BASE / "users.yaml"

with TEST_RESULT.open("w") as file_test_result, USERS.open("w") as file_users:
    results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}
    results2 = [{"id": 1, "name": "Sasha", "role": "admin"}]
    file_test_result.write(yaml.safe_dump(results, indent=2))
    file_users.write(yaml.safe_dump(results2, indent=2))

with TEST_RESULT.open("r") as file_test_result:
    loaded_test_results = yaml.safe_load(file_test_result)
    print(f"Успешно пройдено: {loaded_test_results["passed"]/loaded_test_results["total"]*100:.0f}% тестов")


with USERS.open("r") as file_users:
    loaded_users = yaml.safe_load(file_users)
    loaded_users.append({"id": 2, "name": "Вася", "role": "poweruser"})
    print(loaded_users)
with USERS.open("w", encoding="utf-8") as file_users:
    yaml.safe_dump(loaded_users, file_users, indent=2, allow_unicode=True)

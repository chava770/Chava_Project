import requests
import json


def calculate_average_salary_and_export():

    url = "http://127.0.0.1:8000/api/api/"
    headers = {'Authorization': 'Basic Y2hhdmE6bG92ZXVyc2VsZjEyMw=='}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error: Could not retrieve worker data from API.")
        return

    workers = json.loads(response.text)
    total_salary = sum(int(round(float(worker['SALARY']))) for worker in workers)
    average_salary = total_salary / len(workers)

    with open("below_average_workers.txt", "w") as file:
        for worker in workers:
            if worker['HIRE_DATE'] < '2022-01-01' and float(worker['SALARY']) < average_salary:
                file.write(f"Employee: {worker['FIRST_NAME']} {worker['LAST_NAME']}, Possition: {worker['JOB_ID']}, Salary: {worker['SALARY']}\n")

    print("Export complete: below_average_workers.txt")

calculate_average_salary_and_export()


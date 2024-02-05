import os
import sys
import requests
import time
import logging
from datetime import datetime


import constants

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API endpoint
task_status_api_url = f'http://localhost:5637/tasks/'
parent_mid = "20ded03827c57dfdc41c57b57c51abaa210845ef62ae9627e2d59a89b8be67c2"
hive_read_key = "35173f24ee09301820ea75bbda6f208cba920b5482ab2a395b47b9c5985f2977"
token_hive_agent = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpKU3prOWZmM2EyYWJjbzRRMm1jNCJ9.eyJpc3MiOiJodHRwczovL2Rldi02dGUxbHAweS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjVhOTFlMTM5Y2U3YWFjZDFhYTcxMWMyIiwiYXVkIjoiaHR0cHM6Ly9wbGF0Zm9ybS5wcmVwcm9kLmhpdmVuZXQuY29tLyIsImlhdCI6MTcwNjUwNzQ5NCwiZXhwIjoxNzA2NTkzODk0LCJhenAiOiJzWENIaUk0b2ROMmt2OFA0NVNWY1Frc0tSc3liTEphUyIsInNjb3BlIjoib2ZmbGluZV9hY2Nlc3MiLCJwZXJtaXNzaW9ucyI6W119.hWFw9Jd4z0FbSjgq0WJ2Emc_kTWOPmiSrrs8bGC-f8qAVpgcYDExDG097pJ86QuYwBMI5FYlG9xg6DSlBLTXeCPYyIX0YpUj5M0qy8W2wtYMnkcelb_VWCtDyd6ol4cGsjUGTNqxBP0o2dk2HMcH3J3bZY73ZgKaEZiD5s1p1ZEdodr1c5rJBd-l_uTYA_sjY8TAiDIRD4dvLUDA0aK7nJNdumqdP2Vn4DP2Y6QT8kAgQhe47UyjHcA37fePeCYpcZjwrgnQvs4k7EfpfHKX6SddDkHXGeUBH_DjpWNUQks_ukGyA59KoH9tczyduD1_ql6g0uE5O7FINq-pWHpqQA"

headers = {
    'X-Trace-Id': 'Polling Script',
    'X-Hive-Read-Key': f'{constants.hive_read_key_dock}',
    'Accept': 'application/json',
    'Authorization': f'Bearer {constants.token_hive_agent_dock}',
}


def extract_data(response_json):
    """
            Scope: parsing json to extract metadata
            :return: extracted data from response json
    """
    try:
        print(response_json.get("id"))
        executions = response_json["timestamps"]["executions"]
        total_epoch = (executions[0].get("succeeded")) - (executions[0].get("started"))
        total_utc = datetime.utcfromtimestamp(total_epoch)
        total_time = total_utc.strftime("%H:%M:%S")
        logger.info(f"file upload time epoch: {total_utc}, time: {total_time}")
        
        return total_time
    except Exception as e:
        logger.exception("Error extracting data: %s", e)
        return None


def poll_api_and_extract_data(id_value, start_time):
    """
        Scope: to poll api to get data
        raise exceptions if there is an error in response, sleep for some time poll again in loop
        solution instead of sleep()
        extracted data from response json
    """

    while True:
        try:
            response = requests.get(constants.get_task_status_api_url_dock + id_value, headers=headers)
            response.raise_for_status()
            if response.status_code == 200 and response.json()['status'] == 'SUCCESSFUL':
                upload_API_end_epoch = extract_data(response.json())
                # upload_API_end_time = 
                print(f"API score, file upload time in sec:  {((upload_API_end_epoch))}s")
                overall_upload_end_time = int(time.time()*1000)
                overall_upload_time = overall_upload_end_time-start_time
                print(response.text)
                print(f"Overall upload of file:{id_value} took : {overall_upload_time:.2f}ms :{overall_upload_time/1000.0}sec")

                break
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            logger.error("Error making API request: %s", e)
        except Exception as e:
            logger.exception("Unhandled exception: %s", e)


def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        logger.error(f"Error: File not found at path '{file_path}'")
        return None
    except Exception as e:
        logger.exception("Unhandled exception: %s", e)
        return None

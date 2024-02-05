import requests
import json
import time
import helper
import constants
import os

import requests_toolbelt.multipart.encoder


def hive_upload_task():
    try: 
        url = constants.task_url
        # parent_mid = "20ded03827c57dfdc41c57b57c51abaa210845ef62ae9627e2d59a89b8be67c2"
        # hive_read_key = "35173f24ee09301820ea75bbda6f208cba920b5482ab2a395b47b9c5985f2977"
        file_path = 'data/swarm-agent-user-1/test_data/image_test.png'
        token_hive_agent = constants.token_hive_agent_dock
        form_data = {            
            "type": "FILE_UPLOAD",
            "jsonMetadata": json.dumps({
                "filename": os.path.basename(f'{file_path}'),
                "filesize": "4261722",
                "parentMid": constants.parent_mid_dock,
                "createdtime": "0",
                "filePath": f'/{file_path}'
            }),
            "metadataVersion": "1.0.0",
        }

        headers = {
            "X-Trace-Id": "File upload start Puja",
            "X-Hive-Read-Key": constants.hive_read_key_dock,
            "Accept": "application/json",
            "Authorization": f"Bearer {token_hive_agent}",
            # 'Content-Type': form_data.content_type

        }  
        files = {"thumbnail": open(file_path, "rb")}
        request_start_time = int(time.time() * 1000)
        response = requests.post(url, headers=headers, data=form_data, files=files)
        end_time = int(time.time() * 1000)
        response_data = response.json()
        id_value = str(response_data.get('id'))
        print(f"Task id is: {id_value}")
        result_mid = response_data.get('resultMid')
        req_submitted_ts = response_data.get('submitted')
        file_size = response_data.get('filesize')
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        upload_req_time = end_time - request_start_time
        print(f"Time taken for /tasks api to start the upload task request is: {upload_req_time:.2f}ms : { upload_req_time/1000.0}sec")
        helper.poll_api_and_extract_data(id_value,request_start_time )
    except requests.exceptions.RequestException as exc:
        print(f"Request Exception: {exc}")
    except Exception as e:
        print(f"Exception: {e}")

hive_upload_task()

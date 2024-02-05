import json
import time

base_url = "http://localhost:8080/"
task_url = "http://localhost:51486/tasks"
get_task_status_api_url = 'http://localhost:8080/tasks/'
get_task_status_api_url_dock = 'http://localhost:51486/tasks/'
# docker port: 51486 , default: 8080
# user: 2cFxjLEh6xx7b83hSTJvK7pxS9Bl3gyS@clients
workspace_mid = "4f94bc2d0b5db3c3585d765f41961dc61c99fb610700c12909ae8e56e2588b83"
parent_mid_dock = workspace_mid
# volumeMID = "7f77b78b33f02d6aac4d15a4babec2b2817f2fd93b1952daff4bfbab3b6bee29"
# workspace_mid = ""
hive_read_key_dock = "e815e52e12b7188bf8f981044bbb5e52453cf22ecab7b51d793319f73b9f96b8"
file_path_dock = "/Users/pbhattacharya/Downloads/image_test.png"
token_hive_agent_dock = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpKU3prOWZmM2EyYWJjbzRRMm1jNCJ9.eyJpc3MiOiJodHRwczovL2Rldi02dGUxbHAweS51cy5hdXRoMC5jb20vIiwic3ViIjoiMmNGeGpMRWg2eHg3YjgzaFNUSnZLN3B4UzlCbDNneVNAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vcGxhdGZvcm0ucHJlcHJvZC5oaXZlbmV0LmNvbS8iLCJpYXQiOjE3MDY3NjUzMzgsImV4cCI6MTcwNjg1MTczOCwiYXpwIjoiMmNGeGpMRWg2eHg3YjgzaFNUSnZLN3B4UzlCbDNneVMiLCJzY29wZSI6InVwZGF0ZTp1c2VycyByZWFkOnVzZXJzIHJlYWQ6dXNlcl9pZHBfdG9rZW5zIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsidXBkYXRlOnVzZXJzIiwicmVhZDp1c2VycyIsInJlYWQ6dXNlcl9pZHBfdG9rZW5zIl19.NoqF1ulJX4T_VZen7oUnm2iSDZOpT4R-Ol622aflRAdFPM4LzSQiHkQcAGYHlq5okN0uB1bWcW7piw_rM7f4hbPwu4k60ow1tLCto50soY8dJvN5BkLcSr0iSM-JymwNLK0C47InV-bACHjvcZHbLbsGDtItYvA8tnobIKTSb1ceVMOtQ7TWVh9jE_CbsIB2Nzv0HHVizMJ57P5uydyazK9Oohd3c-T4vHLrlRvP-kISefYmIcd1gGB2pCarN03Z1AebSa6Yyps0Qc73dMP-SGCOLM7E5pH3WeOL8AyDL0TVolhAp39IWbXKX-j3gsumPG7i5H4XURWs-gPBwt4CFA"
curr_time = int(time.time())

# hive test data variables
# original: user based local instance info


parent_mid = "20ded03827c57dfdc41c57b57c51abaa210845ef62ae9627e2d59a89b8be67c2"
hive_read_key = "35173f24ee09301820ea75bbda6f208cba920b5482ab2a395b47b9c5985f2977"
file_path = "/Users/pbhattacharya/Downloads/image_test.png"
token_hive_agent = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpKU3prOWZmM2EyYWJjbzRRMm1jNCJ9.eyJpc3MiOiJodHRwczovL2Rldi02dGUxbHAweS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjVhOTFlMTM5Y2U3YWFjZDFhYTcxMWMyIiwiYXVkIjoiaHR0cHM6Ly9wbGF0Zm9ybS5wcmVwcm9kLmhpdmVuZXQuY29tLyIsImlhdCI6MTcwNjUwNzQ5NCwiZXhwIjoxNzA2NTkzODk0LCJhenAiOiJzWENIaUk0b2ROMmt2OFA0NVNWY1Frc0tSc3liTEphUyIsInNjb3BlIjoib2ZmbGluZV9hY2Nlc3MiLCJwZXJtaXNzaW9ucyI6W119.hWFw9Jd4z0FbSjgq0WJ2Emc_kTWOPmiSrrs8bGC-f8qAVpgcYDExDG097pJ86QuYwBMI5FYlG9xg6DSlBLTXeCPYyIX0YpUj5M0qy8W2wtYMnkcelb_VWCtDyd6ol4cGsjUGTNqxBP0o2dk2HMcH3J3bZY73ZgKaEZiD5s1p1ZEdodr1c5rJBd-l_uTYA_sjY8TAiDIRD4dvLUDA0aK7nJNdumqdP2Vn4DP2Y6QT8kAgQhe47UyjHcA37fePeCYpcZjwrgnQvs4k7EfpfHKX6SddDkHXGeUBH_DjpWNUQks_ukGyA59KoH9tczyduD1_ql6g0uE5O7FINq-pWHpqQA"

AGENT_HEADERS = {
    "X-Trace-Id": "File upload start Puja",
    "X-Hive-Read-Key": hive_read_key,
    "Accept": "application/json",
    "Authorization": f"Bearer {token_hive_agent}",
}

file_upload_form_data = {
    "type": "FILE_UPLOAD",
    "jsonMetadata": json.dumps({
        "filename": "image_test.png",
        "filesize": "4261722",
        "parentMid": parent_mid,
        "createdtime": "20240124",
        "filePath": file_path
    }),
    "metadataVersion": "1.0.0",
}

conn.request(
        "GET",
        f"/polarion/MyPRest/v1/rest/workitems/get/status:closed%20AND%20cpRelatedWorkitems:{defect_id}%20AND%20type:codecontainer%20AND%20cpTargetNode:{cp_target_node}",
        payload,
        headers,
    )
    res2 = conn.getresponse()
    print(res2.status)

    # if res2 is None:
    #     print("The response is null")
    # else:
    #     data2 = res2.read()
    #     if not data2:
    #         print("Empty response")
    #         return
    #     data22 = data2.decode("utf-8")
    #     try:
    #         data22_json = json.loads(data22)
    #         # print(data22_json)
    #     except json.JSONDecodeError:
    #         # print(data22)
    #         print(f"{defect_id} Failed to decode JSON response")
    #         return

    #     if 'workItems' in data22_json:
    #         codecontainer_ids = [item['id'] for item in data22_json['workItems'] if item['type'] == "codecontainer"]
    #         print("Code Container IDs:", codecontainer_ids)
    #         if len(codecontainer_ids) > 0:
    #             for codecontainer_id in codecontainer_ids:
    #                 conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/{codecontainer_id}", payload, headers)
    #                 res3 = conn.getresponse()
    #                 data3 = res3.read()

    #                 if not data3:
    #                     print("Empty response for code container")
    #                     continue
    #                 data33 = data3.decode("utf-8")
    #                 try:
    #                     data33_json = json.loads(data33)
    #                 except json.JSONDecodeError:
    #                     print("Failed to decode JSON response for code container")
    #                     continue

    #                 print(data33_json['workItems'][0]['cpTargetNode']['value'])

    #                 if data33_json['workItems'][0]['cpTargetNode']['value'] == cp_target_node:
    #                     helper_two(defect_id, cp_target_node)
    #                     helper_mail(defect_id, cp_target_node)
    #                 res3.close()

    #     else:
    #         print("No work items found in the response.")

    res2.close()
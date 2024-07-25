def check_endpoint_info(sent_data, expected_data):
    print("sent_data", sent_data)
    for data in expected_data:
        print(data)
        if(sent_data.get(data) == None):
            return f"The {data} parameter is required!"
        


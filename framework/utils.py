def data_validation(response, sent_data):
    response = response.json()
    for key, value in response.items():
        if key == "id":
            continue
        if key not in sent_data:
            return False
        if value != sent_data[key]:
            return False
    return True


def field_validation(response, field, reference):
    response = response.json()
    for i in response:
        if i[field] != reference:
            return False
    return True

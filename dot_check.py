import requests

def get_carrier_info(usdot_number):
    # Get an API key from FMCSA before proceeding
    api_key = ""

    # API endpoint URL
    url = f"https://mobile.fmcsa.dot.gov/qc/services/carriers/{usdot_number}?webKey={api_key}"

    # Send the HTTP request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the carrier identification and authority status information
        carrier_name = data['content']['carrier']['legalName']
        authority_status = data['content']['carrier']['allowedToOperate']
        operation_desc = data['content']['carrier']['carrierOperation']
        # Return the results as a dictionary
        return {
            "Carrier Name": carrier_name,
            "Authority Status": authority_status,
            "Operation": operation_desc
        }
    else:
        return "Error retrieving carrier information."


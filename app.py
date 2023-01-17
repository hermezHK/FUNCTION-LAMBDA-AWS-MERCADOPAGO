import json
import os
import mercadopago


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    payment_data = json.loads(event["body"])
    # TODO implement
    

    
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    return {
        "statusCode": 200,
        "body":json.dumps( {
            "status": payment['status'],
            "status_detail": payment['status_detail'],
            "id":payment['id'],
            "payment_method": payment['payment_method'],
            
        }
      )    
    }
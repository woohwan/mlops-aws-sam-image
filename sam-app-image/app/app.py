import json
import myopslib


def lambda_handler(event, context):
    """Sample pure Lambda function
    
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # API Gateway 를 통한 요청인지 확인
    if 'body' in event:
        call_by_api_gateway = True
    else:
        call_by_api_gateway = False
    
    # API Gateway 를 통한 요청인 경우와 아닌 경우의 논리 분리
    if call_by_api_gateway:    
        if (event['httpMethod'] == 'GET' and 
            (event['path'] in ['/hello', '/hello/'])):
            response_payload = {"message": "hello ml"}
        elif (event['httpMethod'] == 'POST' and 
              (event['path'] in ['/predict', '/predict/'])):
            # 필요한 피처들이 모두 있는지 확인
            body = json.loads(event['body'])
            if myopslib.get_required_features() <= set(body.keys()):
                prediction = myopslib.predict(body)
                response_payload = {"message": 
                    f"MPG: {prediction}"}
            else:
                response_payload = {"message": 
                    "Incorrect request. "
                    f"event: {body}"}
        else:
            response_payload = {"message": 
                "Incorrect request method. "
                f"path: {event['path']}, "
                f"httpMethod: {event['httpMethod']}"}
    else:
        # 필요한 피처들이 모두 있는지 확인
        if myopslib.get_required_features() <= set(event.keys()):
            prediction = myopslib.predict(event)
            response_payload = {"message": 
                f"MPG: {prediction}"}
        else:
            response_payload = {"message": 
                "Incorrect event. "
                f"event: {event}"}

    return {
        "statusCode": 200,
        "body": json.dumps(response_payload),
    }
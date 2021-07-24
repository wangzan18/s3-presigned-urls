import boto3
import json
    
def lambda_handler(event, context):
    """Sample pure Lambda function
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format
        Event doc: 
    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    url = boto3.client('s3').generate_presigned_url(
        ClientMethod='get_object', 
        Params={'Bucket': 'code.wzlinux.com', 'Key': event['queryStringParameters']['key']},
        # Params={'Bucket': 'logs.transsion.com', 'Key': 'test.jpg'},
        ExpiresIn=3600)

    # print(url)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "url": url,
            # "location": ip.text.replace("\n", "")
        }),
    }
    
# lambda_handler('13', '12')
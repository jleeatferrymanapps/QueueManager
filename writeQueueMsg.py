    print("####################################")
    print("Begin Writing SQS Message")
    print("####################################")

    # Create a new message
    response = queue.send_message(MessageBody=json.dumps(messageBody))

    # The response is NOT a resource, but gives you a message ID and MD5
    print(response)
    print(response['ResponseMetadata']['HTTPStatusCode'])

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("The message was successfully written!")
    else:
        print("The message was not written and needs to be sent to Error Handler")

    print("SQS Message ID = " + response.get('MessageId'))
    print("SQS Message MD5 = " + response.get('MD5OfMessageBody'))

    print("####################################")
    print("Finish Writing SQS Message")
    print("####################################")
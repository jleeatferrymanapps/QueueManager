    print("####################################")
    print("Begin Deleting SQS Message")
    print("####################################")

    response_del = message[0].delete()

    print(response_del)
    print(response_del['ResponseMetadata']['HTTPStatusCode'])
    
    if response_del['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("The message was successfully deleted!")
    else:
        print("The message was not deleted and needs to be sent to Error Handler")


    print("####################################")
    print("Finish Deleting SQS Message")
    print("####################################")

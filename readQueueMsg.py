    print("####################################")
    print("Begin Reading SQS Message")
    print("####################################")

    # Read a message
    message = queue.receive_messages(AttributeNames=['All'])
    print(message[0])
    print("Message ID = " + message[0].message_id)
    print("Message Body = " + message[0].body)
    print(message[0].attributes)
    print("Message TimeStamp = " + message[0].attributes['SentTimestamp'])

    ### Question for Dana: How do you maintain popping out messages in order.
    ### How to pop out the functions into a package.
    ### Error Handling?
    ### How to call other web services?

    print("####################################")
    print("Finish Reading SQS Message")
    print("####################################")
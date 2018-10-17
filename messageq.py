
###### MESSAGE CLASS ######
class Message:

    def __init__(self,message,messageType):
        self.message = message
        self.messageType = messageType

    def getHeader(self):
        """ Reader can understand who sends the message"""
        return self.messageType

    def read(self):
        return self.message

###### MESSAGE QUEUE CLASS ######
class MessageQueue:

    def __init__(self,_name,_qsize,_queue=[]):
        self.name = _name
        self.qsize = _qsize
        self.queue = _queue

    def enqueue(self,message,messageType):
        """
            This function will be called from class.enqueue method.
            messageType argument will be filled by pre-determined number/string
            of mentioned class. If qsize is reached,writer process will halt/drop/
            try again to enqueue message.
        """
        if len(self.queue) == self.qsize:
            return -1
        else:
            self.queue.append(Message(message,messageType))

    def dequeue(self):
        if len(self.queue) == 0:
            return 0
        else:
            del self.queue[0]


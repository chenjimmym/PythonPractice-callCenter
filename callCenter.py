class call(object):
    def __init__(self, identity, name, phone, time, reason):
        self.identity = identity
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
    def display(self):
        print 'ID: {}, Name: {}, Phone: {}, Time: {}, Reason: {}'.format(self.identity, self.name, self.phone, self.time, self.reason)

class callCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)
    def addCall(self, call):
        self.calls.append(call)
        self.queue += 1
    def removeCall(self):
        self.calls.pop(0)
    def info(self):
        for data in self.calls:
            print 'Name: {} Phone Number: {}'.format(data.name, data.phone)
        print 'Queue:', self.queue



# call1 = call(123, 'Bob', '123-456-1234', '12:10pm', 'Service')
# call2 = call(12333333, 'Apple', '333-123-1233', '12:10pm', 'Service')
callCenter1 = callCenter()
callCenter1.addCall(call(123, 'Bobby', '123-456-1234', '12:10pm', 'Service'))
callCenter1.addCall(call(12333333, 'Apple', '333-123-1233', '12:10pm', 'Service'))
callCenter1.addCall(call(12333333, 'Jacob', '222-777-3333', '12:10pm', 'Service'))
callCenter1.removeCall()
callCenter1.info()
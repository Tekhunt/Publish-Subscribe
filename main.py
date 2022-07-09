from user import User
from dispatcher import Dispatcher
from subscriber import Subscriber
from publisher import Publisher
from message import Message



def main():
    user1 = User("hunter")
    print(user1.username)
    print(user1.created_automations)
    user1.create_user()
    print(user1.create_automation("Automation1"))
    print(user1.created_automations)
    dispatcher = Dispatcher()
    publisher_1 = Publisher(dispatcher)
    subscriber_1 = Subscriber(dispatcher, "topic1")
    message = Message()
    message.payload = "My Payload"
    message.topic = "topic1"
    publisher_1.publish(message)




if __name__ == "__main__":
    main()

class User:
    def __init__(self, username):
        self.username = username
        self.created_automations = []

    def create_user(self):
        return f"user with {self.username} created"

    def create_automation(self, automation_name, automation="Autoresponder"):
        if automation_name not in self.created_automations:
            self.created_automations.append(automation_name)
            return f"{automation} automation is created with name {automation_name}"
        return "You already have an automation with this name, please enter a different name for this automation"


user1 = User("hunter")
print(user1.username)
print(user1.created_automations)
user1.create_user()
print(user1.create_automation("feedback"))
print(user1.create_automation("feedback"))
print(user1.created_automations)

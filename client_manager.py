import json

class Client:
    def __init__(self, name, contact, amount, project_details, deadline):
        self.name=name
        self.contact=contact
        self.project_details=project_details
        self.deadline=deadline
        self.amount=amount
        self.paid=False

    def to_dict(self):
         return {
         "name":self.name,
         "contact":self.contact,
         "project_details":self.project_details,
         "deadline":self.deadline,
         "amount":self.amount,
         "paid":self.paid
                 }
        
    def from_dict(data):
        client=Client(data["name"],data["contact"],data["amount"],data["project_details"],data["deadline"])
        client.paid=data["paid"]
        return client
    
class ClientManager:
    def __init__(self):
        self.clients=[]

    def add_client(self,client):
        self.clients.append(client)

    def mark_as_paid(self,name):
        for client in self.clients:
            if client.name==name:
                 client.paid=True


    def get_all_clients(self):
        return self.clients
    
    def get_unpaid_clients(self):
        return [client for client in self.clients if not self.paid]

    def save_to_file(self, filename="clients.json"):
        with open(filename, "w") as f:
            json.dump([client.to_dict() for client in self.clients], f)

    def load_from_file(self, filename="clients.json"):
        try:
            with open(filename, "r") as f:
                data=json.load(f)
                self.clients=[Client.from_dict(item) for item in data]

        except FileNotFoundError:
            self.clients=[]

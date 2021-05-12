import json


class RestAPI:
    def __init__(self, database=None):
        self.users = database or {'users': []}


    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                payload = json.loads(payload)["users"]
                return json.dumps({
                    "users": [
                        u for u in self.users["users"] 
                        if u["name"] in payload
                    ]
                })
            else:
                return json.dumps(self.users)


    def post(self, url, payload=None):
        if url == "/add":
            name = json.loads(payload)["user"]
            user = {
                "name": name, 
                "owes": {}, 
                "owed_by": {}, 
                "balance": 0.0
            }
            self.users["users"].append(user)
            return json.dumps(user)
        elif url == "/iou":
            payload = json.loads(payload)
            amount = payload["amount"]
            lender = payload["lender"]
            borrower = payload["borrower"]
            # lender dict index
            ldi = next((
                i for i, user in enumerate(self.users["users"]) 
                if user["name"] == lender
            ))
            # borrower dict index
            bdi = next((
                i for i, user in enumerate(self.users["users"]) 
                if user["name"] == borrower
            ))
            lender_dict = self.users["users"][ldi]
            borrower_dict = self.users["users"][bdi]
            old_debt = lender_dict["owes"].get(borrower, 0)

            if old_debt - amount > 0:
                lender_dict["owes"][borrower] -= amount
                borrower_dict["owed_by"][lender] = old_debt - amount
            elif old_debt - amount < 0:
                lender_dict["owes"].pop(borrower, None)
                lender_dict["owed_by"][borrower] = amount - old_debt
                borrower_dict["owed_by"].pop(lender, None)
                borrower_dict["owes"][lender] = amount - old_debt
            else:
                lender_dict["owes"].pop(borrower, None)
                lender_dict["owed_by"].pop(borrower, None)
                borrower_dict["owes"].pop(lender, None)
                borrower_dict["owed_by"].pop(lender, None)
            lender_dict["balance"] += amount
            borrower_dict["balance"] -= amount

            return json.dumps({
                "users": [
                    user for user in self.users["users"] 
                    if user["name"] in (lender, borrower)
                ]
            })


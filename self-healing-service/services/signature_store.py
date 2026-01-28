from db.mongo import elements

class SignatureStore:

    def get(self, element_key):
        return elements.find_one({"element_key": element_key})

    def save(self, element_key, signature, neighbors, intent, old_dom):
        elements.update_one(
            {"element_key": element_key},
            {
                "$set": {
                    "signature": signature,
                    "neighbors": neighbors,
                    "intent": intent,
                    "old_dom": old_dom
                }
            },
            upsert=True
        )

from Items import *


class ItemsDAO:

    # Function to insert the object into database.
    def insertItem(self, session, item):
        session.add(item)
        session.commit()
        #print('Record in Table Items >>', item.id)

    # Function to Query the object into database.
    def getItemByName(self, session, queryValue):
        itemByName = session.query(Items).filter(Items.name == queryValue).first()
        #print(itemByName)
        return itemByName

        # Function to Query the object into database.

    def getItemById(self, session, queryValue):
        itemById = session.query(Items).filter(Items.name == "Sugar").first()
        return itemById

    def getAllItems(self, session):
        itemByName = session.query(Items).all()
        #print(itemByName)
        return itemByName
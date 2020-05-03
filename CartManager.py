from DataLoad import DataLoad, loadInventory
from DatabaseManager import DatabaseManager
from ItemsDAO import ItemsDAO


class CartManager:

    def returnAllAvailableItems(self):
        dm = DatabaseManager()
        loadInventory(dm)
        itemsDAO = ItemsDAO()
        items = itemsDAO.getAllItems(dm.getSession())
        dm.getSession().close()
        return items

    def getItemById(self, itemId):
        dm = DatabaseManager()
        itemsDAO = ItemsDAO()
        item = itemsDAO.getItemById(dm.getSession(), itemId)
        dm.getSession().close()
        return item

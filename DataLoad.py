from DatabaseManager import DatabaseManager
from ItemsDAO import ItemsDAO
from PaymentsDAO import PaymentsDAO
from Items import *


def loadInventory(databaseManager):
    itemDAO = ItemsDAO()
    item1 = Items(name='Sugar', price=2.99)
    item2 = Items(name='Salt', price=0.99)
    item3 = Items(name='Code', price=3.99)
    item4 = Items(name='Bread', price=1.99)
    item5 = Items(name='Milk', price=2.99)
    item6 = Items(name='Egg', price=5.99)
    itemDAO.insertItem(databaseManager.getSession(), item1)
    itemDAO.insertItem(databaseManager.getSession(), item2)
    itemDAO.insertItem(databaseManager.getSession(), item3)
    itemDAO.insertItem(databaseManager.getSession(), item4)
    itemDAO.insertItem(databaseManager.getSession(), item5)
    itemDAO.insertItem(databaseManager.getSession(), item6)


class DataLoad:
    pass

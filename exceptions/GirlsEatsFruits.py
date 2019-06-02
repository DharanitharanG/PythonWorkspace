#from exceptions import CustomExceptions as ex;
from exceptions.CustomExceptions import MythriDoesNotLikeException;
from exceptions.CustomExceptions import SupriyaHatesThisException;
fruit = 'Orange'; fruit2 = 'Apple'; fruit3 = 'Banana'; fruit4 = 'Mango'

def supriyaEatsTheFruit(fruitName):
    if fruitName in ['Apple','Orange']:
        print("Supriya likes it... now eating")
    else:
        # print("supriya doesnot eat")
        raise SupriyaHatesThisException("supriya doesnot like "+fruitName)


def mythriEatsTheFruit(fruitName):
    if fruitName in ['Banana','Orange']:
        print("Mythri likes it... now eating")
    else:
        # print("Mythri doesnot eat")
        raise MythriDoesNotLikeException("Mythri doesnot like " + fruitName)


try:
 supriyaEatsTheFruit('Orange')
 mythriEatsTheFruit('Mango')
except MythriDoesNotLikeException as mye:
 print(repr(mye)," so give some other fruit")
except SupriyaHatesThisException as sue:
 print(repr(sue), " so give some other fruit")


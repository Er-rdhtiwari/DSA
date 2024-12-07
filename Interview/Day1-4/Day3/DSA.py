import logging
from turtledemo.penrose import start

logging.basicConfig(
    filename="./DSA.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def binarySearch(sortedArray, element):
    ArrayLen = len(sortedArray)
    start = 0
    end = ArrayLen

    while start <= end:
        mid = int((start + end) / 2)
        if sortedArray[mid] == element:
            return mid
        elif sortedArray[mid] > element:
            end = mid
        elif sortedArray[mid] < element:
            start = mid
        else:
            return False

def PalindromeCheck(inputString):
    left = 0
    right = len(inputString)-1

    while left<=right :
        if inputString[right] == inputString[left]:
            right = right-1
            left = left+1
        else:
            return False
    return True

def FindPair(inputList,targetsum):
    pair = list()

    for i in range(len(inputList)):
        for j in range(i+1, len(inputList)):
            if inputList[i] + inputList[j] == targetsum:
                pair.append((inputList[i],inputList[j]))
    if pair:
        return pair
    return False




if __name__ == "__main__":
    logger.info("Logger Integrated")
    shortedArray = [0,1,9]
    find_element1 = 1
    find_element2 = 9
    pos1 = binarySearch(shortedArray, find_element1)
    logger.info(f"pos1 : {pos1}")
    pos2 = binarySearch(shortedArray, find_element2)
    logger.info(f"pos2: {pos2}")
    isPalindrom = PalindromeCheck("madam")
    logger.info(f"madam isPalindrom: {isPalindrom}")
    isPalindrom = PalindromeCheck("racecar")
    logger.info(f"racecar isPalindrom: {isPalindrom}")
    targetSum = FindPair((1,3,5,6,0,2,4),6)
    logger.info(f"targetSum 6: {targetSum}")

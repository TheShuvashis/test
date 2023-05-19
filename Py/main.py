import json
from datetime import datetime
import calendar

newTask = str()
taskToRemoveIndex = int()

projectsCompleted = 0
yearsOfServices = int()
startYear = 2012


tasks = {}

def SaveData():
    file = open("file.json", "w")
    json.dump(tasks, file)
    file.close()

def LoadData():
    try:
        with open("file.json", "rb") as file:
            data = json.load(file)
            return data
        
    except:
        print("Error while loading file")


def AddTask(_newTask):
    tasks[_newTask] = False

def RemoveTask(_taskToRemoveIndex):
    tasks.pop(_taskToRemoveIndex)

def CheckTasks():
    for item in tasks:
        x = 0
        if item == True:
            x += 1
            if x == len(tasks):
                projectsCompleted += 1

def TaskComplete(taskName):
    tasks[taskName] = True
    if taskName[taskName] == True:
        tasks[taskName] = False

def DetermineYearsOfService():
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    if currentMonth == 9:
        return currentYear - startYear + 1
    
def CalculateRetentionRate(_contractYear, _renewals, _contractAmount):
    retention = _contractYear + 2

    retentionRate = (_renewals / _contractAmount) * 100
    return retentionRate
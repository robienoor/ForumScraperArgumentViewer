from dataBaseConnector import dataBaseConnector

def startArgGraph(drug):

    # TODO: If I'm not in the folder how do I go a level up and get the file in the higher folder
    dbobj = dataBaseConnector('DBConnector.ini')

    experiencesSQL = "SELECT * FROM Experiences WHERE Drug = '%s'" % (drug)
    experiencesData = dbobj.execute(experiencesSQL)

    sideEffectsPresentSQL = "SELECT * FROM SideEffectsPresent Drug = '%s'" % (drug)
    sideEffectsPresentData = dbobj.execute(sideEffectsPresentSQL) 

    symptomConditionSQL = "SELECT * FROM SymptomCondition Drug = '%s'" % (drug)
    symptomConditionData = dbobj.execute(symptomConditionSQL)

    supplementaryDrugsSQL = "SELECT * FROM SupplementaryDrugs = '%s'" % (drug)
    supplementaryDrugsData = dbobj.execute(supplementaryDrugsSQL)

    print('Pulled out all the data')


#drug = input('Please enter a medication:\n')

startArgGraph('tamoxifen')
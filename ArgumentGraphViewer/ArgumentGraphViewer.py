from dataBaseConnector import dataBaseConnector
from dungEvaluator import dungEvaluator

def evalArgGraph():

    # TODO: If I'm not in the folder how do I go a level up and get the file in the higher folder
    dbobj = dataBaseConnector('DBConnector.ini')

    argTallySQL = "SELECT * FROM CompleteArgTally"
    results = dbobj.execute(argTallySQL);

    for row in results:
        row = dict(row)

        post = row['post']
        rating = row['Rating']

        noA = row['PosExp']
        noB = row['NegExp']
        noC = row['NoSideEffectsPresent']
        noD = row['SideEffectsPresent']
        noE = row['SymtomsOK']
        noF = row['SymtomsNotOK']

        positiveNodes = ['A', 'C', 'E']

        dungEval = dungEvaluator(noA, noB, noC, noD, noE, noF)
        groundedExtension = dungEval.getGroundedExtensions()

        if not groundedExtension:
            groundedExtensionStr = ''
            sentimentClass = '0'
        else:
            groundedExtensionStr = str(groundedExtension).strip('[]')
            groundedExtensionStr = str(groundedExtension).strip("'")

            # TODO: Dangerously assumes that no sets exist with two classes. Move to DB
            for node in groundedExtension:
                if node[0] in positiveNodes:
                    sentimentClass = '1'
                    break
                else:
                    sentimentClass = '-1'
        

        insertSQL = "INSERT INTO dungtally (Post, GroundedSemantics, Rating, Class) VALUES (%s, %s, %s, %s)"
        data = (post, groundedExtensionStr, rating, sentimentClass)
        dbobj.insert(insertSQL, data)

    print('success')
    

evalArgGraph()
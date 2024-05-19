# rank scores leetcode 178

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    allscores=[]
    for i in range(len(scores)):
        s=scores['score'][i]
        allscores.append(s)
    allscores.sort(reverse = True)
    if len(scores)==0:
        return pd.Dataframe([None], columns = [ 'score', 'rank'])
    result = []
    rnk = 1
    result.append([ allscores[0], rnk])
    for i in range(1, len(allscores)):
        if allscores[i] != allscores[i - 1]:
            rnk = rnk+1
        result.append([allscores[i],rnk])
    return pd.DataFrame(result, columns = [ 'score', 'rank'])

# short method

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores['score'].rank(method = 'dense', ascending = False)
    return scores[['score', 'rank']].sort_values(by=['score'], ascending = False)
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json
import pandas as pd
from django.core.files.storage import FileSystemStorage
import joblib

model=joblib.load('logreg_cv.pkl')
selected=joblib.load('selected.pkl')


def scoreJson(request):
  
    values = selected.values()
    values_list = list(values)
    returnedJson = {"result": values_list}
    print(returnedJson)
    return JsonResponse(returnedJson)


def scoreFile(request):

    """
d = {'Feature_2': [28.0], 'Feature_3': [130.0], 'Feature_8': [1.0], 'Feature_10': [0.0], 'Feature_17': [0.0],  'Feature_21': [0.0],'Feature_29': [0.0], 'Feature_34': [0.0], 'Feature_38': [0.0], 'Feature_39': [0.0], 'Feature_42': [0.0],'Feature_46': [0.0]}
df = pd.DataFrame(d)


print(logreg_cv.predict_proba(df)[0])

print("accuracy: ", logreg_cv.best_score_)
    """
    print(request.body)
    d = json.loads(request.body)
    print(d)
    df = pd.DataFrame(d)
    print(df)

    score = model.predict_proba(df)[0].tolist()

    return JsonResponse({'result':score})
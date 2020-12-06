from django.shortcuts import render
from tableqa.agent import Agent
import pandas as pd
from django.utils.datastructures import MultiValueDictKeyError


def simple_upload(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            query = request.POST['query']
            df = pd.read_csv(myfile)
            agent = Agent(df)
            database_result = agent.query_db(query)
            database_query = agent.get_query(question=query)
            return render(request, 'agent/simple_upload.html', {
                'database_result': database_result,
                'database_query': database_query
            })
        return render(request, 'agent/simple_upload.html')
    except MultiValueDictKeyError:
        database_result = "Please Upload a CSV"
        return render(request, 'agent/simple_upload.html',{
            'database_result':database_result
        })

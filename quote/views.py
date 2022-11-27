from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import os
import random
import pandas as pd
from django.utils.decorators import method_decorator
from users.decorator import authenticated_user  
from datetime import datetime

class quoteRandom(APIView): 
    @method_decorator(authenticated_user)      
    def get(self , request , format=None):
        root_path = 'jsons'
        count = 1          
        quoteFile = os.path.join(root_path, 'quotes.json')
        authorsFile = os.path.join(root_path, 'authors.json')   
        with open(quoteFile , 'r') as file:
            quotes = json.load(file)
        randomQuote = random.choice(quotes)
        searced = randomQuote['id'] 
        randomQuote = dict(randomQuote) 
        with open(authorsFile , 'r') as file:
            authors = pd.read_json(file)
        s = searced  
        for index, row in authors.iterrows():
            if s in row['quoteIds']:                    
                author = row['author'] 
                randomQuote.update(author=author)
           
        if len(request.session.items()) < 100:
            if s not in request.session:
              
                request.session[s] = count        
            else: 
                if request.session[s] < 100:
                   request.session[s] =  request.session[s] + 1   
                else: 
                    pass
        else: 
            df = pd.DataFrame(data=request.session.items() )
            df.columns = ['quoteId', 'count']
            now = datetime.now()
            now = now.strftime("%d_%m_%Y_%H_%M_%S")
            name = 'quotes_api_report_' + now + '.xlsx'
            file = df.to_excel(name)
            

            
          
        return Response(randomQuote )
       

        
        
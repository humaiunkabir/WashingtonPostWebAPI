from django.shortcuts import render
from newsapp.models import NewsPost
from rest_framework.viewsets import ModelViewSet
from newsapp.serializers import NewsPostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import csv

# Create your views here.
class NewsPostAPIViewSet(ModelViewSet):

    # Assign file path
    filepath='/home/abfl/GITProject/Python/WebScrappingFull/washingtonpost.csv'

    # Get data from database
    queryset = NewsPost.objects.all()

    # Check data not found from database then read data from csv file
    if not queryset:
        with open(filepath, 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                # Chcek blank data
                if row['title'] and row['content'] and row['images']:
                    # Store data in database, those data found from csv file
                    NewsPost.objects.create(
                        title=row['title'],
                        content=row['content'],
                        images =row['images']
                    )
    serializer_class = NewsPostSerializer

    # Only permits for get request
    permission_classes = [IsAuthenticatedOrReadOnly]
 
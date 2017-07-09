# -*- coding: utf-8 -*-
from django.conf import settings
import sys, os
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AKIHA_for_web.settings")
import django
django.setup()
from sorter.models import SortedIdols, SuggestedIdols


class InsertInitialIdols():
    
    SORTED_FILE = "sorter/static/MobaMas.txt"
    SUGGESTED_FILE = "sorter/static/Suggest.txt"
    def main(self):
        self.cleanup_tables()
        # Open Sorted File
        self.open_and_insert_data(self.SORTED_FILE)
        self.open_and_insert_data(self.SUGGESTED_FILE)
    
    
    def open_and_insert_data(self,file_name):
        with open(file_name,"r", encoding="utf-8") as f:
            for l in f:
                l_cleanse = l.rstrip("\r\n").split(",")
                if not l_cleanse[0][0] == "#": #コメント行でなかった場合
                    if "Suggest" in file_name:
                        b = SuggestedIdols.objects.create(name=l_cleanse[0],
                                           bust=l_cleanse[1],
                                           waist=l_cleanse[2],
                                           hip=l_cleanse[3],
                                           age=l_cleanse[4],
                                           height=l_cleanse[5],
                                           weight=l_cleanse[6],
                                           cute=l_cleanse[7],
                                           cool=l_cleanse[8],
                                           passion=l_cleanse[9],
                                           pictures=l_cleanse[10])
                    else:
                        b = SortedIdols.objects.create(name=l_cleanse[0],
                                           bust=l_cleanse[1],
                                           waist=l_cleanse[2],
                                           hip=l_cleanse[3],
                                           age=l_cleanse[4],
                                           height=l_cleanse[5],
                                           weight=l_cleanse[6],
                                           cute=l_cleanse[7],
                                           cool=l_cleanse[8],
                                           passion=l_cleanse[9],
                                           pictures=l_cleanse[10])                        
    
    def cleanup_tables(self):
        SortedIdols.objects.all().delete()
        SuggestedIdols.objects.all().delete()
                    

iii = InsertInitialIdols()
iii.main()

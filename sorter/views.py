# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse
from sorter.models import SortedIdols, SuggestedIdols
from sorter.models import MergeSortChoices

import random
from sorter.merge_sort import MergeSort
from sorter.Regression import RegressionClass
from django.template.response import TemplateResponse


# Create your views here.


def sorter(request):
    response = None
    choice = request.POST.get('idol_select')
    
    if choice == None:
        #getでリクエストを投げられたとき=マージソート開始

        idols_id_list = []
        idols_id_query = SortedIdols.objects.values("id")
        for iiq in idols_id_query:
            idols_id_list.append(iiq["id"])
        random.shuffle(idols_id_list)
        
        b = MergeSortChoices.objects.create(
                shuffled_idols=idols_id_list,
                finish_mergesort = False
            )
        request.session["mergesort_id"] = b.id
        
        context_idols = MergeSort.merge_with_array(idols_id_list,[])
        
    else:
        current_mergesort_status = MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0]
        choice_boolean = 0 if choice == "right" else 1
        
        idols_id_list = current_mergesort_status.shuffled_idols
        if current_mergesort_status.choices == None:
            current_mergesort_status.choices = [choice_boolean,]
        else:
            current_mergesort_status.choices.append(choice_boolean)
        
        context_idols = MergeSort.merge_with_array(idols_id_list,current_mergesort_status.choices)
        
        current_mergesort_status.save()
    
    if len(context_idols) == 2:
        context = {"left_picture": SortedIdols.objects.all().filter(id=context_idols[0]).get().pictures,
                   "right_picture": SortedIdols.objects.all().filter(id=context_idols[1]).get().pictures,
                   "left_name": SortedIdols.objects.all().filter(id=context_idols[0]).get().name,
                   "right_name": SortedIdols.objects.all().filter(id=context_idols[1]).get().name
                   }
        return render(request, "sorter/sorter.html", context)
    
    #マージソートが終了すると全件返ってくるため。
    else:
        current_mergesort_status = MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0]
        current_mergesort_status.mergesort_ans = context_idols
        current_mergesort_status.finish_mergesort = True
        current_mergesort_status.save()
        rc = RegressionClass()
        rc.register_with_database(context_idols)
        rc.normalize_coef()
        rc.regression()
        
        #データベースにSuggested_scoreを投入
        rc.return_predict_with_database(request.session["mergesort_id"])
        
        
        context = {"suggested_name": MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0].most_preferred_name,
                   "suggested_picture": MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0].most_preferred_picture,
                   "coef": rc.return_coef_dict(request.session["mergesort_id"])
        }
        
        return render(request, "sorter/result.html",context)

def akiha_help(request):
    response = "ヘルプ"
    return HttpResponse(response)

def result(request):
    #マージソートが終わっていたら
    if MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0].finish_mergesort == True:
        context = {"suggested_picture": MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0].most_preferred_picture,
                       "suggested_name":MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0].most_preferred_name,
                       "coef": convert_list_to_dict(
                           MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0].pref_coefficient)
        }
        return render(request, "sorter/result.html", context)
    else:
        #マージソートが終わっていないときにresultを開こうとしたら
        return TemplateResponse(request,"sorter/result_not_complete.html")
        

def sorted(request):
    sorted_complete_list = MergeSortChoices.objects.all().filter(id=request.session["mergesort_id"])[0].mergesort_ans
    idols_sorted_list = []
    if not sorted_complete_list == None:
        for scl in sorted_complete_list:
            q = SortedIdols.objects.all().filter(id=scl).values("name")[0]["name"]
            idols_sorted_list.append(q)
    
        context = {"idols_list": idols_sorted_list}
        return render(request,"sorter/sorted.html",context)
    else:
        context = None
        return TemplateResponse(request,"sorter/sorted_not_complete.html")
    

def convert_list_to_dict(convert_list):
    ret = {"bust": convert_list[0],
           "waist": convert_list[1],
           "hip": convert_list[2],
           "age": convert_list[3],
           "height": convert_list[4],
           "weight": convert_list[5],
           "cute": convert_list[6],
           "cool": convert_list[7],
           "passion": convert_list[8],
    }
    return ret
    
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from armydbapp.models import *
from django.core.validators import URLValidator, ValidationError
from django.db import IntegrityError
from hashlib import md5
import datetime
import queue
import io
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator


today = datetime.datetime.now()
today = datetime.date(today.year,today.month,today.day)     

def update_soldier_status():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        names=[]
        dof3at=[]
        soldier_num=[]
        i=1
        for soldier in soldier_list:
                names.append(soldier.name)
                
                return_date = soldier.return_date
                present = soldier.is_present
                soldier_num.append(i)
                i+=1
                

                if soldier.is_at_vacation == False and present == True and soldier.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation = False)
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=False)
                                        elif present == False:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=True)
                
                if soldier. is_at_punishment == False :
                        pass
                else:

                        for punishment in soldiers_punishments:
                                if punishment.soldier.soldier_id == soldier.soldier_id:
                                        if today < punishment.end_date :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=punishment)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=True)
                                        elif today > punishment.end_date:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=False)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=None)


        for soldier in soldier_list:
                if soldier.service_end_date in dof3at:
                        pass
                else:
                        dof3at.append(soldier.service_end_date)
        dof3at.sort()

def update_soldier_status():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        names=[]
        dof3at=[]
        soldier_num=[]
        i=1
        for soldier in soldier_list:
                names.append(soldier.name)
                return_date = soldier.return_date
                present = soldier.is_present
                soldier_num.append(i)
                i+=1

                

                if soldier.is_at_vacation == False and present == True and soldier.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation = False)
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=False)
                                        elif present == False:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=True)
                
                if soldier. is_at_punishment == False :
                        pass
                else:

                        for punishment in soldiers_punishments:
                                if punishment.soldier.soldier_id == soldier.soldier_id:
                                        if today < punishment.end_date :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=punishment)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=True)
                                        elif today > punishment.end_date:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=False)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=None)


        for soldier in soldier_list:
                if soldier.service_end_date in dof3at:
                        pass
                else:
                        dof3at.append(soldier.service_end_date)
        dof3at.sort()

def update_soldier_status():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        names=[]
        dof3at=[]
        soldier_num=[]
        i=1
        for soldier in soldier_list:
                names.append(soldier.name)
                return_date = soldier.return_date
                present = soldier.is_present
                soldier_num.append(i)
                i+=1

                

                if soldier.is_at_vacation == False and present == True and soldier.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation = False)
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=False)
                                        elif present == False:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=True)
                
                if soldier. is_at_punishment == False :
                        pass
                else:

                        for punishment in soldiers_punishments:
                                if punishment.soldier.soldier_id == soldier.soldier_id:
                                        if today < punishment.end_date :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=punishment)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=True)
                                        elif today > punishment.end_date:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=False)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=None)


        for soldier in soldier_list:
                if soldier.service_end_date in dof3at:
                        pass
                else:
                        dof3at.append(soldier.service_end_date)
        dof3at.sort()

def update_soldier_status():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        names=[]
        dof3at=[]
        soldier_num=[]
        i=1
        for soldier in soldier_list:
                names.append(soldier.name)
                return_date = soldier.return_date
                present = soldier.is_present
                soldier_num.append(i)
                i+=1

                

                if soldier.is_at_vacation == False and present == True and soldier.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation = False)
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=False)
                                        elif present == False:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=True)
                
                if soldier. is_at_punishment == False :
                        pass
                else:

                        for punishment in soldiers_punishments:
                                if punishment.soldier.soldier_id == soldier.soldier_id:
                                        if today < punishment.end_date :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=punishment)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=True)
                                        elif today > punishment.end_date:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=False)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=None)


        for soldier in soldier_list:
                if soldier.service_end_date in dof3at:
                        pass
                else:
                        dof3at.append(soldier.service_end_date)
        dof3at.sort()


def home(request):
    if request.method == "GET":
            if request.user.is_authenticated:
                return redirect ("armydbapp:index")
            return render(request, "armydbapp/home.html")
    else:
            return HttpResponse(status=500)

def login_view(request):
    if request.user.is_authenticated:
        return redirect ("armydbapp:index")
        
    return render(request, 'armydbapp/login.html')

def login_user(request):
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            if not username or not password:
                    return render(request, "armydbapp/login.html", {"error":"Enter all required fields"})
            user = authenticate(request, username=username, password=password)
            if user is not None:
                    login(request, user)
                    return redirect("armydbapp:index")
                    
            else:
                    return render(request, "armydbapp/login.html", {"error":"Wrong username or password"})
    else:
            return redirect("armydbapp:index")
            

def logout_user(request):
    logout(request)
    return redirect("armydbapp:login")

def index(request):
    if request.method == "GET":
        user = request.user
        names=[]

        points_dec_S1 = {"قياس1":0,"13احمد":0,"11رياض":0,"11محمود":0,"12رياض":0,"12محمود":0,"13رياض":0,"13محمود":0,"14رياض":0,"14محمود":0,"15رياض":0,"15محمود":0,"1سعيد":0,"1عرب":0,"2سعيد":0,"2عرب":0}
        points_dec_S2 = {"قياس2":0,"3عرب":0,"4سعيد":0,"4عرب":0,"5عرب":0,"6عرب":0,"7عرب":0,"8عرب":0,"9سعيد":0,"9عرب":0}
        points_dec_S3 = {"قياس3":0,"11عرب":0,"12سعيد":0,"13سعيد":0,"13عرب":0}

        points_list_S1 = ["قياس1","13احمد","11رياض","11محمود","12رياض","12محمود","13رياض","13محمود","14رياض","14محمود","15رياض","15محمود","1سعيد","1عرب","2سعيد","2عرب"]
        points_list_S2 = ["قياس2","3عرب","4سعيد","4عرب","5عرب","6عرب","7عرب","8عرب","9سعيد","9عرب"]
        points_list_S3 = ["قياس3","11عرب","12سعيد","13سعيد","13عرب"]

        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")

        for soldier in soldier_list:

                names.append(soldier.name)

                for point in points_list_S1:
                        if soldier.point == point and soldier.current_army_unit != "قيادة الكتيبة" and soldier.is_present:
                                points_dec_S1[point]=points_dec_S1.get(point)+1
                
                for point in points_list_S2:
                        if soldier.point == point and soldier.current_army_unit != "قيادة الكتيبة":
                                points_dec_S2[point]=points_dec_S2.get(point)+1
                
                for point in points_list_S3:
                        if soldier.point == point and soldier.current_army_unit != "قيادة الكتيبة":
                                points_dec_S3[point]=points_dec_S3.get(point)+1
                
                if soldier.is_absent == True:
                        return_date = soldier.return_date 
                        if  return_date!=None:
                                days_absent=daysBetweenDates(return_date.year,return_date.month,return_date.day,today.year,today.month,today.day)
                        days_absent = str(days_absent)
                        Soldier.objects.filter(soldier_id = soldier.soldier_id).update(days_absent = days_absent)
        
        
        values_list_s1 = list(points_dec_S1.values())
        values_list_s2 = list(points_dec_S2.values())
        values_list_s3 = list(points_dec_S3.values())



        squad = "قيادة السرية الأولي"

        #update_soldier_status()
        no_sarfaya,no_salary,salary = sarfaya_numbering()
        dof3at, radif_specialities, dof3a_number_of_specialities, dof3a_total,total_speciality = dof3at_radif()
        sum_number_of_specialities_sub_officer, number_of_specialities_sub_officer,awaiting_trial,sum_number_of_specialities, number_of_specialities, specialities, number_of_at_vacation_sick, number_late_unit, number_late_vacation, number_punished, number_of_soldiers, number_of_at_vacation, number_prisioned, number_out, number_absent, number_mission,number_here, number_returning = numbering()
        number_of_at_vacation_sick_k10_head, number_of_soldiers_k10_head, number_of_at_vacation_k10_head, number_prisioned_k10_head, number_out_k10_head, number_absent_k10_head, number_mission_k10_head, number_here_k10_head = numbering_k10_head()
        number_of_at_vacation_sick_s1_head, number_of_soldiers_s1_head, number_of_at_vacation_s1_head, number_prisioned_s1_head, number_out_s1_head, number_absent_s1_head, number_mission_s1_head, number_here_s1_head = numbering_s1_head()
        number_of_at_vacation_sick_s2_head, number_of_soldiers_s2_head, number_of_at_vacation_s2_head, number_prisioned_s2_head, number_out_s2_head, number_absent_s2_head, number_mission_s2_head, number_here_s2_head = numbering_s2_head()
        number_of_at_vacation_sick_s3_head, number_of_soldiers_s3_head, number_of_at_vacation_s3_head, number_prisioned_s3_head, number_out_s3_head, number_absent_s3_head, number_mission_s3_head, number_here_s3_head = numbering_s3_head()
        return render(request, "armydbapp/index.html", {"user":user,
                                "values_list_s1":values_list_s1,
                                "values_list_s2":values_list_s2,
                                "values_list_s3":values_list_s3,
                                "names":names,
                                "number_punished":number_punished,
                                "number_of_soldiers":number_of_soldiers,
                                "number_of_soldiers":number_of_soldiers,
                                "number_of_at_vacation":number_of_at_vacation,
                                "number_prisioned":number_prisioned,
                                "number_out":number_out,
                                "number_absent":number_absent,
                                "number_mission":number_mission,
                                "number_here":number_here,
                                "number_returning":number_returning,
                                "number_late_vacation":number_late_vacation,
                                "number_late_unit":number_late_unit,
                                "number_of_at_vacation_sick":number_of_at_vacation_sick,
                                "number_of_at_vacation_sick_k10_head":number_of_at_vacation_sick_k10_head,
                                "number_of_soldiers_k10_head":number_of_soldiers_k10_head, 
                                "number_of_at_vacation_k10_head":number_of_at_vacation_k10_head, 
                                "number_prisioned_k10_head":number_prisioned_k10_head, 
                                "number_out_k10_head":number_out_k10_head, 
                                "number_absent_k10_head":number_absent_k10_head, 
                                "number_mission_k10_head":number_mission_k10_head, 
                                "number_here_k10_head":number_here_k10_head,
                                "number_of_at_vacation_sick_s1_head":number_of_at_vacation_sick_s1_head,
                                "number_of_soldiers_s1_head":number_of_soldiers_s1_head, 
                                "number_of_at_vacation_s1_head":number_of_at_vacation_s1_head, 
                                "number_prisioned_s1_head":number_prisioned_s1_head, 
                                "number_out_s1_head":number_out_s1_head, 
                                "number_absent_s1_head":number_absent_s1_head, 
                                "number_mission_s1_head":number_mission_s1_head, 
                                "number_here_s1_head":number_here_s1_head,
                                "number_of_at_vacation_sick_s2_head":number_of_at_vacation_sick_s2_head,
                                "number_of_soldiers_s2_head":number_of_soldiers_s2_head, 
                                "number_of_at_vacation_s2_head":number_of_at_vacation_s2_head, 
                                "number_prisioned_s2_head":number_prisioned_s2_head, 
                                "number_out_s2_head":number_out_s2_head, 
                                "number_absent_s2_head":number_absent_s2_head, 
                                "number_mission_s2_head":number_mission_s2_head, 
                                "number_here_s2_head":number_here_s2_head,
                                "number_of_at_vacation_sick_s3_head":number_of_at_vacation_sick_s3_head,
                                "number_of_soldiers_s3_head":number_of_soldiers_s3_head, 
                                "number_of_at_vacation_s3_head":number_of_at_vacation_s3_head, 
                                "number_prisioned_s3_head":number_prisioned_s3_head, 
                                "number_out_s3_head":number_out_s3_head, 
                                "number_absent_s3_head":number_absent_s3_head, 
                                "number_mission_s3_head":number_mission_s3_head, 
                                "number_here_s3_head":number_here_s3_head,
                                "number_of_specialities":number_of_specialities, 
                                "specialities":specialities,
                                "sum_number_of_specialities":sum_number_of_specialities,
                                "awaiting_trial":awaiting_trial,
                                "dof3at":dof3at,
                                "radif_specialities":radif_specialities,
                                "dof3a_number_of_specialities":dof3a_number_of_specialities,
                                "number_of_specialities_sub_officer":number_of_specialities_sub_officer,
                                "sum_number_of_specialities_sub_officer":sum_number_of_specialities_sub_officer,
                                "squad":squad,
                                "dof3a_total":dof3a_total,
                                "total_speciality":total_speciality,
                                "no_sarfaya":no_sarfaya,
                                "no_salary":no_salary,
                                "salary":salary,
                                },)

def present_list (request):
        place = request.GET.get('place')
        soldiers = Soldier.objects.all()
        soldiers_punishments = SoldierPunishments.objects.all()
        soldiers_list = []
        names=[]
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]

        
        for soldier in soldiers:
                names.append(soldier.name)
                if soldier.is_present == True:
                        if soldier.is_at_punishment == False and soldier.is_in_mission == False and soldier.is_out == False:
                                if place == 'all':
                                        soldiers_list.append(soldier)
                                elif place == 's1':
                                        if soldier.current_army_unit in s1:
                                                soldiers_list.append(soldier)
                                elif place == 's2':
                                        if soldier.current_army_unit in s2:
                                                soldiers_list.append(soldier)
                                elif place == 's3':
                                        if soldier.current_army_unit in s3:
                                                soldiers_list.append(soldier)
                                elif place == 's': #kayadat el katiba
                                        if soldier.current_army_unit == "قيادة الكتيبة":
                                                soldiers_list.append(soldier)

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldiers_list,"soldiers_punishments": soldiers_punishments,"names":names,},)

def absent_indexList (request):
        place = request.GET.get('place')
        soldiers = Soldier.objects.all()
        soldiers_punishments = SoldierPunishments.objects.all()
        soldiers_list = []
        names=[]
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]

        
        for soldier in soldiers:
                names.append(soldier.name)
                if soldier.is_absent == True:
                        if soldier.is_at_punishment == False and soldier.is_in_mission == False and soldier.is_out == False:
                                if place == 'all':
                                        soldiers_list.append(soldier)
                                elif place == 's1':
                                        if soldier.current_army_unit in s1:
                                                soldiers_list.append(soldier)
                                elif place == 's2':
                                        if soldier.current_army_unit in s2:
                                                soldiers_list.append(soldier)
                                elif place == 's3':
                                        if soldier.current_army_unit in s3:
                                                soldiers_list.append(soldier)
                                elif place == 's': #kayadat el katiba
                                        if soldier.current_army_unit == "قيادة الكتيبة":
                                                soldiers_list.append(soldier)

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldiers_list,"soldiers_punishments": soldiers_punishments,"names":names,},)    

def out_list (request):
        place = request.GET.get('place')
        soldiers = Soldier.objects.all()
        soldiers_punishments = SoldierPunishments.objects.all()
        soldiers_list = []
        names=[]
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]

        
        for soldier in soldiers:
                names.append(soldier.name)
                if soldier.is_out == True:
                        if place == 'all':
                                soldiers_list.append(soldier)
                        elif place == 's1':
                                if soldier.current_army_unit in s1:
                                        soldiers_list.append(soldier)
                        elif place == 's2':
                                if soldier.current_army_unit in s2:
                                        soldiers_list.append(soldier)
                        elif place == 's3':
                                if soldier.current_army_unit in s3:
                                        soldiers_list.append(soldier)
                        elif place == 's': #kayadat el katiba
                                if soldier.current_army_unit == "قيادة الكتيبة":
                                        soldiers_list.append(soldier)

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldiers_list,"soldiers_punishments": soldiers_punishments,"names":names,},)       

def vacation_list (request):
        place = request.GET.get('place')
        soldiers = Soldier.objects.all()
        soldiers_punishments = SoldierPunishments.objects.all()
        soldiers_list = []
        names=[]
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]

        
        for soldier in soldiers:
                names.append(soldier.name)
                if soldier.is_at_vacation == True:
                        if place == 'all':
                                soldiers_list.append(soldier)
                        elif place == 's1':
                                if soldier.current_army_unit in s1:
                                        soldiers_list.append(soldier)
                        elif place == 's2':
                                if soldier.current_army_unit in s2:
                                        soldiers_list.append(soldier)
                        elif place == 's3':
                                if soldier.current_army_unit in s3:
                                        soldiers_list.append(soldier)
                        elif place == 's': #kayadat el katiba
                                if soldier.current_army_unit == "قيادة الكتيبة":
                                        soldiers_list.append(soldier)

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldiers_list,"soldiers_punishments": soldiers_punishments,"names":names,},)       

def vacation_sick_list (request):
        place = request.GET.get('place')
        soldiers = Soldier.objects.all()
        soldiers_punishments = SoldierPunishments.objects.all()
        soldiers_list = []
        names=[]
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]

        
        for soldier in soldiers:
                names.append(soldier.name)
                if soldier.is_at_vacation_sick == True:
                        if place == 'all':
                                soldiers_list.append(soldier)
                        elif place == 's1':
                                if soldier.current_army_unit in s1:
                                        soldiers_list.append(soldier)
                        elif place == 's2':
                                if soldier.current_army_unit in s2:
                                        soldiers_list.append(soldier)
                        elif place == 's3':
                                if soldier.current_army_unit in s3:
                                        soldiers_list.append(soldier)
                        elif place == 's': #kayadat el katiba
                                if soldier.current_army_unit == "قيادة الكتيبة":
                                        soldiers_list.append(soldier)

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldiers_list,"soldiers_punishments": soldiers_punishments,"names":names,},)       

def mission_list (request):
        place = request.GET.get('place')
        soldiers = Soldier.objects.all()
        soldiers_punishments = SoldierPunishments.objects.all()
        soldiers_list = []
        names=[]
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]

        
        for soldier in soldiers:
                names.append(soldier.name)
                if soldier.is_in_mission == True:
                        if place == 'all':
                                soldiers_list.append(soldier)
                        elif place == 's1':
                                if soldier.current_army_unit in s1:
                                        soldiers_list.append(soldier)
                        elif place == 's2':
                                if soldier.current_army_unit in s2:
                                        soldiers_list.append(soldier)
                        elif place == 's3':
                                if soldier.current_army_unit in s3:
                                        soldiers_list.append(soldier)
                        elif place == 's': #kayadat el katiba
                                if soldier.current_army_unit == "قيادة الكتيبة":
                                        soldiers_list.append(soldier)

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldiers_list,"soldiers_punishments": soldiers_punishments,"names":names,},)       

def prison_list (request):
        place = request.GET.get('place')
        soldiers = Soldier.objects.all()
        soldiers_punishments = SoldierPunishments.objects.all()
        soldiers_list = []
        names=[]
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]

        
        for soldier in soldiers:
                names.append(soldier.name)
                if soldier.is_at_punishment == True and soldier.current_punishment.punishment == "حبس":
                        if place == 'all':
                                soldiers_list.append(soldier)
                        elif place == 's1':
                                if soldier.current_army_unit in s1:
                                        soldiers_list.append(soldier)
                        elif place == 's2':
                                if soldier.current_army_unit in s2:
                                        soldiers_list.append(soldier)
                        elif place == 's3':
                                if soldier.current_army_unit in s3:
                                        soldiers_list.append(soldier)
                        elif place == 's': #kayadat el katiba
                                if soldier.current_army_unit == "قيادة الكتيبة":
                                        soldiers_list.append(soldier)

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldiers_list,"soldiers_punishments": soldiers_punishments,"names":names,},)   

        
def soldier_list(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        names=[]
        dof3at=[]
        soldier_num=[]
        i=1
        for soldier in soldier_list:

                # soldier.point = str(soldier.remarks).split('-')[-1].split('بتاريخ')[0].replace(" ","")
                # soldier.save()
                names.append(soldier.name)
                return_date = soldier.return_date
                present = soldier.is_present
                soldier_num.append(i)
                i+=1

                

                if soldier.is_at_vacation == False and present == True and soldier.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation = False)
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=False)
                                        elif present == False:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=True)
                
                if soldier. is_at_punishment == False :
                        pass
                else:

                        for punishment in soldiers_punishments:
                                if punishment.soldier.soldier_id == soldier.soldier_id:
                                        if today < punishment.end_date :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=punishment)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=True)
                                        elif today > punishment.end_date:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update( is_at_punishment=False)
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(current_punishment=None)


        for soldier in soldier_list:
                if soldier.service_end_date in dof3at:
                        pass
                else:
                        dof3at.append(soldier.service_end_date)
        dof3at.sort()
        
        paginator = Paginator(soldier_list,1500)
        page = request.GET.get('page')
        
        soldier_list = paginator.get_page(page)
        return render(request, "armydbapp/soldier_list.html",{"soldier_list":soldier_list,"soldiers_punishments": soldiers_punishments,"dof3at": dof3at, "names": names,},)
                
def soldier_search(request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)


        if request.method == "POST":
                query = request.POST.get('q')
                soldier_list_filtered = []
                soldier_list1 = Soldier.objects.filter(name__istartswith=query)
                soldier_list1 = soldier_list1.order_by("name")
                soldier_list2 = Soldier.objects.filter(name__icontains=query)
                soldier_list2 = soldier_list2.order_by("name")
                for soldier in soldier_list1:
                        soldier_list_filtered.append(soldier)
                for soldier in soldier_list2:
                        if soldier in soldier_list:
                                pass
                        else:
                                soldier_list_filtered.append(soldier)

                soldiers_punishments = SoldierPunishments.objects.all()
 

       
        
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def add_soldier(request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_soldier.html",{"names":names,},)

def submit_soldier(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                soldier_name = request.POST.get('soldier-name')
                soldier_img = request.FILES.get('soldier-img')
                soldier_id = request.POST.get('soldier-id')
                soldier_army_unit_name = request.POST.get('soldier-army-unit-name')
                soldier_army_unit_number = request.POST.get('soldier-army-unit-number')
                soldier_current_army_unit = soldier_army_unit_number + " " + soldier_army_unit_name
                soldier_service_start_date = request.POST.get('soldier-service-start-date')
                soldier_service_end_date = request.POST.get('soldier-service-end-date')
                soldier_speciality= request.POST.get('soldier-speciality')
                soldier_adress= request.POST.get('soldier-adress')
                soldier_cultural_level= request.POST.get('cultural-level')
                soldier_educational_degree= request.POST.get('educational-degree')
                soldier_a5eir_sarfaya = request.POST.get('a5eir-sarfaya')
                id_tag= "S"+ str(soldier_id)
                new_soldier = Soldier(  name=soldier_name,
                                        soldier_img=soldier_img, 
                                        soldier_id=soldier_id, 
                                        service_start_date=soldier_service_start_date, 
                                        service_end_date=soldier_service_end_date,
                                        current_army_unit=soldier_current_army_unit,
                                        speciality =soldier_speciality,
                                        adress = soldier_adress,
                                        cultural_level = soldier_cultural_level,
                                        educational_degree =soldier_educational_degree,
                                        a5eir_sarfaya = soldier_a5eir_sarfaya,
                                        id_tag= id_tag,
                                        )
                
                new_soldier.save()

                soldier_unit = SoldierArmyUnits(soldier = new_soldier, 
                                                army_unit = soldier_current_army_unit, 
                                                start_date = today, 
                                                )

                soldier_unit.save()
                return redirect("armydbapp:add_soldier")

def add_img(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_img.html",{"soldier_id":soldier_id,"names":names,},)

def submit_add_img(request):
        if request.method == "POST":
                soldier_img = request.FILES.get('soldier-img')
                soldier_number = request.POST.get('soldier_number')
                soldier =  Soldier.objects.filter(soldier_id=soldier_number).get()
                soldier.soldier_img=soldier_img
                soldier.save()
                return redirect("armydbapp:soldier_list")

def add_reward(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_reward.html",{"soldier_id":soldier_id,"names":names,},)

def submit_reward(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                rewarded_soldier = get_object_or_404(Soldier, soldier_id=soldier_number)
                days_rewarded = request.POST.get('days_rewarded')
                Soldier.objects.filter(soldier_id=soldier_number).update(reward_days=days_rewarded)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_rewarded=True)

                new_reward = Rewards (soldier = rewarded_soldier, reward_days = days_rewarded)
                
                new_reward.save()

                return redirect("armydbapp:soldier_list")

def mawkaf_a5eir_sarfaya(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/mawkaf_a5eir_sarfaya.html",{"soldier_id":soldier_id,"names":names,},)

def submit_mawkaf_a5eir_sarfaya(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                soldier_a5eir_sarfaya = request.POST.get('a5eir-sarfaya')
                Soldier.objects.filter(soldier_id=soldier_number).update(a5eir_sarfaya=soldier_a5eir_sarfaya)
                return redirect("armydbapp:soldier_list")

def add_zucchini(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_zucchini.html",{"soldier_id":soldier_id,"names":names,},)

def submit_zucchini(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                soldier = get_object_or_404(Soldier, soldier_id=soldier_number)
                zucchini = request.POST.get('zucchini')
                soldier.zucchini = zucchini
                soldier.save()

                return redirect("armydbapp:soldier_list")

def add_work_assigned(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_work_assigned.html",{"soldier_id":soldier_id,"names":names,},)

def submit_work_assigned(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                soldier = get_object_or_404(Soldier, soldier_id=soldier_number)
                work_assigned = request.POST.get('work_assigned')
                soldier.work_assigned = work_assigned
                soldier.save()

                return redirect("armydbapp:soldier_list")

def add_job(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_job.html",{"soldier_id":soldier_id,"names":names,},)

def submit_job(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                soldier = get_object_or_404(Soldier, soldier_id=soldier_number)
                job = request.POST.get('job')
                soldier.job = job
                soldier.save()

                return redirect("armydbapp:soldier_list")

def add_remark(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        
        soldier = get_object_or_404(Soldier, soldier_id=soldier_id)
        remarks = soldier.remarks

        return render(request, "armydbapp/add_remarks.html",{"soldier_id":soldier_id,"names":names,"remarks":remarks,},)

def submit_remark(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                soldier = get_object_or_404(Soldier, soldier_id=soldier_number)
                remarks = request.POST.get('remarks')
                soldier.point   = request.POST.get('remarks')
                old_remarks = soldier.remarks
                if old_remarks == None:
                       new_remarks = remarks
                else:
                        new_remarks = str(old_remarks) + " \n "  + str(remarks)
                soldier.remarks = new_remarks
                soldier.point   = remarks.split('بتاريخ')[0].replace(" ","").replace("-","")
                soldier.save()
                
        return redirect("armydbapp:soldier_list")
        

def add_vacation(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_vacation.html",{"soldier_id":soldier_id,"names":names,},)



def submit_vacation(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                date_of_return = request.POST.get('date_of_return')
                Soldier.objects.filter(soldier_id=soldier_number).update(return_date=date_of_return)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_at_vacation=True)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_present=False)
                soldier = Soldier.objects.filter(soldier_id=soldier_number).get()
                vacation = Vacations(soldier=soldier,start_date=today,end_date=date_of_return)
                vacation.save()
                             
                return_date = soldier.return_date
                present = soldier.is_present
                               
                if soldier.is_at_vacation == False and present == True and soldier.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation = False)
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=False)
                                        elif present == False:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=True)
                
                return redirect("armydbapp:soldier_list")

def add_vacation_sick(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_vacation_sick.html",{"soldier_id":soldier_id,"names":names,},)

def submit_vacation_sick(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                date_of_return = request.POST.get('date_of_return')
                Soldier.objects.filter(soldier_id=soldier_number).update(return_date=date_of_return)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_at_vacation_sick=True)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_at_vacation=True)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_present=False)

                soldier =  Soldier.objects.filter(soldier_id=soldier_number).get()
                
                return_date = soldier.return_date
                present = soldier.is_present
                               
                if soldier.is_at_vacation == False and present == True and soldier.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation = False)
                                        Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=False)
                                        elif present == False:
                                                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_absent=True)
                return redirect("armydbapp:soldier_list")

def add_punishment(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_punishment.html",{"soldier_id":soldier_id,"names":names,},)

def submit_punishment(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                punished_soldier = get_object_or_404(Soldier, soldier_id=soldier_number)
                type_of_punishment = request.POST.get('punishment_type')
                start_date_punishment = request.POST.get('punishment_start_date')
                end_date_punishment = request.POST.get('punishment_end_date')

                soldier_punishment = SoldierPunishments(soldier=punished_soldier, 
                                                        punishment=type_of_punishment, 
                                                        start_date=start_date_punishment, 
                                                        end_date=end_date_punishment)
                
                soldier_punishment.save()
                Soldier.objects.filter(soldier_id=soldier_number).update(current_punishment = soldier_punishment)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_at_punishment=True)
                return redirect("armydbapp:soldier_list")

def soldier_information(request):
        soldier_id = request.GET.get('soldier_id')
        
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        
        for soldier in soldier_list:
                names.append(soldier.name)
        
        soldier = Soldier.objects.filter(soldier_id=soldier_id).get()
        info={"soldier":soldier,"names":names,}
        punishement_list = SoldierPunishments.objects.filter(soldier = soldier)
        if punishement_list: 
                info.update({"punishement_list":punishement_list})
        
        units_list = SoldierArmyUnits.objects.filter(soldier = soldier)
        if units_list:
                info.update({"units_list":units_list})
        
        vacations = Vacations.objects.filter(soldier = soldier)
        if vacations:
                info.update({"vacations":vacations})
        
        rewards = Rewards.objects.filter(soldier = soldier)
        if rewards:
                info.update({"rewards":rewards})
        promotions = Promotion.objects.filter(soldier = soldier)
        if promotions:
                info.update({"promotions":promotions})
        
        
        return render(request, "armydbapp/soldier_information.html",info,)



def delete_soldier(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/delete_soldier.html",{"soldier_id":soldier_id,"names":names,},)

def submit_delete_soldier(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                Soldier.objects.filter(soldier_id=soldier_number).delete()
                return redirect("armydbapp:soldier_list")


def dont_delete_soldier(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")

def add_promotion(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_promotion.html",{"soldier_id":soldier_id,"names":names,},)

def submit_promotion(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                promoted_soldier = get_object_or_404(Soldier, soldier_id=soldier_number)
                soldier_rank = request.POST.get('rank')
                soldier_promotion = Promotion(soldier=promoted_soldier, 
                                                        soldier_rank=soldier_rank, 
                                                        promotion_date=today,)
                soldier_promotion.save()                                        
        return redirect("armydbapp:soldier_list")

def awaiting_trial(request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                
        return render(request, "armydbapp/awaiting_trial.html",{"soldier_id":soldier_id,"names":names,},)

def submit_awaiting_trial(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                reason = request.POST.get('reason-awaiting-trial')
                Soldier.objects.filter(soldier_id=soldier_number).update(is_awaiting_trial=True)
                Soldier.objects.filter(soldier_id=soldier_number).update(reason_awaiting_trial= reason)     
                return redirect("armydbapp:soldier_list")
                
def dont_awaiting_trial(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")


def trial_done (request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                
        return render(request, "armydbapp/trial_done.html",{"soldier_id":soldier_id,"names":names,},)


def submit_trial_done(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                Soldier.objects.filter(soldier_id=soldier_number).update(is_awaiting_trial=False)               
                return redirect("armydbapp:soldier_list")

def dont_trial_done(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")

def reward_consumed (request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        
        return render(request, "armydbapp/reward_consumed.html",{"soldier_id":soldier_id,"names":names,},)


def submit_reward_consumed(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                Soldier.objects.filter(soldier_id=soldier_number).update(is_rewarded=False)               
                return redirect("armydbapp:soldier_list")

def dont_reward_consumed(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")

def absent (request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/absent.html",{"soldier_id":soldier_id,"names":names,},)


def submit_absent(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                Soldier.objects.filter(soldier_id=soldier_number).update(is_absent=True)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_present=False)             
                return redirect("armydbapp:soldier_list")

def dont_absent(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")

def present (request):
        soldier_id = request.GET["soldier_id"]
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/present.html",{"soldier_number":soldier_id,"names":names,},)


def submit_present(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                Soldier.objects.filter(soldier_id=soldier_number).update(is_absent=False)    
                Soldier.objects.filter(soldier_id=soldier_number).update(is_present=True)  
                Soldier.objects.filter(soldier_id=soldier_number).update(is_at_vacation=False)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_at_vacation_sick=False)          
                return redirect("armydbapp:soldier_list")

def dont_present(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")

def outing (request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/outing.html",{"soldier_id":soldier_id,"names":names,},)

def submit_outing(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                type_of_outing = request.POST.get('type_of_outing')
                Soldier.objects.filter(soldier_id=soldier_number).update(outing_type=type_of_outing)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_out=True)
                return redirect("armydbapp:soldier_list")

def no_outing (request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/no_outing.html",{"soldier_id":soldier_id,"names":names,},)

def submit_no_outing(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                Soldier.objects.filter(soldier_id=soldier_number).update(outing_type=None)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_out=False)
                return redirect("armydbapp:soldier_list")

def dont_no_outing(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")    


def mission (request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/mission.html",{"soldier_id":soldier_id,"names":names,},)

def submit_mission(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                type_of_mission = request.POST.get('type_of_mission')
                Soldier.objects.filter(soldier_id=soldier_number).update(mission_type=type_of_mission)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_in_mission=True)
                Soldier.objects.filter(soldier_id=soldier.soldier_id).update(is_present=False)
                return redirect("armydbapp:soldier_list")

def no_mission (request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/no_mission.html",{"soldier_id":soldier_id,"names":names,},)

def submit_no_mission(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                Soldier.objects.filter(soldier_id=soldier_number).update(mission_type=None)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_in_mission=False)
                Soldier.objects.filter(soldier_id=soldier_number).update(is_present=True)
                return redirect("armydbapp:soldier_list")

def dont_no_mission(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")    

def change_army_unit (request):
        soldier_id = request.GET.get('soldier_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/change_army_unit.html",{"soldier_id":soldier_id,"names":names,},)

def submit_change_army_unit(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                soldier =  Soldier.objects.filter(soldier_id=soldier_number)
                soldier_army_unit_name = request.POST.get('soldier-army-unit-name')
                soldier_army_unit_number = request.POST.get('soldier-army-unit-number')
                soldier_current_army_unit = soldier_army_unit_number + " " + soldier_army_unit_name
                start_date_unit = today
                soldier_last_unit = Soldier.objects.get(soldier_id=soldier_number).current_army_unit
                
                last_unit =  SoldierArmyUnits.objects.filter(soldier= Soldier.objects.get(soldier_id=soldier_number), army_unit = soldier_last_unit)
                last_unit.update(end_date = today)
                
                

                soldier_unit = SoldierArmyUnits(soldier = Soldier.objects.get(soldier_id=soldier_number), 
                                                army_unit = soldier_current_army_unit, 
                                                start_date = start_date_unit, 
                                                )
                
                soldier.update(current_army_unit=soldier_current_army_unit)
                soldier_unit.save()

                return redirect("armydbapp:soldier_list")

def dont_change_army_unit(request):
        if request.method == "POST":
                return redirect("armydbapp:soldier_list")  

def numbering ():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        number_of_soldiers = 0 
        number_of_at_vacation = 0
        number_of_at_vacation_sick = 0
        number_prisioned = 0
        number_out = 0 
        number_absent = 0
        number_mission = 0
        number_here = 0
        number_punished = 0
        number_returning = 0
        number_late_vacation = 0
        number_late_unit = 0 
        specialities=[]
        soldiers = Soldier.objects.all()
        sub_officers = Sub_officer.objects.all()
        awaiting_trial = 0 
        for soldier in soldiers:
                number_of_soldiers = number_of_soldiers +1 
                if soldier.is_awaiting_trial == True:
                        awaiting_trial +=1 
                if soldier.is_at_vacation:
                        number_of_at_vacation += 1
                if soldier.is_at_vacation_sick:
                        number_of_at_vacation_sick += 1
                if soldier.is_at_punishment: 
                        number_punished += 1
                       
                        current_punishment = soldier.current_punishment
                        current_punishment = current_punishment.punishment
                        if current_punishment == "حبس":
                                number_prisioned += 1 
              
                if soldier.is_out:
                        number_out += 1
                if soldier.is_absent:
                        number_absent += 1
                if soldier.is_in_mission:
                        number_mission += 1
                if soldier.return_date == today:
                        number_returning += 1
                if soldier.return_date != None:
                        if daysBetweenDates(soldier.return_date.year, soldier.return_date.month, soldier.return_date.day, today.year, today.month, today.day) >= 31: 
                                number_late_vacation +=1

                if soldier.current_army_unit == "قيادة الكتيبة":
                        pass
                else:
                      
                    try:
                                                                
                        last_unit = SoldierArmyUnits.objects.get(soldier= soldier , army_unit = soldier.current_army_unit)
                        if last_unit.start_date != None:
                            if daysBetweenDates(last_unit.start_date.year, last_unit.start_date.month, last_unit.start_date.day, today.year, today.month, today.day) >= 90: 
                                    number_late_unit +=1
                    
                    except:
                        pass
                
                if soldier.speciality:
                        if soldier.speciality not in specialities:
                                specialities.append(soldier.speciality)

        for sub_officer in sub_officers : 
                        if sub_officer.speciality not in specialities:
                                specialities.append(sub_officer.speciality)

        number_of_specialities = [0] * len(specialities)
        number_of_specialities_sub_officer = [0] * len(specialities)
        
        for soldier in soldiers:
                for speciality in specialities:

                        if soldier.speciality == speciality:
                                number_of_specialities[specialities.index(speciality)] += 1 
        
        for sub_officer in sub_officers:
                for speciality in specialities:

                        if sub_officer.speciality == speciality:
                                number_of_specialities_sub_officer[specialities.index(speciality)] += 1 

        sum_number_of_specialities = str(sum(number_of_specialities))
        sum_number_of_specialities_sub_officer = str(sum(number_of_specialities_sub_officer))
        
        j=0
        for i in number_of_specialities:
                number_of_specialities[j]= str(i)
                j += 1 
        j=0
        for i in number_of_specialities_sub_officer:
                number_of_specialities_sub_officer[j]= str(i)
                j += 1 
        
        number_here = number_of_soldiers - (number_of_at_vacation + number_prisioned + number_out + number_absent + number_mission) 
        
        return  sum_number_of_specialities_sub_officer,number_of_specialities_sub_officer,str(awaiting_trial),sum_number_of_specialities , number_of_specialities, specialities, str(number_of_at_vacation_sick), str(number_late_unit) , str(number_late_vacation), str(number_punished), str(number_of_soldiers), str(number_of_at_vacation), str(number_prisioned), str(number_out), str(number_absent), str(number_mission), str(number_here), str(number_returning)

def dof3at_radif():
        specialities=[]
        soldiers = Soldier.objects.all()
        dof3at = []
        dof3a_total = []
        specialities_total = []

        for soldier in soldiers:
                if soldier.speciality:
                        if soldier.speciality not in specialities:
                                specialities.append(soldier.speciality)

                if soldier.service_end_date not in dof3at:
                        dof3at.append(soldier.service_end_date)

        
        dof3at.sort() 
        

        total_speciality = [0] * len(specialities)
        dof3a_number_of_specialities = [0] * len(dof3at)

        for i in range(0,len(dof3at)):
                dof3a_number_of_specialities[i] = [0] * len(specialities)
        
        for soldier in soldiers:
                for speciality in specialities:
                        if soldier.speciality == speciality:
                                dof3a_number_of_specialities[dof3at.index(soldier.service_end_date)][specialities.index(speciality)] += 1

        
        for i in range(0,(len(dof3at))):
                for j in range (0,(len(specialities))):
                        x = dof3a_number_of_specialities[i][j]
                        x = str(x)
                        dof3a_number_of_specialities[i][j]= x
                        
        dof3a_total = [0] * len(dof3at)

        for dof3a in dof3at:
                for soldier in soldiers:
                        if soldier.service_end_date == dof3a:
                                dof3a_total[dof3at.index(soldier.service_end_date)] += 1

        for sp in specialities: 
                for soldier in soldiers: 
                        if soldier.speciality == sp : 
                                total_speciality[specialities.index(soldier.speciality)] += 1
                                
        
        j=0 
        for i in dof3at:
                dof3at[j] = str(i.year) + "/" + str(i.month) + "/" + str(i.day)
                j+=1 


                            
        return dof3at, specialities, dof3a_number_of_specialities, dof3a_total,total_speciality


def reward_list(request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/reward_list.html",{"soldier_list":soldier_list,"soldiers_punishments": soldiers_punishments,"names":names,},)

def punished_list(request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/punished_list.html",{"soldier_list":soldier_list,"soldiers_punishments": soldiers_punishments,"names":names,},)


daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year): #funtion returns true if the year is a leap year, false if the year is a common year 
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 !=0:
        return False 
    else:
        return True 

def daysOfMonth(month):
    return daysOfMonths[month-1]

def isDateBefore(y1, m1, d1, y2, m2, d2):
    if y1 < y2 :
        return True
    elif y1 == y2:
        if m1 < m2 :
            return True
        elif m1 == m2:
            return d1 < d2
    else:
        return False

def dayAfter (y, m, d):
    if isLeapYear(y):
        daysOfMonths[1]=29
    else:
        daysOfMonths[1]=28
        
    if d < daysOfMonth(m):
        return y,m,d+1
    if m < 12:
        return y, m+1 ,1
    else:
        return y+1 ,1,1
        

    
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    if isDateBefore(y1, m1, d1, y2, m2, d2) == False:
            return 0 
    days = 0
    while isDateBefore(y1, m1, d1, y2, m2, d2):
        y1,m1,d1=dayAfter(y1,m1,d1)
        days +=1 
    return days

def late_vacation_list(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]

                
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.return_date != None:
                        if daysBetweenDates(soldier.return_date.year, soldier.return_date.month, soldier.return_date.day, today.year, today.month, today.day) >= 31: 
                                soldier_list_filtered.append(soldier)

       
        return render(request, "armydbapp/late_vacation_list.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)


def return_today_list(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.return_date == today:
                        soldier_list_filtered.append(soldier)

       
        return render(request, "armydbapp/return_today_list.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def late_unit_list(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.current_army_unit == "قيادة الكتيبة":
                        pass
                else:
                    try:
                        last_unit =  SoldierArmyUnits.objects.get(soldier= soldier , army_unit = soldier.current_army_unit)
                        if last_unit.start_date != None:
                                if daysBetweenDates(last_unit.start_date.year, last_unit.start_date.month, last_unit.start_date.day, today.year, today.month, today.day) >= 90: 
                                        soldier_list_filtered.append(soldier)
                    except:
                        pass

       
        return render(request, "armydbapp/late_unit_list.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def absent_list(request):      
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.is_absent == True:
                        soldier_list_filtered.append(soldier)
                        return_date = soldier.return_date 
                        days_absent = daysBetweenDates(return_date.year, return_date.month, return_date.day, today.year, today.month, today.day)
                        days_absent = str(days_absent)
                        Soldier.objects.filter(soldier_id = soldier.soldier_id).update(days_absent = days_absent)

       

       

        return render(request, "armydbapp/absent_list.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def awaiting_trial_list(request):      
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.is_awaiting_trial == True:
                        soldier_list_filtered.append(soldier)

       

        return render(request, "armydbapp/awaiting_trial_list.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def vacation_choice(request):
        if request.method == "POST":
                soldier_number = request.POST.get('soldier_number')
                soldier = Soldier.objects.get(soldier_id=soldier_number)
                value = request.POST.get(soldier.id_tag)
                soldier.vacation_choice= value
                soldier.save()  
                        
        return redirect("armydbapp:soldier_list") 


def katiba_headquart(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.current_army_unit == "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)

       

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def s1_headquart(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.current_army_unit == "قيادة السرية الأولي":
                        soldier_list_filtered.append(soldier)

       
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _قياس1(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "قياس1" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _13احمد(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "13احمد" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _11رياض(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "11رياض" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _11محمود(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "11محمود" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)

       

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _12رياض(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "12رياض" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _12محمود(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "12محمود" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _13رياض(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "13رياض" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _13محمود(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "13محمود" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _14رياض(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "14رياض" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _14محمود(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "14محمود" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _15رياض(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "15رياض" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _15محمود(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "15محمود" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _1سعيد(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "1سعيد" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _1عرب(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "1عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _2سعيد(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "2سعيد" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _2عرب(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "2عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)





def _قياس2(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "قياس2" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _3عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "3عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _4سعيد(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "4سعيد" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _4عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "4عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _5عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "5عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _6عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "6عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _7عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "7عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _8عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "8عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _9سعيد(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "9سعيد" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _9عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "9عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)





def _قياس3(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "قياس3" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _11عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "11عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _12سعيد(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "12سعيد" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _13سعيد(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "13سعيد" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def _13عرب(request):  
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.point == "13عرب" and soldier.current_army_unit != "قيادة الكتيبة":
                        soldier_list_filtered.append(soldier)
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)


def dof3a_radif(request):
        if request.method == "POST":
                dof3a = request.POST.get('dof3a')
                dof3a = datetime.datetime.strptime(dof3a, "%Y-%m-%d")
                soldier_list = Soldier.objects.all()
                soldier_list = soldier_list.order_by("name")
                soldiers_punishments = SoldierPunishments.objects.all()
                soldier_list_filtered = []
                names=[]
                for soldier in soldier_list:
                        names.append(soldier.name)
                        if soldier.service_end_date.year == dof3a.year:
                                if soldier.service_end_date.month == dof3a.month:
                                        soldier_list_filtered.append(soldier)
                                                
        
        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def numbering_k10_head ():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        number_of_soldiers_k10_head = 0 
        number_of_at_vacation_k10_head = 0
        number_of_at_vacation_sick_k10_head = 0
        number_prisioned_k10_head = 0
        number_out_k10_head = 0 
        number_absent_k10_head = 0
        number_mission_k10_head = 0
        number_here_k10_head = 0
        number_punished_k10_head = 0
        number_returning_k10_head = 0
        number_late_vacation_k10_head = 0
        number_late_unit_k10_head = 0 
        soldiers = Soldier.objects.all()
        
        for soldier in soldiers:
                if soldier.current_army_unit == "قيادة الكتيبة":
                        number_of_soldiers_k10_head += 1 
                        if soldier.is_at_vacation:
                                number_of_at_vacation_k10_head += 1
                        if soldier.is_at_vacation_sick:
                                number_of_at_vacation_sick_k10_head += 1
                        if soldier.is_at_punishment: 
                                number_punished_k10_head +=1

                                current_punishment = soldier.current_punishment
                                current_punishment = current_punishment.punishment
                                if current_punishment == "حبس":
                                        number_prisioned_k10_head += 1 
                        if soldier.is_out:
                                number_out_k10_head += 1
                        if soldier.is_absent:
                                number_absent_k10_head += 1
                        if soldier.is_in_mission:
                                number_mission_k10_head += 1
                        

        number_here_k10_head = number_of_soldiers_k10_head - (number_of_at_vacation_k10_head + number_prisioned_k10_head + number_out_k10_head + number_absent_k10_head + number_mission_k10_head) 
        
        return str(number_of_at_vacation_sick_k10_head), str(number_of_soldiers_k10_head), str(number_of_at_vacation_k10_head), str(number_prisioned_k10_head), str(number_out_k10_head), str(number_absent_k10_head), str(number_mission_k10_head), str(number_here_k10_head)


def numbering_s1_head ():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        number_of_soldiers_s1_head = 0 
        number_of_at_vacation_s1_head = 0
        number_of_at_vacation_sick_s1_head = 0
        number_prisioned_s1_head = 0
        number_out_s1_head = 0 
        number_absent_s1_head = 0
        number_mission_s1_head = 0
        number_here_s1_head = 0
        number_punished_s1_head = 0
        number_returning_s1_head = 0
        number_late_vacation_s1_head = 0
        number_late_unit_s1_head = 0 
        soldiers = Soldier.objects.all()
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        for soldier in soldiers:
                if soldier.current_army_unit in s1:
                        number_of_soldiers_s1_head += 1 
                        if soldier.is_at_vacation:
                                number_of_at_vacation_s1_head += 1
                        if soldier.is_at_vacation_sick:
                                number_of_at_vacation_sick_s1_head += 1
                        if soldier.is_at_punishment: 
                                number_punished_s1_head +=1
                                current_punishment = soldier.current_punishment
                                current_punishment = current_punishment.punishment
                                if current_punishment == "حبس":
                                        number_prisioned_s1_head += 1 
                        if soldier.is_out:
                                number_out_s1_head += 1
                        if soldier.is_absent:
                                number_absent_s1_head += 1
                        if soldier.is_in_mission:
                                number_mission_s1_head += 1
                        

        number_here_s1_head = number_of_soldiers_s1_head - (number_of_at_vacation_s1_head + number_prisioned_s1_head + number_out_s1_head + number_absent_s1_head + number_mission_s1_head) 
        
        return str(number_of_at_vacation_sick_s1_head), str(number_of_soldiers_s1_head), str(number_of_at_vacation_s1_head), str(number_prisioned_s1_head), str(number_out_s1_head), str(number_absent_s1_head), str(number_mission_s1_head), str(number_here_s1_head)

def numbering_s2_head ():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        number_of_soldiers_s2_head = 0 
        number_of_at_vacation_s2_head = 0
        number_of_at_vacation_sick_s2_head = 0
        number_prisioned_s2_head = 0
        number_out_s2_head = 0 
        number_absent_s2_head = 0
        number_mission_s2_head = 0
        number_here_s2_head = 0
        number_punished_s2_head = 0
        number_returning_s2_head = 0
        number_late_vacation_s2_head = 0
        number_late_unit_s2_head = 0 
        soldiers = Soldier.objects.all()
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        for soldier in soldiers:
                if soldier.current_army_unit in s2:
                        number_of_soldiers_s2_head += 1 
                        if soldier.is_at_vacation:
                                number_of_at_vacation_s2_head += 1
                        if soldier.is_at_vacation_sick:
                                number_of_at_vacation_sick_s2_head += 1
                        if soldier.is_at_punishment: 
                                try:
                                        number_punished_s2_head +=1
                                        current_punishment = soldier.current_punishment
                                        current_punishment = current_punishment.punishment
                                        if current_punishment == "حبس":
                                                number_prisioned_s2_head += 1 
                                except:
                                        pass #bug
                        if soldier.is_out:
                                number_out_s2_head += 1
                        if soldier.is_absent:
                                number_absent_s2_head += 1
                        if soldier.is_in_mission:
                                number_mission_s2_head += 1
                        

        number_here_s2_head = number_of_soldiers_s2_head - (number_of_at_vacation_s2_head + number_prisioned_s2_head + number_out_s2_head + number_absent_s2_head + number_mission_s2_head) 
        
        return str(number_of_at_vacation_sick_s2_head), str(number_of_soldiers_s2_head), str(number_of_at_vacation_s2_head), str(number_prisioned_s2_head), str(number_out_s2_head), str(number_absent_s2_head), str(number_mission_s2_head), str(number_here_s2_head)

def numbering_s3_head ():
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        number_of_soldiers_s3_head = 0 
        number_of_at_vacation_s3_head = 0
        number_of_at_vacation_sick_s3_head = 0
        number_prisioned_s3_head = 0
        number_out_s3_head = 0 
        number_absent_s3_head = 0
        number_mission_s3_head = 0
        number_here_s3_head = 0
        number_punished_s3_head = 0
        number_returning_s3_head = 0
        number_late_vacation_s3_head = 0
        number_late_unit_s3_head = 0 
        soldiers = Soldier.objects.all()
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]
        for soldier in soldiers:
                if soldier.current_army_unit in s3:
                        number_of_soldiers_s3_head += 1 
                        if soldier.is_at_vacation:
                                number_of_at_vacation_s3_head += 1
                        if soldier.is_at_vacation_sick:
                                number_of_at_vacation_sick_s3_head += 1
                        if soldier.is_at_punishment: 
                                number_punished_s3_head +=1
                                current_punishment = soldier.current_punishment
                                current_punishment = current_punishment.punishment
                                if current_punishment == "حبس":
                                        number_prisioned_s3_head += 1 
                        if soldier.is_out:
                                number_out_s3_head += 1
                        if soldier.is_absent:
                                number_absent_s3_head += 1
                        if soldier.is_in_mission:
                                number_mission_s3_head += 1
                        

        number_here_s3_head = number_of_soldiers_s3_head - (number_of_at_vacation_s3_head + number_prisioned_s3_head + number_out_s3_head + number_absent_s3_head + number_mission_s3_head) 
        
        return str(number_of_at_vacation_sick_s3_head), str(number_of_soldiers_s3_head), str(number_of_at_vacation_s3_head), str(number_prisioned_s3_head), str(number_out_s3_head), str(number_absent_s3_head), str(number_mission_s3_head), str(number_here_s3_head)



def gen_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    return FileResponse(buffer, as_attachment=True, filename='قاعدة البيانات.pdf')

def s1_all(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        s1 = ["قيادة السرية الأولي","1 تاجر","2 تاجر","3 تاجر","4 تاجر","5 تاجر","6 تاجر","7 تاجر","8 تاجر","1 أحمد","2 أحمد","3 أحمد","4 أحمد","5 أحمد","6 أحمد","7 أحمد","8 أحمد","4 نحاس",]
        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.current_army_unit in s1 :
                        soldier_list_filtered.append(soldier)

       

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def s2_all(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        s2 = ["قيادة السرية الثانية","9 تاجر","10 تاجر","11 تاجر","12 تاجر","11 أحمد","12 أحمد","10 أحمد","9 أحمد","1 بديع","2 بديع","3 بديع", "4 بديع", "1 هشام","2 هشام","3 هشام", "4 هشام",]
        for soldier in soldier_list:
                names.append(soldier.name)
        for i in s2:
                for soldier in soldier_list:
                        if soldier.current_army_unit == i:
                                soldier_list_filtered.append(soldier)

       

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)

def s3_all(request):
               
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        soldiers_punishments = SoldierPunishments.objects.all()
        soldier_list_filtered = []
        names=[]
        s3 = ["قيادة السرية الثالثة","5 بديع","6 بديع","7 بديع","8 بديع","9 بديع","10 بديع","11 بديع","12 بديع","5 هشام","6 هشام","7 هشام","8 هشام","9 هشام","10 هشام","11 هشام","12 هشام",]
        for soldier in soldier_list:
                names.append(soldier.name)
                
        for i in s3:
                for soldier in soldier_list:
                        if soldier.current_army_unit == i:
                                soldier_list_filtered.append(soldier)

       

        return render(request, "armydbapp/soldier_list_filter.html",{"soldier_list_filtered":soldier_list_filtered,"soldiers_punishments": soldiers_punishments,"names":names,},)


#officers_views
def add_officer(request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_officer.html",{"names":names,},)

def submit_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                officer_name = request.POST.get('officer-name')
                officer_rank = request.POST.get('officer-rank')
                officer_img = request.FILES.get('officer-img')
                officer_id = request.POST.get('officer-id')
                officer_exp_number= request.POST.get('officer-exp-number')
                officer_mobile_number= request.POST.get('officer-mobile-number')
                officer_adress= request.POST.get('officer-adress')
                officer_speciality= request.POST.get('officer-speciality')
                officer_army_unit_name = request.POST.get('officer-army-unit-name')
                officer_current_army_unit = officer_army_unit_name
                officer_service_start_date = request.POST.get('officer-service-start-date')
                id_tag= "S"+ str(officer_id)
                new_officer = Officer(  name=officer_name,
                                        rank= officer_rank,
                                        officer_img=officer_img, 
                                        officer_id=officer_id, 
                                        exp_number = officer_exp_number,
                                        mobile_number = officer_mobile_number,
                                        service_start_date=officer_service_start_date, 
                                        current_army_unit=officer_current_army_unit,
                                        speciality =officer_speciality,
                                        adress = officer_adress,
                                        id_tag= id_tag,
                                        )
                
                new_officer.save()

                officer_unit = OfficerArmyUnits(officer = new_officer, 
                                                army_unit = officer_current_army_unit, 
                                                start_date = today, 
                                                )

                officer_unit.save()
                return redirect("armydbapp:add_officer")

def add_img_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_img_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_add_img_officer(request):
        if request.method == "POST":
                officer_img = request.FILES.get('officer-img')
                officer_number = request.POST.get('officer_number')
                officer =  Officer.objects.filter(officer_id=officer_number).get()
                officer.officer_img= officer_img
                officer.save()
                return redirect("armydbapp:officer_list")

def add_reward_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_reward_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_reward_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                rewarded_officer = get_object_or_404(Officer, officer_id=officer_number)
                days_rewarded = request.POST.get('days_rewarded')
                Officer.objects.filter(officer_id=officer_number).update(reward_days=days_rewarded)
                Officer.objects.filter(officer_id=officer_number).update(is_rewarded=True)

                new_reward = Officer_Rewards (officer = rewarded_officer, reward_days = days_rewarded)
                
                new_reward.save()

                return redirect("armydbapp:officer_list")


def add_work_assigned_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_work_assigned_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_work_assigned_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                officer = get_object_or_404(Officer, officer_id=officer_number)
                work_assigned = request.POST.get('work_assigned')
                officer.work_assigned = work_assigned
                officer.save()

                return redirect("armydbapp:officer_list")


def add_remark_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        
        officer = get_object_or_404(Officer, officer_id=officer_id)
        remarks = officer.remarks

        return render(request, "armydbapp/add_remarks.html",{"officer_id":officer_id,"names":names,"remarks":remarks,},)

def submit_remark_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                officer = get_object_or_404(Officer, officer_id=officer_number)
                remarks = request.POST.get('remarks')
                old_remarks = officer.remarks
                if old_remarks == None:
                       new_remarks = remarks
                else:
                        new_remarks = str(old_remarks) + " \n "  + str(remarks)
                officer.remarks = new_remarks
                officer.save()
                
        return redirect("armydbapp:officer_list")
        

def add_vacation_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_vacation_officer.html",{"officer_id":officer_id,"names":names,},)



def submit_vacation_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                date_of_return = request.POST.get('date_of_return')
                Officer.objects.filter(officer_id=officer_number).update(return_date=date_of_return)
                Officer.objects.filter(officer_id=officer_number).update(is_at_vacation=True)
                Officer.objects.filter(officer_id=officer_number).update(is_present=False)
                officer = Officer.objects.filter(officer_id=officer_number).get()
                vacation = OfficerVacations(officer=officer,start_date=today,end_date=date_of_return)
                vacation.save()
                             
                return_date = officer.return_date
                present = officer.is_present
                               
                if officer.is_at_vacation == False and present == True and officer.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Officer.objects.filter(officer_id=officer.officer_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Officer.objects.filter(officer_id=officer.officer_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Officer.objects.filter(officer_id=officer.officer_id).update(is_at_vacation = False)
                                        Officer.objects.filter(officer_id=officer.officer_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Officer.objects.filter(officer_id=officer.officer_id).update(is_absent=False)
                                        elif present == False:
                                                Officer.objects.filter(officer_id=officer.officer_id).update(is_absent=True)
                
                return redirect("armydbapp:officer_list")

def add_vacation_sick_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_vacation_sick_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_vacation_sick_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                date_of_return = request.POST.get('date_of_return')
                Officer.objects.filter(officer_id=officer_number).update(return_date=date_of_return)
                Officer.objects.filter(officer_id=officer_number).update(is_at_vacation_sick=True)
                Officer.objects.filter(officer_id=officer_number).update(is_at_vacation=True)
                Officer.objects.filter(officer_id=officer_number).update(is_present=False)

                officer =  Officer.objects.filter(officer_id=officer_number).get()
                
                return_date = Officer.return_date
                present = Officer.is_present
                               
                if Officer.is_at_vacation == False and present == True and Officer.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Officer.objects.filter(officer_id=Officer.officer_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Officer.objects.filter(officer_id=Officer.officer_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Officer.objects.filter(officer_id=Officer.officer_id).update(is_at_vacation = False)
                                        Officer.objects.filter(officer_id=Officer.officer_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Officer.objects.filter(officer_id=Officer.officer_id).update(is_absent=False)
                                        elif present == False:
                                                Officer.objects.filter(officer_id=Officer.officer_id).update(is_absent=True)
                return redirect("armydbapp:officer_list")

def add_punishment_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_punishment_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_punishment_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                punished_officer = get_object_or_404(Officer, officer_id=officer_number)
                type_of_punishment = request.POST.get('punishment_type')
                start_date_punishment = request.POST.get('punishment_start_date')
                end_date_punishment = request.POST.get('punishment_end_date')

                officer_punishment = OfficerPunishments(officer=punished_officer, 
                                                        punishment=type_of_punishment, 
                                                        start_date=start_date_punishment, 
                                                        end_date=end_date_punishment)
                
                officer_punishment.save()
                officer.objects.filter(officer_id=officer_number).update(current_punishment = officer_punishment)
                officer.objects.filter(officer_id=officer_number).update(is_at_punishment=True)
                return redirect("armydbapp:officer_list")

def officer_information(request):
        officer_id = request.GET.get('officer_id')
        
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        
        for soldier in soldier_list:
                names.append(soldier.name)
        
        officer = Officer.objects.filter(officer_id=officer_id).get()
        info={"officer":officer,"names":names,}
        punishement_list = OfficerPunishments.objects.filter(officer = officer)
        if punishement_list: 
                info.update({"punishement_list":punishement_list})
        
        units_list = OfficerArmyUnits.objects.filter(officer = officer)
        if units_list:
                info.update({"units_list":units_list})
        
        vacations = OfficerVacations.objects.filter(officer = officer)
        if vacations:
                info.update({"vacations":vacations})
        
        rewards = Officer_Rewards.objects.filter(officer = officer)
        if rewards:
                info.update({"rewards":rewards})
        promotions = OfficerPromotion.objects.filter(officer = officer)
        if promotions:
                info.update({"promotions":promotions})
        
        
        return render(request, "armydbapp/officer_information.html",info,)



def delete_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/delete_officer.html",{"officer_number":officer_id,"names":names,},)
        #return render(request, "armydbapp/delete_officer.html",{"soldier_id":soldier_id,"names":names,},)

def submit_delete_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                Officer.objects.filter(officer_id=int(officer_number)).delete()
                return redirect("armydbapp:officer_list")


def dont_delete_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:officer_list")

def add_promotion_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_promotion_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_promotion_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                promoted_officer = get_object_or_404(Officer, officer_id=officer_number)
                officer_rank = request.POST.get('rank')
                officer_promotion = OfficerPromotion(officer=promoted_officer, 
                                                        officer_rank=officer_rank, 
                                                        promotion_date=today,)
                officer_promotion.save()                                        
        return redirect("armydbapp:officer_list")

def awaiting_trial_officer(request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                
        return render(request, "armydbapp/awaiting_trial_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_awaiting_trial_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                reason = request.POST.get('reason-awaiting-trial')
                Officer.objects.filter(officer_id=officer_number).update(is_awaiting_trial=True)
                Officer.objects.filter(officer_id=officer_number).update(reason_awaiting_trial= reason)     
                return redirect("armydbapp:officer_list")
                
def dont_awaiting_trial_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:officer_list")


def trial_done_officer (request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                
        return render(request, "armydbapp/trial_done_officer.html",{"officer_id":officer_id,"names":names,},)


def submit_trial_done_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                Officer.objects.filter(officer_id=officer_number).update(is_awaiting_trial=False)               
                return redirect("armydbapp:officer_list")

def dont_trial_done_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:officer_list")

def reward_consumed_officer (request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        
        return render(request, "armydbapp/reward_consumed_officer.html",{"officer_id":officer_id,"names":names,},)


def submit_reward_consumed_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                Officer.objects.filter(officer_id=officer_number).update(is_rewarded=False)               
                return redirect("armydbapp:officer_list")

def dont_reward_consumed_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:officer_list")

def absent_officer (request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/absent_officer.html",{"officer_id":officer_id,"names":names,},)


def submit_absent_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                Officer.objects.filter(officer_id=officer_number).update(is_absent=True)               
                return redirect("armydbapp:officer_list")

def dont_absent_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:officer_list")

def present_officer (request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/present_officer.html",{"officer_id":officer_id,"names":names,},)


def submit_present_officer(request):
        if request.method == "POST":
                officer_number = int(request.POST.get('officer_number'))
                Officer.objects.filter(officer_id=officer_number).update(is_absent=False)    
                Officer.objects.filter(officer_id=officer_number).update(is_present=True)  
                Officer.objects.filter(officer_id=officer_number).update(is_at_vacation=False)
                Officer.objects.filter(officer_id=officer_number).update(is_at_vacation_sick=False)          
                return redirect("armydbapp:soldier_list")

def dont_present_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:officer_list")

def mission_officer (request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/mission.html",{"officer_id":officer_id,"names":names,},)

def submit_mission_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                type_of_mission = request.POST.get('type_of_mission')
                Officer.objects.filter(officer_id=officer_number).update(mission_type=type_of_mission)
                Officer.objects.filter(officer_id=officer_number).update(is_in_mission=True)
                Officer.objects.filter(officer_id=officer.officer_id).update(is_present=False)
                return redirect("armydbapp:officer_list")

def no_mission_officer (request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/no_mission_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_no_mission_officer(request):
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                Officer.objects.filter(officer_id=officer_number).update(mission_type=None)
                Officer.objects.filter(officer_id=officer_number).update(is_in_mission=False)
                Officer.objects.filter(officer_id=officer.officer_id).update(is_present=True)
                return redirect("armydbapp:officer_list")

def dont_no_mission_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:officer_list")    

def change_army_unit_officer (request):
        officer_id = request.GET.get('officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/change_army_unit_officer.html",{"officer_id":officer_id,"names":names,},)

def submit_change_army_unit_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                officer_number = request.POST.get('officer_number')
                officer =  Officer.objects.filter(officer_id=officer_number)
                officer_army_unit_name = request.POST.get('officer-army-unit-name')
                officer_army_unit_number = request.POST.get('officer-army-unit-number')
                officer_current_army_unit = officer_army_unit_number + " " + officer_army_unit_name
                start_date_unit = today
                officer_last_unit = Officer.objects.get(officer_id=officer_number).current_army_unit
                
                last_unit =  OfficerArmyUnits.objects.filter(soldier= Soldier.objects.get(soldier_id=soldier_number), army_unit = soldier_last_unit)
                last_unit.update(end_date = today)
                
                

                officer_unit = OfficerArmyUnits(officer = Officer.objects.get(officer_id=officer_number), 
                                                army_unit = officer_current_army_unit, 
                                                start_date = start_date_unit, 
                                                )
                
                officer.update(current_army_unit=officer_current_army_unit)
                officer_unit.save()

                return redirect("armydbapp:officer_list")

def dont_change_army_unit_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:officer_list")  


#sub_officer_views
def add_sub_officer(request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_sub_officer.html",{"names":names,},)

def submit_sub_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                sub_officer_name = request.POST.get('sub_officer-name')
                sub_officer_rank = request.POST.get('sub_officer-rank')
                sub_officer_img = request.FILES.get('sub_officer-img')
                sub_officer_id = request.POST.get('sub_officer-id')
                sub_officer_mobile_number= request.POST.get('sub_officer-mobile-number')
                sub_officer_adress= request.POST.get('sub_officer-adress')
                sub_officer_speciality= request.POST.get('sub_officer-speciality')
                sub_officer_army_unit_name = request.POST.get('sub_officer-army-unit-name')
                sub_officer_current_army_unit = sub_officer_army_unit_name
                sub_officer_service_start_date = request.POST.get('sub_officer-service-start-date')
                id_tag= "S"+ str(sub_officer_id)
                new_sub_officer = Sub_officer(  name=sub_officer_name,
                                        rank=sub_officer_rank,
                                        sub_officer_img=sub_officer_img, 
                                        sub_officer_id=sub_officer_id, 
                                        mobile_number = sub_officer_mobile_number,
                                        service_start_date=sub_officer_service_start_date, 
                                        current_army_unit=sub_officer_current_army_unit,
                                        speciality =sub_officer_speciality,
                                        adress = sub_officer_adress,
                                        id_tag= id_tag,
                                        )
                
                new_sub_officer.save()

                sub_officer_unit = Sub_officerArmyUnits(sub_officer = new_sub_officer, 
                                                army_unit = sub_officer_current_army_unit, 
                                                start_date = today, 
                                                )

                sub_officer_unit.save()
                return redirect("armydbapp:add_sub_officer")

def add_img_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_img_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_add_img_sub_officer(request):
        if request.method == "POST":
                sub_officer_img = request.FILES.get('sub_officer-img')
                sub_officer_number = request.POST.get('sub_officer_number')
                sub_officer =  Sub_officer.objects.filter(sub_officer_id=sub_officer_number).get()
                sub_officer.sub_officer_img=sub_officer_img
                sub_officer.save()
                return redirect("armydbapp:sub_officer_list")

def add_reward_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_reward_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_reward_sub_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                rewarded_sub_officer = get_object_or_404(Sub_officer, sub_officer_id=sub_officer_number)
                days_rewarded = request.POST.get('days_rewarded')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(reward_days=days_rewarded)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_rewarded=True)

                new_reward = Sub_officer_Rewards (sub_officer = rewarded_sub_officer, reward_days = days_rewarded)
                
                new_reward.save()

                return redirect("armydbapp:sub_officer_list")


def add_work_assigned_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_work_assigned_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_work_assigned_sub_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                sub_officer = get_object_or_404(Sub_Officer, sub_officer_id=sub_officer_number)
                work_assigned = request.POST.get('work_assigned')
                sub_officer.work_assigned = work_assigned
                sub_officer.save()

                return redirect("armydbapp:sub_officer_list")


def add_remark_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        
        sub_officer = get_object_or_404(Sub_Officer, sub_officer_id=sub_officer_id)
        remarks = sub_officer.remarks

        return render(request, "armydbapp/add_remarks.html",{"sub_officer_id":sub_officer_id,"names":names,"remarks":remarks,},)

def submit_remark_sub_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                sub_officer = get_object_or_404(Sub_Officer, sub_officer_id=sub_officer_number)
                remarks = request.POST.get('remarks')
                old_remarks = sub_officer.remarks
                if old_remarks == None:
                       new_remarks = remarks
                else:
                        new_remarks = str(old_remarks) + " \n "  + str(remarks)
                sub_officer.remarks = new_remarks
                sub_officer.save()
                
        return redirect("armydbapp:sub_officer_list")
        

def add_vacation_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_vacation_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)



def submit_vacation_sub_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                date_of_return = request.POST.get('date_of_return')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(return_date=date_of_return)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_at_vacation=True)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_present=False)
                sub_officer = Sub_officer.objects.filter(sub_officer_id=sub_officer_number).get()
                vacation = Sub_officer_Vacations(sub_officer=sub_officer,start_date=today,end_date=date_of_return)
                vacation.save()
                             
                return_date = sub_officer.return_date
                present = sub_officer.is_present
                               
                if sub_officer.is_at_vacation == False and present == True and sub_officer.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_vacation = False)
                                        Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_absent=False)
                                        elif present == False:
                                                Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_absent=True)
                
                return redirect("armydbapp:sub_officer_list")

def add_vacation_sick_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_vacation_sick_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_vacation_sick_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                date_of_return = request.POST.get('date_of_return')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(return_date=date_of_return)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_at_vacation_sick=True)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_at_vacation=True)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_present=False)

                sub_officer =  Sub_officer.objects.filter(sub_officer_id=sub_officer_number).get()
                
                return_date = sub_Officer.return_date
                present = sub_Officer.is_present
                               
                if sub_Officer.is_at_vacation == False and present == True and sub_Officer.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Sub_officer.objects.filter(sub_officer_id=sub_Officer.sub_officer_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Sub_officer.objects.filter(sub_officer_id=sub_Officer.sub_officer_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Sub_officer.objects.filter(sub_officer_id=sub_Officer.sub_officer_id).update(is_at_vacation = False)
                                        Sub_officer.objects.filter(sub_officer_id=sub_Officer.sub_officer_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Sub_officer.objects.filter(sub_officer_id=sub_Officer.sub_officer_id).update(is_absent=False)
                                        elif present == False:
                                                Sub_officer.objects.filter(sub_officer_id=sub_Officer.sub_officer_id).update(is_absent=True)
                return redirect("armydbapp:sub_officer_list")

def add_punishment_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_punishment_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_punishment_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                punished_sub_officer = get_object_or_404(Sub_officer, sub_officer_id=sub_officer_number)
                type_of_punishment = request.POST.get('punishment_type')
                start_date_punishment = request.POST.get('punishment_start_date')
                end_date_punishment = request.POST.get('punishment_end_date')

                sub_officer_punishment = Sub_officerPunishments(sub_officer=punished_sub_officer, 
                                                        punishment=type_of_punishment, 
                                                        start_date=start_date_punishment, 
                                                        end_date=end_date_punishment)
                
                sub_officer_punishment.save()
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(current_punishment = sub_officer_punishment)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_at_punishment=True)
                return redirect("armydbapp:sub_officer_list")

def sub_officer_information(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        
        for soldier in soldier_list:
                names.append(soldier.name)
        
        sub_officer = Sub_officer.objects.filter(sub_officer_id=sub_officer_id).get()
        info={"sub_officer":sub_officer,"names":names,}
        punishement_list = Sub_officerPunishments.objects.filter(sub_officer = sub_officer)
        if punishement_list: 
                info.update({"punishement_list":punishement_list})
        
        units_list = Sub_officerArmyUnits.objects.filter(sub_officer = sub_officer)
        if units_list:
                info.update({"units_list":units_list})
        
        vacations = Sub_officer_Vacations.objects.filter(sub_officer = sub_officer)
        if vacations:
                info.update({"vacations":vacations})
        
        rewards = Sub_officer_Rewards.objects.filter(sub_officer = sub_officer)
        if rewards:
                info.update({"rewards":rewards})
        promotions = Sub_officer_Promotion.objects.filter(sub_officer = sub_officer)
        if promotions:
                info.update({"promotions":promotions})
        
        
        return render(request, "armydbapp/sub_officer_information.html",info,)



def delete_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/delete_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_delete_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).delete()
                return redirect("armydbapp:sub_officer_list")


def dont_delete_sub_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:sub_officer_list")

def add_promotion_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_promotion_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_promotion_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                promoted_sub_officer = get_object_or_404(Sub_Officer, sub_officer_id=sub_officer_number)
                sub_officer_rank = request.POST.get('rank')
                sub_officer_promotion = sub_OfficerPromotion(sub_officer=promoted_sub_officer, 
                                                        sub_officer_rank=sub_officer_rank, 
                                                        promotion_date=today,)
                sub_officer_promotion.save()                                        
        return redirect("armydbapp:sub_officer_list")

def awaiting_trial_sub_officer(request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                
        return render(request, "armydbapp/awaiting_trial_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_awaiting_trial_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                reason = request.POST.get('reason-awaiting-trial')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_awaiting_trial=True)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(reason_awaiting_trial= reason)     
                return redirect("armydbapp:sub_officer_list")
                
def dont_awaiting_trial_sub_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:sub_officer_list")


def trial_done_sub_officer (request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
                
        return render(request, "armydbapp/trial_done_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)


def submit_trial_done_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_awaiting_trial=False)               
                return redirect("armydbapp:sub_officer_list")

def dont_trial_done_sub_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:sub_officer_list")

def reward_consumed_sub_officer (request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        
        return render(request, "armydbapp/reward_consumed_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)


def submit_reward_consumed_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_rewarded=False)               
                return redirect("armydbapp:sub_officer_list")

def dont_reward_consumed_sub_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:sub_officer_list")

def absent_sub_officer (request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/absent_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)


def submit_absent_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_absent=True)               
                return redirect("armydbapp:sub_officer_list")

def dont_absent_sub_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:sub_officer_list")

def present_sub_officer (request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/present_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)


def submit_present_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_absent=False)    
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_present=True)  
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_at_vacation=False)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_at_vacation_sick=False)          
                return redirect("armydbapp:sub_officer_list")

def dont_present_sub_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:sub_officer_list")

def mission_sub_officer (request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/mission_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_mission_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                type_of_mission = request.POST.get('type_of_mission')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(mission_type=type_of_mission)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_in_mission=True)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_present=False)
                return redirect("armydbapp:sub_officer_list")

def no_mission_sub_officer (request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/no_mission_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_no_mission_sub_officer(request):
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(mission_type=None)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_in_mission=False)
                Sub_officer.objects.filter(sub_officer_id=sub_officer_number).update(is_present=True)
                return redirect("armydbapp:sub_officer_list")

def dont_no_mission_sub_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:sub_officer_list")    

def change_army_unit_sub_officer (request):
        sub_officer_id = request.GET.get('sub_officer_id')
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/change_army_unit_sub_officer.html",{"sub_officer_id":sub_officer_id,"names":names,},)

def submit_change_army_unit_sub_officer(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        if request.method == "POST":
                sub_officer_number = request.POST.get('sub_officer_number')
                sub_officer =  Sub_officer.objects.filter(sub_officer_id=sub_officer_number)
                sub_officer_army_unit_name = request.POST.get('sub_officer-army-unit-name')
                sub_officer_army_unit_number = request.POST.get('sub_officer-army-unit-number')
                sub_officer_current_army_unit = sub_officer_army_unit_number + " " + sub_officer_army_unit_name
                start_date_unit = today
                sub_officer_last_unit = Sub_officer.objects.get(sub_officer_id=sub_officer_number).current_army_unit
                
                last_unit =  Sub_officerArmyUnits.objects.filter(soldier= Soldier.objects.get(soldier_id=soldier_number), army_unit = soldier_last_unit)
                last_unit.update(end_date = today)
                
                

                sub_officer_unit = Sub_officerArmyUnits(sub_officer = Sub_officer.objects.get(sub_officer_id=sub_officer_number), 
                                                army_unit = sub_officer_current_army_unit, 
                                                start_date = start_date_unit, 
                                                )
                
                sub_officer.update(current_army_unit=sub_officer_current_army_unit)
                sub_officer_unit.save()

                return redirect("armydbapp:sub_officer_list")

def dont_change_army_unit_sub_officer(request):
        if request.method == "POST":
                return redirect("armydbapp:sub_officer_list")  


def sub_officer_list(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        soldiers = Soldier.objects.all()
        sub_officer_list = Sub_officer.objects.all()
        sub_officer_list = sub_officer_list.order_by("name")
        sub_officers_punishments = Sub_officerPunishments.objects.all()
        names=[]
        dof3at=[]
        sub_officer_num=[]
        i=1
        for soldier in soldiers:
                names.append(soldier.name)
        for sub_officer in sub_officer_list:
                names.append(sub_officer.name)
                return_date = sub_officer.return_date
                present = sub_officer.is_present
                sub_officer_num.append(i)
                i+=1

                

                if sub_officer.is_at_vacation == False and present == True and sub_officer.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_vacation = False)
                                        Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_absent=False)
                                        elif present == False:
                                                Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_absent=True)
                
                if sub_officer.is_at_punishment == False :
                        pass
                else:

                        for punishment in sub_officers_punishments:
                                if punishment.sub_officer.sub_officer_id == sub_officer.sub_officer_id:
                                        if today < punishment.end_date :
                                                Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(current_punishment=punishment)
                                                Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_punishment=True)
                                        elif today > punishment.end_date:
                                                Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(is_at_punishment=False)
                                                Sub_officer.objects.filter(sub_officer_id=sub_officer.sub_officer_id).update(current_punishment= None)


        
        
        paginator = Paginator(sub_officer_list,101)
        page = request.GET.get('page')
        
        sub_officer_list = paginator.get_page(page)
        return render(request, "armydbapp/sub_officer_list.html",{"sub_officer_list":sub_officer_list,"sub_officers_punishments": sub_officers_punishments,"dof3at": dof3at, "names": names,},)

def officer_list(request):
        today = datetime.datetime.now()
        today = datetime.date(today.year,today.month,today.day)
        soldiers = Soldier.objects.all()
        officer_list = Officer.objects.all()
        officer_list = officer_list.order_by("name")
        

        officers_punishments = OfficerPunishments.objects.all()
        names=[]
        dof3at=[]
        officer_num=[]
        i=1
        for soldier in soldiers:
                names.append(soldier.name)
        for officer in officer_list:
                names.append(officer.name)
                return_date = officer.return_date
                present = officer.is_present
                officer_num.append(i)
                i+=1

                

                if officer.is_at_vacation == False and present == True and officer.is_absent == False:
                      pass
                else:        
                        if return_date:
                                if today < return_date:
                                        Officer.objects.filter(officer_id=officer.officer_id).update(is_at_vacation=True)
                                elif today == return_date:
                                        Officer.objects.filter(officer_id=officer.officer_id).update(is_at_vacation=True)
                                
                                elif today > return_date :
                                        Officer.objects.filter(officer_id=officer.officer_id).update(is_at_vacation = False)
                                        Officer.objects.filter(officer_id=officer.officer_id).update(is_at_vacation_sick = False)
                                        if present == True :
                                                Officer.objects.filter(officer_id=officer.officer_id).update(is_absent=False)
                                        elif present == False:
                                                Officer.objects.filter(officer_id=officer.officer_id).update(is_absent=True)
                
                if officer.is_at_punishment == False :
                        pass
                else:

                        for punishment in officers_punishments:
                                if punishment.officer.officer_id == officer.officer_id:
                                        if today < punishment.end_date :
                                                Officer.objects.filter(officer_id=officer.officer_id).update(current_punishment=punishment)
                                                Officer.objects.filter(officer_id=officer.officer_id).update(is_at_punishment=True)
                                        elif today > punishment.end_date:
                                                Officer.objects.filter(officer_id=officer.officer_id).update(is_at_punishment=False)
                                                Officer.objects.filter(officer_id=officer.officer_id).update(current_punishment=None)


        
        
        paginator = Paginator(officer_list,31)
        page = request.GET.get('page')
        
        officer_list = paginator.get_page(page)
        return render(request, "armydbapp/officer_list.html",{"officer_list":officer_list,"officers_punishments": officers_punishments,"dof3at": dof3at, "names": names,},)


def map_builder (request):
        working_map = request.GET.get('working_map')
        names = []
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        companys = Company.objects.all()
        squads = Squad.objects.all()
        soldier_list_filtered = []
        company= [] 
        for soldier in soldier_list:
                names.append(soldier.name)
                if str(soldier.current_army_unit) == working_map:
                        soldier_list_filtered.append(soldier)
        for squad in squads: 
                if squad.squad_name == working_map:
                        company.append(squad.company)

        return render(request, "armydbapp/map.html",{"soldier_list_filtered":soldier_list_filtered,"names": names,"company": company,"squads": squads, "working_map": working_map},)

def mashro3_agaza (request):
        names = []
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        mashro3_awel = []
        mashro3_tani = []
        mashro3_talat = []

        for soldier in soldier_list:
                if soldier.vacation_choice == 1:
                        mashro3_awel.append(soldier)
                if soldier.vacation_choice == 2:
                        mashro3_tani.append(soldier)
                if soldier.vacation_choice == 3:
                        mashro3_talat.append(soldier)

        paginator1 = Paginator(mashro3_awel,31)
        page1 = request.GET.get('page')
        paginator2 = Paginator(mashro3_tani,31)
        page2 = request.GET.get('page')
        paginator3 = Paginator(mashro3_talat,31)
        page3 = request.GET.get('page')
        
        mashro3_awel = paginator1.get_page(page1)
        mashro3_tani = paginator2.get_page(page2)
        mashro3_talat = paginator3.get_page(page3)
        return render(request, "armydbapp/mashro3_agaza.html",{"mashro3_awel":mashro3_awel,"mashro3_tani":mashro3_tani,"mashro3_talat":mashro3_talat, "names": names,},)

def sarfaya_numbering ():
        soldiers = Soldier.objects.all()
        no_sarfaya = 0 
        no_salary = 0 
        salary = 0 
        for soldier in soldiers: 
                if soldier.a5eir_sarfaya == "بدون اخر صرفية":
                        no_sarfaya +=1
                if soldier.a5eir_sarfaya == "تم استلام اخر صرفية و لم يتم الدرج بالماهية":
                        no_salary += 1
                if soldier.a5eir_sarfaya == "تم الدرج بالماهية":
                        salary += 1
        
        return str(no_sarfaya),str(no_salary),str(salary)


def sarfaya_list (request):
        names = []
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        choice1 = []
        choice2 = []
        choice3 = []

        for soldier in soldier_list:
                names.append(soldier.name)
                if soldier.a5eir_sarfaya == "بدون اخر صرفية":
                        choice1.append(soldier)
                if soldier.a5eir_sarfaya == "تم استلام اخر صرفية و لم يتم الدرج بالماهية":
                        choice2.append(soldier)
                if soldier.a5eir_sarfaya == "تم الدرج بالماهية":
                        choice3.append(soldier)

        paginator1 = Paginator(choice1,31)
        page1 = request.GET.get('page')
        paginator2 = Paginator(choice2,31)
        page2 = request.GET.get('page')
        paginator3 = Paginator(choice3,31)
        page3 = request.GET.get('page')
        
        choice1 = paginator1.get_page(page1)
        choice2 = paginator2.get_page(page2)
        choice3 = paginator3.get_page(page3)
        return render(request, "armydbapp/sarfaya_list.html",{"choice1":choice1,"choice2":choice2,"choice3":choice3, "names": names,},)

def settings (request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/settings.html",{"names":names,},)


def units_settings (request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/units_settings.html",{"names":names,},)

def add_company (request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_company.html",{"names":names,},)

def add_squad (request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        return render(request, "armydbapp/add_squad.html",{"names":names,},)

def submit_new_company (request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)
        company_name = request.POST.get('company-name')
        company_img = request.FILES.get('company-img')
        new_company = Company(  company_name=company_name,
                                        company_img=company_img, 
                                        )
                
        new_company.save()

        return render(request, "armydbapp/add_company.html",{"names":names,},)

def submit_new_squad (request):
        soldier_list = Soldier.objects.all()
        soldier_list = soldier_list.order_by("name")
        names=[]
        for soldier in soldier_list:
                names.append(soldier.name)

        squad_name = request.POST.get('squad-name')
        company_name = request.POST.get('unit-name')
        company = get_object_or_404(Company, company_name=company_name)
        new_squad = Squad(  squad_name=squad_name,
                                        company=company, 
                                        )

        new_squad.save()

        return render(request, "armydbapp/add_squad.html",{"names":names,},)


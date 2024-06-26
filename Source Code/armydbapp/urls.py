from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'armydbapp'

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('loguser', views.login_user, name='loguser'),
    path('logout', views.logout_user, name='logout'),
    path('', views.index, name='index'),
    path('soldier_list', views.soldier_list, name='soldier_list'),
    path('soldier_search', views.soldier_search, name='soldier_search'),
    path('add_soldier', views.add_soldier, name='add_soldier'),
    path('submit_soldier', views.submit_soldier, name='submit_soldier'),
    path('add_reward', views.add_reward, name='add_reward'),
    path('submit_reward', views.submit_reward, name='submit_reward'),
    path('add_vacation', views.add_vacation, name='add_vacation'),
    path('submit_vacation', views.submit_vacation, name='submit_vacation'),
    path('add_vacation_sick', views.add_vacation_sick, name='add_vacation_sick'),
    path('submit_vacation_sick', views.submit_vacation_sick, name='submit_vacation_sick'),
    path('add_punishment', views.add_punishment, name='add_punishment'),
    path('submit_punishment', views.submit_punishment, name='submit_punishment'),          
    path('soldier_information', views.soldier_information, name='soldier_information'),
    path('delete_soldier', views.delete_soldier, name='delete_soldier'),
    path('submit_delete_soldier', views.submit_delete_soldier, name='submit_delete_soldier'),
    path('dont_delete_soldier', views.dont_delete_soldier, name='dont_delete_soldier'),
    path('awaiting_trial', views.awaiting_trial, name='awaiting_trial'),
    path('submit_awaiting_trial', views.submit_awaiting_trial, name='submit_awaiting_trial'),
    path('dont_awaiting_trial', views.dont_awaiting_trial, name='dont_awaiting_trial'),
    path('trial_done', views.trial_done, name='trial_done'),
    path('submit_trial_done', views.submit_trial_done, name='submit_trial_done'),
    path('dont_trial_done', views.dont_trial_done, name='dont_trial_done'),
    path('reward_consumed', views.reward_consumed, name='reward_consumed'),
    path('submit_reward_consumed', views.submit_reward_consumed, name='submit_reward_consumed'),
    path('dont_reward_consumed', views.dont_reward_consumed, name='dont_reward_consumed'),
    path('absent', views.absent, name='absent'),
    path('submit_absent', views.submit_absent, name='submit_absent'),
    path('dont_absent', views.dont_absent, name='dont_absent'),
    path('present', views.present, name='present'),
    path('submit_present', views.submit_present, name='submit_present'),
    path('dont_present', views.dont_present, name='dont_present'),
    path('outing', views.outing, name='outing'),
    path('submit_outing', views.submit_outing, name='submit_outing'),
    path('no_outing', views.no_outing, name='no_outing'),
    path('submit_no_outing', views.submit_no_outing, name='submit_no_outing'),
    path('dont_no_outing', views.dont_no_outing, name='dont_no_outing'),
    path('mission', views.mission, name='mission'),
    path('submit_mission', views.submit_mission, name='submit_mission'),
    path('no_mission', views.no_mission, name='no_mission'),
    path('submit_no_mission', views.submit_no_mission, name='submit_no_mission'),
    path('dont_no_mission', views.dont_no_mission, name='dont_no_mission'),
    path('change_army_unit', views.change_army_unit, name='change_army_unit'),
    path('submit_change_army_unit', views.submit_change_army_unit, name='submit_change_army_unit'),
    path('dont_change_army_unit', views.dont_change_army_unit, name='dont_change_army_unit'),
    path('reward_list', views.reward_list, name='reward_list'),
    path('punished_list', views.punished_list, name='punished_list'),
    path('late_vacation_list', views.late_vacation_list, name='late_vacation_list'),
    path('return_today_list', views.return_today_list, name='return_today_list'),
    path('late_unit_list', views.late_unit_list, name='late_unit_list'),
    path('vacation_choice', views.vacation_choice, name='vacation_choice'),
    path('katiba_headquart', views.katiba_headquart, name='katiba_headquart'),
    path('s1_headquart', views.s1_headquart, name='s1_headquart'),

    path('قياس1', views._قياس1, name='قياس1'),
    path('13احمد', views._13احمد, name='13احمد'),
    path('11رياض', views._11رياض, name='11رياض'),
    path('11محمود', views._11محمود, name='11محمود'),
    path('12رياض', views._12رياض, name='12رياض'),
    path('12محمود', views._12محمود, name='12محمود'),
    path('13رياض', views._13رياض, name='13رياض'),
    path('13محمود', views._13محمود, name='13محمود'),
    path('14رياض', views._14رياض, name='14رياض'),
    path('14محمود', views._14محمود, name='14محمود'),
    path('15رياض', views._15رياض, name='15رياض'),
    path('15محمود', views._15محمود, name='15محمود'),
    path('1سعيد', views._1سعيد, name='1سعيد'),
    path('1عرب', views._1عرب, name='1عرب'),
    path('2سعيد', views._2سعيد, name='2سعيد'),
    path('2عرب', views._2عرب, name='2عرب'),

    path('قياس2', views._قياس2, name='قياس2'),
    path('3عرب', views._3عرب, name='3عرب'),
    path('4سعيد', views._4سعيد, name='4سعيد'),
    path('4عرب', views._4عرب, name='4عرب'),
    path('5عرب', views._5عرب, name='5عرب'),
    path('6عرب', views._6عرب, name='6عرب'),
    path('7عرب', views._7عرب, name='7عرب'),
    path('8عرب', views._8عرب, name='8عرب'),
    path('9سعيد', views._9سعيد, name='9سعيد'),
    path('9عرب', views._9عرب, name='9عرب'),
    path('9عرب', views._9عرب, name='9عرب'),

    path('قياس3', views._قياس3, name='قياس3'),
    path('11عرب', views._11عرب, name='11عرب'),
    path('12سعيد', views._12سعيد, name='12سعيد'),
    path('13سعيد', views._13سعيد, name='13سعيد'),
    path('13عرب', views._13عرب, name='13عرب'),


    path('dof3a_radif', views.dof3a_radif, name='dof3a_radif'),
    path('awaiting_trial_list', views.awaiting_trial_list, name='awaiting_trial_list'),
    path('absent_list', views.absent_list, name='absent_list'),
    path('add_img', views.add_img, name='add_img'),
    path('submit_add_img', views.submit_add_img, name='submit_add_img'),
    path('add_promotion', views.add_promotion, name='add_promotion'),
    path('submit_promotion', views.submit_promotion, name='submit_promotion'),
    path('add_zucchini', views.add_zucchini, name='add_zucchini'),
    path('submit_zucchini', views.submit_zucchini, name='submit_zucchini'),
    path('add_work_assigned', views.add_work_assigned, name='add_work_assigned'),
    path('submit_work_assigned', views.submit_work_assigned, name='submit_work_assigned'),
    path('add_job', views.add_job, name='add_job'),
    path('submit_job', views.submit_job, name='submit_job'),
    path('s1_all', views.s1_all, name='s1_all'),
    path('s2_all', views.s2_all, name='s2_all'),
    path('s3_all', views.s3_all, name='s3_all'),
    path('add_remark', views.add_remark, name='add_remark'),
    path('submit_remark', views.submit_remark, name='submit_remark'),
    path('mawkaf_a5eir_sarfaya', views.mawkaf_a5eir_sarfaya, name='mawkaf_a5eir_sarfaya'),
    path('submit_mawkaf_a5eir_sarfaya', views.submit_mawkaf_a5eir_sarfaya, name='submit_mawkaf_a5eir_sarfaya'),
    path('present_list', views.present_list, name='present_list'),
    path('absent_indexList', views.absent_indexList, name='absent_indexList'),
    path('out_list', views.out_list, name='out_list'),
    path('vacation_list', views.vacation_list, name='vacation_list'),
    path('vacation_sick_list', views.vacation_sick_list, name='vacation_sick_list'),
    path('mission_list', views.mission_list, name='mission_list'),
    path('prison_list', views.prison_list, name='prison_list'),
    #officer_views
    path('add_officer', views.add_officer, name='add_officer'),
    path('submit_officer', views.submit_officer, name='submit_officer'),
    path('add_img_officer', views.add_img_officer, name='add_img_officer'),
    path('submit_add_img_officer', views.submit_add_img_officer, name='submit_add_img_officer'),
    path('add_reward_officer', views.add_reward_officer, name='add_reward_officer'),
    path('submit_reward_officer', views.submit_reward_officer, name='submit_reward_officer'),
    path('add_work_assigned_officer', views.add_work_assigned_officer, name='add_work_assigned_officer'),
    path('submit_work_assigned_officer', views.submit_work_assigned_officer, name='submit_work_assigned_officer'),
    path('add_remark_officer', views.add_remark_officer, name='add_remark_officer'),
    path('submit_remark_officer', views.submit_remark_officer, name='submit_remark_officer'),
    path('add_vacation_officer', views.add_vacation_officer, name='add_vacation_officer'),
    path('submit_vacation_officer', views.submit_vacation_officer, name='submit_vacation_officer'),
    path('add_vacation_sick_officer', views.add_vacation_sick_officer, name='add_vacation_sick_officer'),
    path('submit_vacation_sick_officer', views.submit_vacation_sick_officer, name='submit_vacation_sick_officer'),
    path('add_punishment_officer', views.add_punishment_officer, name='add_punishment_officer'),
    path('submit_punishment_officer', views.submit_punishment_officer, name='submit_punishment_officer'),
    path('officer_information', views.officer_information, name='officer_information'),
    path('delete_officer', views.delete_officer, name='delete_officer'),
    path('submit_delete_officer', views.submit_delete_officer, name='submit_delete_officer'),
    path('dont_delete_officer', views.dont_delete_officer, name='dont_delete_officer'),
    path('add_promotion_officer', views.add_promotion_officer, name='add_promotion_officer'),
    path('submit_promotion_officer', views.submit_promotion_officer, name='submit_promotion_officer'),
    path('awaiting_trial_officer', views.awaiting_trial_officer, name='awaiting_trial_officer'),
    path('submit_awaiting_trial_officer', views.submit_awaiting_trial_officer, name='submit_awaiting_trial_officer'),
    path('dont_awaiting_trial_officer', views.dont_awaiting_trial_officer, name='dont_awaiting_trial_officer'),
    path('trial_done_officer', views.trial_done_officer, name='trial_done_officer'),
    path('submit_trial_done_officer', views.submit_trial_done_officer, name='submit_trial_done_officer'),
    path('dont_trial_done_officer', views.dont_trial_done_officer, name='dont_trial_done_officer'),
    path('reward_consumed_officer', views.reward_consumed_officer, name='reward_consumed_officer'),
    path('submit_reward_consumed_officer', views.submit_reward_consumed_officer, name='submit_reward_consumed_officer'),
    path('dont_reward_consumed_officer', views.dont_reward_consumed_officer, name='dont_reward_consumed_officer'),
    path('absent_officer', views.absent_officer, name='absent_officer'),
    path('submit_absent_officer', views.submit_absent_officer, name='submit_absent_officer'),
    path('dont_absent_officer', views.dont_absent_officer, name='dont_absent_officer'),
    path('present_officer', views.present_officer, name='present_officer'),
    path('submit_present_officer', views.submit_present_officer, name='submit_present_officer'),
    path('dont_present_officer', views.dont_present_officer, name='dont_present_officer'),
    path('mission_officer', views.mission_officer, name='mission_officer'),
    path('submit_mission_officer', views.submit_mission_officer, name='submit_mission_officer'),
    path('no_mission_officer', views.no_mission_officer, name='no_mission_officer'),
    path('submit_no_mission_officer', views.submit_no_mission_officer, name='submit_no_mission_officer'),
    path('dont_no_mission_officer', views.dont_no_mission_officer, name='dont_no_mission_officer'),
    path('change_army_unit_officer', views.change_army_unit_officer, name='change_army_unit_officer'),
    path('submit_change_army_unit_officer', views.submit_change_army_unit_officer, name='submit_change_army_unit_officer'),
    path('dont_change_army_unit_officer', views.dont_change_army_unit_officer, name='dont_change_army_unit_officer'),
    #sub_officer_views
    path('add_sub_officer', views.add_sub_officer, name='add_sub_officer'),
    path('submit_sub_officer', views.submit_sub_officer, name='submit_sub_officer'),
    path('add_img_sub_officer', views.add_img_sub_officer, name='add_img_sub_officer'),
    path('submit_add_img_sub_officer', views.submit_add_img_sub_officer, name='submit_add_img_sub_officer'),
    path('add_reward_sub_officer', views.add_reward_sub_officer, name='add_reward_sub_officer'),
    path('submit_reward_sub_officer', views.submit_reward_sub_officer, name='submit_reward_sub_officer'),
    path('add_work_assigned_sub_officer', views.add_work_assigned_sub_officer, name='add_work_assigned_sub_officer'),
    path('submit_work_assigned_sub_officer', views.submit_work_assigned_sub_officer, name='submit_work_assigned_sub_officer'),
    path('add_remark_sub_officer', views.add_remark_sub_officer, name='add_remark_sub_officer'),
    path('submit_remark_sub_officer', views.submit_remark_sub_officer, name='submit_remark_sub_officer'),
    path('add_vacation_sub_officer', views.add_vacation_sub_officer, name='add_vacation_sub_officer'),
    path('submit_vacation_sub_officer', views.submit_vacation_sub_officer, name='submit_vacation_sub_officer'),
    path('add_vacation_sick_sub_officer', views.add_vacation_sick_sub_officer, name='add_vacation_sick_sub_officer'),
    path('submit_vacation_sick_sub_officer', views.submit_vacation_sick_sub_officer, name='submit_vacation_sick_sub_officer'),
    path('add_punishment_sub_officer', views.add_punishment_sub_officer, name='add_punishment_sub_officer'),
    path('submit_punishment_sub_officer', views.submit_punishment_sub_officer, name='submit_punishment_sub_officer'),
    path('sub_officer_information', views.sub_officer_information, name='sub_officer_information'),
    path('delete_sub_officer', views.delete_sub_officer, name='delete_sub_officer'),
    path('submit_delete_sub_officer', views.submit_delete_sub_officer, name='submit_delete_sub_officer'),
    path('dont_delete_sub_officer', views.dont_delete_sub_officer, name='dont_delete_sub_officer'),
    path('add_promotion_sub_officer', views.add_promotion_sub_officer, name='add_promotion_sub_officer'),
    path('submit_promotion_sub_officer', views.submit_promotion_sub_officer, name='submit_promotion_sub_officer'),
    path('awaiting_trial_sub_officer', views.awaiting_trial_sub_officer, name='awaiting_trial_sub_officer'),
    path('submit_awaiting_trial_sub_officer', views.submit_awaiting_trial_sub_officer, name='submit_awaiting_trial_sub_officer'),
    path('dont_awaiting_trial_sub_officer', views.dont_awaiting_trial_sub_officer, name='dont_awaiting_trial_sub_officer'),
    path('trial_done_sub_officer', views.trial_done_sub_officer, name='trial_done_sub_officer'),
    path('submit_trial_done_sub_officer', views.submit_trial_done_sub_officer, name='submit_trial_done_sub_officer'),
    path('dont_trial_done_sub_officer', views.dont_trial_done_sub_officer, name='dont_trial_done_sub_officer'),
    path('reward_consumed_sub_officer', views.reward_consumed_sub_officer, name='reward_consumed_sub_officer'),
    path('submit_reward_consumed_sub_officer', views.submit_reward_consumed_sub_officer, name='submit_reward_consumed_sub_officer'),
    path('dont_reward_consumed_sub_officer', views.dont_reward_consumed_sub_officer, name='dont_reward_consumed_sub_officer'),
    path('absent_sub_officer', views.absent_sub_officer, name='absent_sub_officer'),
    path('submit_absent_sub_officer', views.submit_absent_sub_officer, name='submit_absent_sub_officer'),
    path('dont_absent_sub_officer', views.dont_absent_sub_officer, name='dont_absent_sub_officer'),
    path('present_sub_officer', views.present_sub_officer, name='present_sub_officer'),
    path('submit_present_sub_officer', views.submit_present_sub_officer, name='submit_present_sub_officer'),
    path('dont_present_sub_officer', views.dont_present_sub_officer, name='dont_present_sub_officer'),
    path('mission_sub_officer', views.mission_sub_officer, name='mission_sub_officer'),
    path('submit_mission_sub_officer', views.submit_mission_sub_officer, name='submit_mission_sub_officer'),
    path('no_mission_sub_officer', views.no_mission_sub_officer, name='no_mission_sub_officer'),
    path('submit_no_mission_sub_officer', views.submit_no_mission_sub_officer, name='submit_no_mission_sub_officer'),
    path('dont_no_mission_sub_officer', views.dont_no_mission_sub_officer, name='dont_no_mission_sub_officer'),
    path('change_army_unit_sub_officer', views.change_army_unit_sub_officer, name='change_army_unit_sub_officer'),
    path('submit_change_army_unit_sub_officer', views.submit_change_army_unit_sub_officer, name='submit_change_army_unit_sub_officer'),
    path('dont_change_army_unit_sub_officer', views.dont_change_army_unit_sub_officer, name='dont_change_army_unit_sub_officer'),
    path('officer_list', views.officer_list, name='officer_list'),
    path('sub_officer_list', views.sub_officer_list, name='sub_officer_list'),
    path('map_builder', views.map_builder, name='map_builder'),
    path('mashro3_agaza', views.mashro3_agaza, name='mashro3_agaza'),
    path('sarfaya_list', views.sarfaya_list, name='sarfaya_list'),
    path('settings', views.settings, name='settings'),
    path('units_settings', views.units_settings, name='units_settings'),
    path('add_company', views.add_company, name='add_company'),
    path('add_squad', views.add_squad, name='add_squad'),
    path('submit_new_company', views.submit_new_company, name='submit_new_company'),
    path('submit_new_squad', views.submit_new_squad, name='submit_new_squad'),
    #path('delete_unit', views.delete_unit, name='delete_unit'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
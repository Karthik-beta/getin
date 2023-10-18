from django.urls import re_path
from reportapp import views

from reportapp.views import (AttendanceRecordListView,
                         AttendanceSummaryView,
                         AutocompleteView,
                         EmployeeDataListCreateView,
                         EmployeeDataRetrieveUpdateDeleteView,
                         ExportExcelView,
                         AttendanceStatisticsAPIView,
                         DownloadEmployeeData,
                         AttendanceStatisticsMonthAPIView,
                         DownloadAttendanceData,
                         GenderCountAPI,)

urlpatterns = [

    re_path(r'^attendance_record/$', AttendanceRecordListView.as_view(), name='attendance_record_list'),

    re_path(r'^autocomplete/$', AutocompleteView.as_view(), name='autocomplete'),

    re_path(r'^attendance_summary/$', AttendanceSummaryView.as_view(), name='attendance_summary'),

    re_path(r'^employee/$', EmployeeDataListCreateView.as_view(), name='employee-list-create'),

    # re_path(r'^employee/$', views.employeeApi),
    # re_path(r'^employee/([0-9]+)$', views.employeeApi),

    re_path(r'^employee/(?P<employee_id>\d+)/$', EmployeeDataRetrieveUpdateDeleteView.as_view(), name='employee-retrieve-update-delete'),


    re_path(r'^export_excel/$', ExportExcelView.as_view(), name='export-excel'),

    re_path(r'^AttendanceStatistics/$', AttendanceStatisticsAPIView.as_view()),

    re_path(r'^AttendanceStatisticsMonth/$', AttendanceStatisticsMonthAPIView.as_view()),

    re_path(r'^download_employee_data/$', DownloadEmployeeData.as_view(), name='download-employee-data'),

    re_path(r'^download_attendance_data/$', DownloadAttendanceData.as_view(), name='download-attendance-data'),

    re_path(r'^gender_count/$', GenderCountAPI.as_view(), name='gender-count')

]
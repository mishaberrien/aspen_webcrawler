from utils import StudentAttendance
# from utils import StudentIdentifyingInfo
import credentials

student_info = StudentAttendance()

student_info.login_aspen_website(credentials.ASPEN_USERNAME,
                                      credentials.ASPEN_PASSWORD)
student_info.select_view('school')
student_info.select_school('ascend')
student_info.select_tab('Student')
student_info.select_filter('former')
report = student_info.pull_attendance_report()

report.to_csv('../data/attendance_ascend_former.csv',
              index=False)
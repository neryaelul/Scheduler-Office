import mysql.connector
# Import date class from datetime module
from datetime import date, datetime
import hashlib
import random
import string



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hadar"
)


mycursor = mydb.cursor()

async def token(key):
    # Returns the current local date
        sql = "SELECT * FROM teachers WHERE token = %s" 
        adr = (key, )
        mycursor.execute(sql, adr)

        record_teacher = mycursor.fetchone()

        if record_teacher is not None:
            num_result_teacher = len(record_teacher)
        else:
            num_result_teacher = 0
        if num_result_teacher > 0:
            return {"s":1,"permission" : record_teacher[10] }
        else:
            return {"s":0,"permission" : 0 }

async def newLessons(name,price,TeacherId,RoomColor):
    today = datetime.today()
    # Returns the current local date
    sql = "INSERT INTO lessons (date,name,price,TeacherId,RoomColor) VALUES (%s,%s,%s,%s,%s)"
    val = (today,name,price,TeacherId,RoomColor)
    mycursor.execute(sql,val)

    mydb.commit()

    return mycursor.rowcount, "השיעור התווסף בהצלחה"
#newLessons("fff")

async def newStudent(FirstName,LastName,id,address):
    today = datetime.today()
    # Returns the current local date
    sql = "INSERT INTO students (date,FirstName,LastName,IdentificationCard,address) VALUES (%s,%s,%s,%s,%s)"
    val = (today,FirstName,LastName,id,address)
    mycursor.execute(sql,val)

    mydb.commit()

    return mycursor.rowcount, "התלמיד נוסף בהצלחה"
#newLessons("fff")

async def delLessons(id):
    today = datetime.today()
    # Returns the current local date
    sql = "DELETE FROM test WHERE id = %s"
    adr = (id, )

    mycursor.execute(sql, adr)

    mydb.commit()

    print(mycursor.rowcount, "record delete.")
    
async def studentInfo():
    today = datetime.today()
    # Returns the current local date
    sql = "SELECT * FROM students"    

    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    print(len(myresult))
    allRes = []
    i = 0
    for x in myresult:
        allRes.append(
             {
                "id": x[0],
                "name": x[1] +' '+ x[2]              
            })
    return allRes


#להמשיך מפה
async def updateSchedule(id):
    today = datetime.today()
    sql = "UPDATE schedule SET canceled = '1' WHERE id = %s"
    val = (id,)

        # Execute the SQL query
    mycursor.execute(sql, val)
    mydb.commit()
    return "השיעור בוטל"


async def lessonsInfo():
    # Returns the current local date
    sql = "SELECT * FROM lessons"    

    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    print(len(myresult))
    allRes = []
    i = 0
    for x in myresult:
       
       sql_teacher = "SELECT * FROM teachers WHERE id = %s" 
       adr_teacher = (x[3], )
       mycursor.execute(sql_teacher, adr_teacher)
       
       
       record_teacher = mycursor.fetchone()
       num_result_teacher = len(record_teacher)
    
       if(num_result_teacher > 0):
          allRes.append(
             {
                "id": x[0],
                "name": x[1],
                "teacher":record_teacher[2] + ' ' + record_teacher[3]
                
            })
    return allRes
           

async def selectLessons(id):
    today = datetime.today()
    # Returns the current local date
    sql = "SELECT * FROM lessons WHERE name = %s"
    adr = (id, )

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()
    print(len(myresult))
    for x in myresult:
        print(x)

async def get_schedule_day(day):
    today = datetime.today()
    date_str = day  # single argument representing a date
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    # Returns the current local date
    target_date = date_obj
    sql = "SELECT * FROM schedule WHERE DATE(ScheduleDate) = %s AND canceled = '0' "
    adr = (target_date, )

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()
    
    print(len(myresult))
    allRes = []
    i = 0
    for x in myresult:
       
        sql_lesson = "SELECT * FROM lessons WHERE id = %s" 
        adr_lesson = (x[2], )
        mycursor.execute(sql_lesson, adr_lesson)
        result_lesson = mycursor.fetchone()

        if result_lesson is not None:
            num_result_lesson = len(result_lesson)
        else:
            num_result_lesson = 0
       

        if num_result_lesson > 0:
            print(num_result_lesson)
            print(result_lesson)
            sql_student = "SELECT * FROM students WHERE id = %s" 
            adr_student = (x[4], )
            mycursor.execute(sql_student, adr_student)
            record_student = mycursor.fetchone()

            if record_student is not None:
                num_result_student = len(record_student)
            else:
                num_result_student = 0

            print(record_student)

            if num_result_student > 0:
                sql_teacher = "SELECT * FROM teachers WHERE id = %s" 
                adr_teacher = (result_lesson[3], )
                mycursor.execute(sql_teacher, adr_teacher)
                record_teacher = mycursor.fetchone()
                
                if record_teacher is not None:
                    num_result_teacher = len(record_teacher)
                else:
                    num_result_teacher = 0
                print(record_teacher[1])

                
                if(num_result_teacher > 0):
                    allRes.append(
                        {
                        "id": x[0],
                        "name": result_lesson[1],
                        "date": x[3],
                        "RoomColor":result_lesson[5],
                        "teacher":record_teacher[2] + ' ' + record_teacher[3],
                        "student":record_student[1] + ' ' + record_student[2]
                    })
         

         
    print(allRes)
    return allRes

#/////////// דרך יעילה וקצרה יותר לכתוב ע״י sql ושילוב טבלאות ////////////

# async def get_schedule_day(day):
#     date_str = day
#     date_obj = datetime.strptime(date_str, '%Y-%m-%d')

#     sql = """SELECT lessons.name, schedule.ScheduleDate, lessons.RoomColor, 
#                     CONCAT(teachers.FirstName, ' ', teachers.LastName) as teacher,
#                     CONCAT(students.FirstName, ' ', students.LastName) as student
#             FROM schedule
#             INNER JOIN lessons ON schedule.lessonId = lessons.id
#             INNER JOIN students ON schedule.studentId = students.id
#             INNER JOIN teachers ON lessons.teacherId = teachers.id
#             WHERE DATE(schedule.ScheduleDate) = %s"""

#     adr = (date_obj, )
#     mycursor.execute(sql, adr)
#     myresult = mycursor.fetchall()

#     allRes = []
#     for row in myresult:
#         allRes.append({
#             "name": row[0],
#             "date": row[1],
#             "RoomColor": row[2],
#             "teacher": row[3],
#             "student": row[4]
#         })
        
#     print(allRes)
#     return allRes




    



async def newSchedule(LessonId,StudentId,ScheduleDate):
    today = datetime.today()
    # Returns the current local date
    original_datetime = datetime.strptime(ScheduleDate, "%Y-%m-%d %H:%M")
    new_datetime = original_datetime.replace(minute=0)
    new_datetime_str = new_datetime.strftime("%Y-%m-%d %H:%M")

    print(new_datetime_str)
    sql = "SELECT * FROM schedule WHERE LessonId = %s AND ScheduleDate = %s AND canceled = 0"
    adr = (LessonId, new_datetime_str)

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()
    num_result = len(myresult)
    if(num_result <= 0):
        
        sql = "INSERT INTO schedule (date,LessonId,StudentId,ScheduleDate) VALUES (%s,%s,%s,%s)"
        val = (today,LessonId,StudentId, new_datetime_str)
        mycursor.execute(sql,val)

        mydb.commit()

        # return mycursor.rowcount, "record inserted."
        return "השיעור נקבע בהצלחה"
    else:
        return "קיים שיעור זהה באותו זמן"
    

async def delSchedule(id):
    today = datetime.today()
    # Returns the current local date
    sql = "DELETE FROM schedule WHERE id = %s"
    adr = (id, )

    mycursor.execute(sql, adr)

    mydb.commit()

    return (mycursor.rowcount, "record delete.")

async def newTeacher(FirstName,LastName,SalaryPerHour,IdentificationCard,address,username,password,permission):
    today = datetime.today()
    # Returns the current local date
    if len(password) < 8:
        return 0,"הסיסמה חייבת להכיל מעל 8 תווים"
    
    else:
        sql = "SELECT * FROM teachers WHERE username = %s" 
        adr = (username, )
        mycursor.execute(sql, adr)

        record_teacher = mycursor.fetchone()

        if record_teacher is not None:
            num_result_teacher = len(record_teacher)
        else:
            num_result_teacher = 0
        
        if num_result_teacher > 0:
            return mycursor.rowcount, "שם מתשמש זה כבר קיים"
        else:
            # Create a new sha256 hash object
            hash_object = hashlib.sha256()
            hash_object.update(password.encode())
            hex_dig_password = hash_object.hexdigest()

            now = datetime.today()
            sql = "INSERT INTO teachers (FirstName,LastName,Date,SalaryPerHour,IdentificationCard,address,username,password,permission) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (FirstName,LastName,now,SalaryPerHour,IdentificationCard,address,username,hex_dig_password,permission)
            mycursor.execute(sql,val)

            mydb.commit()
        
            return mycursor.rowcount, "המורה נוסף בהצלחה"
        
async def report(target_month,target_year):

    today = datetime.today()
    # Returns the current local date
    allRes = []
    now = datetime.now()

    # Get the current month
    current_month = now.month

    sql_scheduleNotCanceled = "SELECT * FROM schedule WHERE MONTH(ScheduleDate) = %s AND YEAR(ScheduleDate) = %s"
    adr_scheduleNotCanceled = (target_month, target_year)
    mycursor.execute(sql_scheduleNotCanceled, adr_scheduleNotCanceled)
       
    scheduleThisMonthNotCanceled =  mycursor.fetchall()

    if scheduleThisMonthNotCanceled is not None:
        num_result_scheduleThisMonthNotCanceled = len(scheduleThisMonthNotCanceled)
    else:
        num_result_scheduleThisMonthNotCanceled = 0

    allRes.append(
    {
        "scheduleNotCanceled": num_result_scheduleThisMonthNotCanceled
    })
        

    sql_scheduleCanceled = "SELECT * FROM schedule WHERE MONTH(ScheduleDate) = %s AND YEAR(ScheduleDate) = %s AND canceled = 1"
    adr_scheduleCanceled = (target_month, target_year)
    mycursor.execute(sql_scheduleCanceled, adr_scheduleCanceled)
    scheduleThisMonthCanceled =  mycursor.fetchall()

    if scheduleThisMonthCanceled is not None:
        num_result_scheduleThisMonthCanceled_number = len(scheduleThisMonthCanceled)
    else:
        num_result_scheduleThisMonthCanceled_number = 0

    allRes.append(
    {
        "scheduleThisMonthCanceled": num_result_scheduleThisMonthCanceled_number
    })
    
    
    sql_students = "SELECT * FROM students WHERE MONTH(date) = %s AND YEAR(date) = %s"
    adr_students = (target_month, target_year)
    mycursor.execute(sql_students, adr_students)
    studentsThisMonth = mycursor.fetchall()
    if scheduleThisMonthCanceled is not None:
        studentsThisMonth_number = len(studentsThisMonth)
    else:
        studentsThisMonth_number = 0

    allRes.append(
    {
        "students": studentsThisMonth_number
    })

    sql_teachers = "SELECT * FROM teachers WHERE  MONTH(date) = %s AND YEAR(date) = %s"
    adr_teachers = (target_month, target_year)
    mycursor.execute(sql_teachers, adr_teachers)
    teachersThisMonth =  mycursor.fetchall()
    if teachersThisMonth is not None:
        teachersThisMonth_number = len(teachersThisMonth)
    else:
        teachersThisMonth_number = 0

    allRes.append(
    {
        "teachers": teachersThisMonth_number
    })



    #דוח מורים שכר

    techers_info = []
    sql_teachers_all = "SELECT * FROM teachers"
    mycursor.execute(sql_teachers_all)
    sql_teachers_all =  mycursor.fetchall()

    
    for row_teachers in sql_teachers_all:
        number_of_lessons_per_teacher = 0
        techer_sum = 0

        sql_teachers_lessons= "SELECT * FROM lessons WHERE TeacherId = %s"
        adr_teachers_lessons = (row_teachers[0], )
        mycursor.execute(sql_teachers_lessons, adr_teachers_lessons)
        teachers_lessons =  mycursor.fetchall()
        if teachers_lessons is not None:
            teachers_lessons_number = len(teachers_lessons)
        else:
            teachers_lessons_number = 0


        if teachers_lessons_number > 0:
            for row_teachers_lessons in teachers_lessons:
                sql_schedule_lessons = "SELECT * FROM schedule WHERE  MONTH(ScheduleDate) = %s AND YEAR(ScheduleDate) = %s AND canceled = 0 AND LessonId = %s"
                adr_schedule_lessons = (target_month, target_year, row_teachers_lessons[0])
                mycursor.execute(sql_schedule_lessons, adr_schedule_lessons)
                scheduleThisMonth_lessons =  mycursor.fetchall()

                if scheduleThisMonth_lessons is not None:
                    scheduleThisMonth_lessons_number = len(scheduleThisMonth_lessons)
                else:
                    scheduleThisMonth_lessons_number = 0
                
                number_of_lessons_per_teacher += scheduleThisMonth_lessons_number 
                techer_sum += row_teachers[5]*scheduleThisMonth_lessons_number


                
        techers_info.append(
        {
            "teacher": row_teachers[2] + ' ' + row_teachers[3],
            "number_of_lessons": number_of_lessons_per_teacher,
            "techer_sum": techer_sum,
            "techer_salary":  row_teachers[5]
        })
    allRes.append(
    {
        "teachers_info": techers_info
    })


    return (allRes)
           

async def delSchedule(id):
    # Returns the current local date
    sql = "DELETE FROM schedule WHERE id = %s"
    adr = (id, )

    mycursor.execute(sql, adr)

    mydb.commit()

    return (mycursor.rowcount, "record delete.")

async def login(username,password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    hex_dig_password = hash_object.hexdigest()
    # Returns the current local date
        # Returns the current local date
    sql = "SELECT * FROM teachers WHERE username = %s AND password = %s" 
    adr = (username, hex_dig_password)
    mycursor.execute(sql, adr)

    record_teacher = mycursor.fetchone()

    if record_teacher is not None:
        num_result_teacher = len(record_teacher)
    else:
        num_result_teacher = 0
    
    if num_result_teacher > 0:


        letters = string.ascii_letters
        rand_string = ''.join(random.choice(letters) for i in range(40))
        token = username + '-' + rand_string
        sql = "UPDATE teachers SET token = %s WHERE username = %s"
        val = (token, username)

        # Execute the SQL query
        mycursor.execute(sql, val)
        # Execute the SQL query
        # Commit the changes
        mydb.commit()
        return "התחברת בהצלחה!",token
    else: 
        return "שם משתמש או סיסמה לא נכונים",0

async def teachersInfoById(id):
    # Returns the current local date
        # Returns the current local date
    sql = "SELECT * FROM teachers WHERE id = %s" 
    adr = (id, )
    mycursor.execute(sql, adr)

    result = mycursor.fetchall()
    # print(len(myresult))
    a = []
    i = 0
    # for row in result:
    #     print(row[1])
    #     a[i] = row
    #     i += 1

    return result

async def teachersInfo():
    # Returns the current local date
        # Returns the current local date
    sql = "SELECT * FROM teachers" 

    mycursor.execute(sql)

    result = mycursor.fetchall()
    # print(len(myresult))
    a = []
    i = 0
    # for row in result:
    #     print(row[1])
    #     a[i] = row
    #     i += 1

    return result

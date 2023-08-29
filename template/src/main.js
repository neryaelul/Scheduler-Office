$(document).ready(function () {
    const keyStorage = localStorage.getItem('key');
    var path = window.location.pathname;
    var page = path.split("/").pop();

    if (keyStorage !== null) {
        // The item exists in localStorage
        console.log('keyStorage exists:', keyStorage);
        const json = {
            "key": keyStorage            
        };
        var settings = {
            "url": "http://127.0.0.1:8000/check/",
            "method": "POST",
            "timeout": 0,
            "headers": {
              "Content-Type": "application/json"
            },
            "data": JSON.stringify(json),
          };
          
          $.ajax(settings).done(function (response) {
            console.log(response);
                
            const sValue = response.res.s;
            const permissionValue = response.res.permission;
            if(permissionValue > 1){
                $('.selection').show();
                $('#show_report_salary').show();
                $('#show_report_general').show();
            }
            
            if(sValue == 1){
                
            }else{
                if(page != "login"){
                    window.location.href = "http://127.0.0.1:8000/login";
                }
            }
                var res = response;

            
          });
        } else {
            if(page != "login"){
                window.location.href = "http://127.0.0.1:8000/login";
            }
            

        }
   

    function daysInMonth (month, year) {
        return new Date(parseInt(year), parseInt(month), 0).getDate();
    }
    function nameDayHE(date){
        const d = new Date(date);
        let day = d.getDay();
        var nDay = "";
        switch (day) {
            case 0:
              nDay = "ראשון"
              break;
            case 1:
              nDay = "שני"
              break;
            case 2:
              nDay = "שלישי"
              break;
            case 3:
              nDay = "רביעי"
              break;
            case 4:
              nDay = "חמישי"
              break;
            case 5:
              nDay = "שישי"
              break;
            case 6:
              nDay = "שבת"
              break;
            default:
                nDay = "ראשון"
          }
          return nDay;

    }
    function RoomColor(room){
        var classCSS = "";
        switch (room) {
            case "red":
              classCSS = "meetRed"
              break;
            case "blue":
              classCSS = "meetBlue"
              break;
            case "green":
              classCSS = "meetGreen"
              break;
            case "orange":
              classCSS = "meetOrange"
              break;
            case "pink":
              classCSS = "meetPink"
              break;
          }
          return classCSS;

    }

    function daysInMonthAppend(m,y){
        days = '';
        var mD = daysInMonth(m,y);
        for (i = 1; i <= mD; i++){
            day =  nameDayHE(y + '-' + m + '-' + i);
            console.log(day);
            if(day == "שישי" || day == "שבת"){
                bg_daysof = "background-color: #f7d9c5;";
            }else{
                bg_daysof = "";
            }
            days += '<div class="date" data-test="ff" style="'+bg_daysof+'" data-day="'+day+'" data-date="' + y + '-' + m + '-' + i + '"><div class="day"><span class="dayNumber">' + i + '</span> <br /><span>' + day + '</span></div></div>';
            
        }

        $('.calendar').html(days);

        
        var response_teachers = '';
        $.ajax({ type: "GET",   
                url: "http://127.0.0.1:8000/info/teachers/",   
                async: false,
                success : function(text)
                {
                    response_teachers = text;
                    // console.log(JSON.stringify(response_teachers));
                    for(let i = 0; i < response_teachers.res.length; i++) {
                        
                        $('#teacher_newLesson').append(`<option value="${response_teachers.res[i][0]} ">${response_teachers.res[i][2]} ${response_teachers.res[i][3]}</option>`);
                    
                    }
                }
        });
         $.ajax({ type: "GET",   
                url: "http://127.0.0.1:8000/info/lessons/",   
                async: false,
                success : function(text)
                {
                    response_lessons = text;
                    $('#newSchedule_lessons').empty();
                    // console.log(JSON.stringify(response_lessons));
                    for(let i = 0; i < response_lessons.res.length; i++) {
                        
                        $('#newSchedule_lessons').append(`<option value="${response_lessons.res[i].id}">${response_lessons.res[i].name} עם ${response_lessons.res[i].teacher}</option>`);
                        
                    }
                }
        });
        $('#loginSend').click(function(){
            const json = {
                "username": $('#username_login').val(),
                "password": $('#password_login').val(),
                
            };
            var settings = {
                "url": "http://127.0.0.1:8000/login/",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify(json),
              };
              
              $.ajax(settings).done(function (response) {
                console.log(response);
                localStorage.setItem('key', response.res[1]);
                
                alert(response.res[0]);
                window.location.href = "/";

                var res = response;
                
              });
              //window.location.assign(location.href);
            //   window.location.assign(window.location.href + "&next");
        });

        $.ajax({ type: "GET",   
        url: "http://127.0.0.1:8000/info/students/",   
        async: false,
        success : function(text)
            {
                    $('#newSchedule_students').empty();
                    response_students = text;
                    // console.log(JSON.stringify(response_students));
                    for(let i = 0; i < response_students.res.length; i++) {
                        
                        $('#newSchedule_students').append(`<option value="${response_students.res[i].id}">${response_students.res[i].name}</option>`);
                    
                    }
                }
        });
        $('#exit').click(function(){
            localStorage.removeItem("key");
            window.location.assign(window.location.href);
        });
        $('#show_report_salary').click(function(){
            var m = $('#m').val();
            var y = $('#y').val();
            const json = {
                "key": localStorage.getItem('key'),
                "month": m,
                "year": y
                
            };
            var settings = {
                "url": "http://127.0.0.1:8000/report",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify(json),
              };
              
              $.ajax(settings).done(function (response) {
                // console.log(response);
                
                // alert(response.res[1]);
                var data = response;
               
                        
                    
                var report = '<div class="miniBox">';
                report += '<p>' + m + '/' + y + '</p>';
                report += '<table><thead><tr>';
                report += '<th>מורה</th>';
                report += '<th>מספר שיעורים החודש</th>';
                report += '<th>שכר שעתי</th>';
                report += '<th>שכר החודש</th></tr></thead><tbody>';

                // Add each teacher to the second table.
                for (var i = 0; i < data.res[4].teachers_info.length; i++) {
                    report += '<tr>';
                    report += '<td>' + data.res[4].teachers_info[i].teacher + '</td>';
                    report += '<td>' + data.res[4].teachers_info[i].number_of_lessons + '</td>';
                    report += '<td>' + data.res[4].teachers_info[i].techer_salary + '</td>';
                    report += '<td>' + data.res[4].teachers_info[i].techer_sum + '</td>';
                   
                    
                    report += '</tr>';
                }

                report += '</tbody></table></div>';
                $('#report_general').html(report);
              });
              $('#report_general').show();
              $('.bgDARK').show();
              
            //   window.location.assign(window.location.href + "&next");
        });

        $('#show_report_general').click(function(){
            var m = $('#m').val();
            var y = $('#y').val();
            const json = {
                "key": localStorage.getItem('key'),
                "month": m,
                "year": y
            };
            var settings = {
                "url": "http://127.0.0.1:8000/report",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify(json),
              };
              
              $.ajax(settings).done(function (response) {
                // console.log(response);
                
                // alert(response.res[1]);
                var data = response;
               
                        
                    
                var report = '<div class="miniBox">';
                report += '<p>' + m + '/' + y + '</p>';
                report +='<table><thead><tr>';
                report += '<th>שיעורים קיימים</th>';
                report += '<th>שיעורים שבוטלו</th>';
                report += '<th>תלמידים חדשים</th>';
                report += '<th>מורים חדשים</th></tr></thead><tbody><tr>';
                report += '<td>' + data.res[0].scheduleNotCanceled + '</td>';
                report += '<td>' + data.res[1].scheduleThisMonthCanceled + '</td>';
                report += '<td>' + data.res[2].students + '</td>';
                report += '<td>' + data.res[3].teachers + '</td></tr></tbody></table>';

                // Generate the second table.
                // report += '<table><thead><tr>';
                // report += '<th>מורה</th>';
                // report += '<th>מספר שיעורים החודש</th>';
                // report += '<th>שכר החודש</th></tr></thead><tbody>';

                // // Add each teacher to the second table.
                // for (var i = 0; i < data.res[4].teachers_info.length; i++) {
                //     report += '<tr>';
                //     report += '<td>' + data.res[4].teachers_info[i].teacher + '</td>';
                //     report += '<td>' + data.res[4].teachers_info[i].number_of_lessons + '</td>';
                //     report += '<td>' + data.res[4].teachers_info[i].techer_sum + '</td>';
                //     report += '</tr>';
                // }

                report += '</tbody></table></div>';
                $('#report_general').html(report);
              });
              $('#report_general').show();
              $('.bgDARK').show();
              
            //   window.location.assign(window.location.href + "&next");
        });
        $('#newTeacherSendForm').click(function(){
            const json = {
                "FirstName": $('#firstname_newTeacher').val(),
                "LastName": $('#lastname_newTeacher').val(),
                "id": $('#id_newTeacher').val(),
                "address": $('#address_newTeacher').val(),
                "SalaryPerHour": $('#SalaryPerHour_newTeacher').val(),
                "username": $('#username_newTeacher').val(),
                "password": $('#password_newTeacher').val(),
                "permission": $('#permission_newTeacher').val(),
                "key": localStorage.getItem('key')

            };
            var settings = {
                "url": "http://127.0.0.1:8000/add/teachers/",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify(json),
              };
              
              $.ajax(settings).done(function (response) {
                // console.log(response);
                alert(response.res[1]);
                var res = response;
              });
              window.location.assign(location.href);
            //   window.location.assign(window.location.href + "&next");
        });
        $('#newStudentSendForm').click(function(){
            const json = {
                "FirstName": $('#firstname_newStudent').val(),
                "LastName": $('#lastname_newStudent').val(),
                "id": $('#id_newStudent').val(),
                "address": $('#address_newStudent').val(),
                "key": localStorage.getItem('key')
            };
            var settings = {
                "url": "http://127.0.0.1:8000/add/students/",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify(json),
              };
              
              $.ajax(settings).done(function (response) {
                // console.log(response);
                alert(response.res[1]);
                var res = response;
              });
              window.location.assign(location.href);
            //   window.location.assign(window.location.href + "&next");
        });
        $('#newLessonSendForm').click(function(){
            const json = {
                "name": $('#name_newLesson').val(),
                "price": $('#price_newLesson').val(),
                "TeacherId": $('#teacher_newLesson').val(),
                "RoomColor": $('#room').val(),
                "key": localStorage.getItem('key')
            };
            var settings = {
                "url": "http://127.0.0.1:8000/add/lessons/",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify(json),
              };
              
              $.ajax(settings).done(function (response) {
                // console.log(response);
                alert(response.res[1]);
                var res = response;
              });
              window.location.assign(location.href);
            //   window.location.assign(window.location.href + "&next");
        });
        $('.date').click(function(){
            
            var dayName = this.getAttribute("data-day");
            if(dayName == "שישי" || dayName == "שבת"){
                alert("יום שישי ושבת אינם זמני הפעילות של הבית ספר");
            }else{
                    
                
                var date = this.getAttribute("data-date");
                $('.hourMaster').attr('data-date', date);
                $(".ThisDateHour").remove();

                $('.dayResOut').show();
                $('.bgDARK').show();
                console.log(date);
                var response = '';
                    const json = {
                        "key": keyStorage,
                        "day":date,
                    };
                    var settings = {
                        "url": "http://127.0.0.1:8000/info/day/",
                        "method": "POST",
                        "timeout": 0,
                        "headers": {
                            "Content-Type": "application/json"
                        },
                        "data": JSON.stringify(json),
                        };
                        
                        $.ajax(settings).done(function (response) {
                        for(let i = 0; i < response.res.length; i++) {
                            console.log(response.res[i].name)
                            dateRes = response.res[i].date;
                            nameRes = response.res[i].name;
                            RoomColorRes = response.res[i].RoomColor;
                            StudentNameRes = response.res[i].student;
                            teacherNameRes = response.res[i].teacher;
                            idRec = response.res[i].id;
                            let timeDateRes = dateRes.split('T')[1];  // Splits the string into date and time, and gets the time
                            let hourDateRes = timeDateRes.split(':')[0];
                            $('div[data-hour="'+hourDateRes+':00"]').append('<div class="'+RoomColor(RoomColorRes)+' tooltip ThisDateHour" data-idrec="'+idRec+'" id="r'+idRec+'">'+nameRes+' - ' +teacherNameRes+' ('+StudentNameRes+')<span class="tooltiptext">ביטול שיעור</span></div>');
                            $('#r' + idRec).click(function(){
                                if(!confirm('אתה בטוח שברצונך לבטל את השיעור?')) {
                                    event.preventDefault();
                                }else{
                                var idrec = this.getAttribute("data-idrec");
                                const json = {
                                    "id": idrec,
                                    "key": localStorage.getItem('key')
                                };
                                    var settings = {
                                        "url": "http://127.0.0.1:8000/update/schedule/",
                                        "method": "POST",
                                        "timeout": 0,
                                        "headers": {
                                        "Content-Type": "application/json"
                                        },
                                        "data": JSON.stringify(json),
                                    };
                                    
                                    $.ajax(settings).done(function (response) {
                                        // console.log(response);
                                        alert(response.res);
                                        var res = response;
                                        window.location.assign(location.href);
                                    });
                                }
                                
                            });
                            //for(let j = 0; j < response.res[i].length; j++) {
                                //  console.log(response.res[i][j]);
                            //}
                        }
                        });
                    
                    }
        });
                
        
                
                

        
        $('.hourMaster').click(function(){
            $("#newSchedule_times").empty();
            var dateSelected = this.getAttribute("data-date");
            var dateSelectedFix = dateSelected.replaceAll("-", "/");
            var hourSelected = this.getAttribute("data-hour");



            var currentDate = new Date();
            var partsDate = dateSelected.split('-');
            var checkDate = new Date(partsDate[0], partsDate[1] - 1, partsDate[2]);

            if (checkDate < currentDate) {
                alert("לא ניתן לקבוע שיעורים בתאריך עבר");
            } else {

                

                $('#dateForNewSchedule').attr('data-schedule', dateSelected + ' ' + hourSelected);
                var scheduleTimes = `בתאריך ${dateSelectedFix} ובשעה ${hourSelected} `
                console.log(scheduleTimes);
                $('#newSchedule_times').append(scheduleTimes);
                $('#newScheduleForm').show();

                $('.dayResOut').hide();
            }
        });
        $('#newScheduleSend').click(function(){
            var dateForNewSchedule = $('#dateForNewSchedule').data('schedule');
            


            // Check if the date you want to check is before the current date
            
                const json = {
                    "LessonId": $('#newSchedule_lessons').val(),
                    "ScheduleDate": dateForNewSchedule,
                    "StudentId": $('#newSchedule_students').val(),
                    "key": localStorage.getItem('key')
                };
                var settings = {
                    "url": "http://127.0.0.1:8000/add/schedule",
                    "method": "POST",
                    "timeout": 0,
                    "headers": {
                    "Content-Type": "application/json"
                    },
                    "data": JSON.stringify(json),
                };
                
                $.ajax(settings).done(function (response) {
                    // console.log(response);
                    alert(response.res);
                    var res = response;
                    window.location.assign(location.href);
                });
            
        });

        $('.bgDARK').click(function(){
            $('.dayResOut').hide();
            $('#newStudentForm').hide();
            $('#newLessonForm').hide();
            $('#newTeacherForm').hide();
            $('#newScheduleForm').hide();
            $('#report_salary').hide();
            $('#report_general').hide();
            $('.bgDARK').hide();

        });
       

    }
    
    $('#newStudent').click(function(){
        $('#newStudentForm').show();
        $('.bgDARK').show();
    });
   
    $('#newLesson').click(function(){
        $('#newLessonForm').show();
        $('.bgDARK').show();
    });
    
    $('#newTeacher').click(function(){
        $('#newTeacherForm').show();
        $('.bgDARK').show();

    });
   
    
    const date = new Date();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();
    var m = month
    var y = year;
    daysInMonthAppend(m,y);

    $('#m').val(m);
   
    


    $( "#m" ).on( "change", function() {
        
        var m = $('#m').val();
        var y = $('#y').val();
        daysInMonthAppend(m,y)
    } );

    $( "#y" ).on( "change", function() {
        
        var m = $('#m').val();
        var y = $('#y').val();
        daysInMonthAppend(m,y)
    } );
});

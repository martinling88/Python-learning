#首先，需要知道时间。
#其次，需要知道课程
#最后，补丁时间，typo
from datetime import datetime
m_hour=datetime.now().hour
m_minute=datetime.now().minute
m_day=datetime.now().weekday()
time=(m_hour*60)+m_minute
def time_left(time,next_class,next_subject,next_location):
    out = next_class-time
    hours= out // 60
    minutes = out % 60
    print("现在没课！离下堂课还有",f" {hours}h {minutes}min")
    print("下一堂课:",next_subject)
    print("地点:",next_location)
def time_nextday(time_next):
    next=1440-time+time_next
    hours= next // 60
    minutes = next % 60
    print("自由！但距离下堂课还有",f" {hours}h {minutes}min")

if m_day == 0:
    if time >= 480 and time <600:
        print("ICT（lab），Computer Lab")
    elif time >= 720 and time <840:
        print("Physics (Lecture) ,Lecture Hall" )
    elif time >= 930 and time < 1020:
        print("ICT (lecture) , Auditorium")
    else:
        if  time <600:
           time_left(time,480,"ICT（lab）","Computer Lab")
        elif time >= 600 and time <720:
            time_left(time,720,"Physics (Lecture)","Lecture Hall")
        elif time >= 720 and time < 930:
            time_left(time,930,"ICT (lecture)"," Auditorium")
        else:
            time_nextday(600)
elif m_day == 1:


    if time >=600 and time <720:
        print("Physics (tutorial)，Tutorial Room")
    elif time >= 780 and time <870:
        print("ICT (lecture) , Auditorium")

    else:
        if  time <720:
           time_left(time,600,"Physics (tutorial)","Tutorial Room")
        elif time >= 720 and time <780:
            time_left(time,780,"ICT (lecture)","Auditorium")
        else:
             time_nextday(480)

elif m_day == 2:

    if time >= 480 and time <600:
        print("Physics (lab),Physics Lab")

    else:
        if  time <600:
           time_left(time,600,"Physics (lab)","Physics Lab")

        else:
             time_nextday(480)

elif m_day == 3:

    if time >= 480 and time <600:
        print("Physics (lecture),Lecture Hall")
    elif time >= 660 and time <780:
        print("ICT（lab），Computer Lab")
    else:
        if time <600:
            time_left(time,600,"Physics (lecture)","Lecture Hall")
        elif time >=600 and time < 660:
            time_left(time,660,"ICT（lab）","Computer Lab")
        else:
             time_nextday(840)

elif m_day == 4 :

    if time >= 840 and time < 960:
        print("Physics (Tutorial) ,Tutorial Room")

    else:
        if  time < 960:
           time_left(time,960,"Physics (Tutorial)","Tutorial Room")

        else:
            print("自由！")
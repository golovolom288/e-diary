from datacenter.models import Chastisement, Mark, Commendation, Schoolkid, Lesson
import random


def get_schoolkid(kid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        return None
    except Schoolkid.MultipleObjectsReturned:
        return "Найдено больше одного имени"


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks: mark.points = 5; mark.save()


def create_commendation(kid_name, subject):
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]
    try:
        schoolkid = get_schoolkid(kid_name)
        if not schoolkid:
            print("Ученик не найден")
            return None
        elif schoolkid == "Найдено больше одного имени":
            print("Найдено больше одного ученика")
            return None
        lessons = Lesson.objects.filter(group_letter="А", year_of_study=6, subject__title=subject)
        commendation = Commendation.objects.filter(schoolkid=schoolkid)
        commendation.create(text=random.choice(commendations), created=lessons[0].date, schoolkid=schoolkid, subject=lessons[0].subject,
                            teacher=lessons[0].teacher)
    except:
        print("ошибка")




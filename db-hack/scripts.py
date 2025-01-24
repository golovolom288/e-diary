from datacenter.models import Chastisement, Mark, Commendation, Schoolkid, Lesson
import random


def get_schoolkid(kid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        return
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned('Найдено несколько учеников, уточните ФИО')


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
        lesson = Lesson.objects.filter(group_letter=schoolkid.group_letter, year_of_study=schoolkid.year_of_study, subject__title=subject).order_by("date").first()
        Commendation.objects.create(text=random.choice(commendations), created=lesson.date, schoolkid=schoolkid, subject=lesson.subject,
                            teacher=lesson.teacher)
    except:
        print("ошибка")




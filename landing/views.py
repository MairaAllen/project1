from django.shortcuts import render
from .models import *  # импортирование модели
from .forms import LeadForm


# любой вид(функция) принимает первым атрибутом request, а иначе - запрос
# так как интернет работает на принципе request <--> response

def home(request):
    courses = Course.objects.all()  # запрос в базу данных
    # print(courses[0].description)
    return render(request, 'home.html', {'courses': courses})  # отправка в html


def about(request):
    teachers = Teacher.objects.all()
    return render(request, 'about.html', {'teachers': teachers})


def course(request, pk):
    # запрос на получение определенного объекта
    # .get - метод, который делает запрос в базу данных и возвращает первый подошедший объект.

    # Обязательным аспектом является передача 'условие', то есть нужно
    # передать информацию, которая будет сравниваться с выбранным полем

    # get(имя поля = значение, полученное с url(запроса))
    # значение в БД будет сравниваться с каждым объектом
    # и при первом совпадении вернет этот объект

    course_data = Course.objects.get(pk=pk)
    form = LeadForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        # commit=False приостановка сохранения данных в БД идущих с формы
        is_success = True
        # instance = {id:1, name:'asdf', }
        instance.course = course_data
        instance.save()
        form = LeadForm()
    # print(course_data.price)
    # print(course_data.description)
    return render(request, 'course.html', {'course': course_data, 'form': form, 'is_success': is_success})

def check_leads(request):
    leads = Lead.objects.all()
    return render(
        request,
        'leads.html',
        {'leads':leads}
    )

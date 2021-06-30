from django.shortcuts import render,redirect
from .models import Team
def home(request):
    	
	t1 = Team.objects.get(num = '1')
	t2 = Team.objects.get(num = '2')
	t3 = Team.objects.get(num = '3')
	t4 = Team.objects.get(num = '4')
	t5 = Team.objects.get(num = '5')
	t6 = Team.objects.get(num = '6')
	t7 = Team.objects.get(num = '7')
	t8 = Team.objects.get(num = '8')
	t9 = Team.objects.get(num = '9')
	t10 = Team.objects.get(num = '10')
	t11 = Team.objects.get(num = '11')
	t12 = Team.objects.get(num = '12')
	t13 = Team.objects.get(num = '13')
	t14 = Team.objects.get(num = '14')

	context = {

		't1':t1,
		't2':t2,
		't3':t3,
		't4':t4,
		't5':t5,
		't6':t6,
		't7':t7,
		't8':t8,
		't9':t9,
		't10':t10,
		't11':t11,
		't12':t12,
		't13':t13,
		't14':t14,

	}

	return render(request,'system/home.html',context)

def admin_page(request):

	if request.method == "POST":
		title = request.POST.get('title')
		num = request.POST.get('num')
	else:
		num = None
		title = None

	if num is not None:
		a = Team.objects.get(num = f'{num}')
		if title is not None:
			a.title = title
			a.save()

	return render(request,'system/admin page.html')

def reset(request):
	
	for i in range(1,15):
		a = Team.objects.get(num = f'{i}')
		a.title = i
		a.save()

	return redirect('admin_page')



def rounds(request):

	t1 = Team.objects.get(num = '1')
	t2 = Team.objects.get(num = '2')
	t3 = Team.objects.get(num = '3')
	t4 = Team.objects.get(num = '4')
	t5 = Team.objects.get(num = '5')
	t6 = Team.objects.get(num = '6')
	t7 = Team.objects.get(num = '7')
	t8 = Team.objects.get(num = '8')
	t9 = Team.objects.get(num = '9')
	t10 = Team.objects.get(num = '10')
	t11 = Team.objects.get(num = '11')
	t12 = Team.objects.get(num = '12')
	t13 = Team.objects.get(num = '13')
	t14 = Team.objects.get(num = '14')

	context = {

		't1':t1,
		't2':t2,
		't3':t3,
		't4':t4,
		't5':t5,
		't6':t6,
		't7':t7,
		't8':t8,
		't9':t9,
		't10':t10,
		't11':t11,
		't12':t12,
		't13':t13,
		't14':t14,

	}

	return render(request,'system/rounds.html',context)


def shahar(request):

	t1 = Team.objects.get(num = '1')
	t2 = Team.objects.get(num = '2')
	t3 = Team.objects.get(num = '3')
	t4 = Team.objects.get(num = '4')
	t5 = Team.objects.get(num = '5')
	t6 = Team.objects.get(num = '6')
	t7 = Team.objects.get(num = '7')
	t8 = Team.objects.get(num = '8')
	t9 = Team.objects.get(num = '9')
	t10 = Team.objects.get(num = '10')
	t11 = Team.objects.get(num = '11')
	t12 = Team.objects.get(num = '12')
	t13 = Team.objects.get(num = '13')
	t14 = Team.objects.get(num = '14')

	context = {

		't1':t1,
		't2':t2,
		't3':t3,
		't4':t4,
		't5':t5,
		't6':t6,
		't7':t7,
		't8':t8,
		't9':t9,
		't10':t10,
		't11':t11,
		't12':t12,
		't13':t13,
		't14':t14,

	}

	return render(request,'system/shahar.html',context)


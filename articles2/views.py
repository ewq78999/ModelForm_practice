from django.shortcuts import render, redirect
from .models import Article2
from .forms import Article2Form


# Create your views here.

def index(request):
    articles2 = Article2.objects.all()

    context = {
        'articles2' : articles2,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    article2 = Article2.objects.get(id=id)

    context = {
        'article2' : article2,
    }

    return render(request, 'detail.html', context)


def create(request):
    # POST 라면
    if request.method == 'POST':
        # form 정의하고
        form = Article2Form(request.POST)
        # form이 가치 있다면(o) / 가치 없으면(x) else로 pass
        if form.is_valid():
            # form을 저장하고 그 값을 article2에 저장
            article2 = form.save()
            # detail 페이지로 redirect
            return redirect('articles2:detail', id=article2.id)


    # GET(or 잘못된 form) 이라면
    else:
        # 비어있는 form 만들고
        form = Article2Form()

    # context에 담은 다음
    context = {
        'form' : form,
    }

    #create.html 랜더링(새 창)
    return render(request, 'create.html', context)


def delete(request, id):
    # 정의하고
    article2 = Article2.objects.get(id=id)
    # 삭제하고
    article2.delete()
    # 다시 index로 redirect
    return redirect('articles2:index')

def update(request, id):
    # article2의 object 정의하고
    article2 = Article2.objects.get(id=id)

    # POST 형식이면
    if request.method == "POST":
        # 기존의 값에서 새로운 정보가 추가된 값으로 정의
        form = Article2Form(request.POST, instance=article2)

        # form이 o라면 계속 진행 / x 라면 else가 아닌 하단의 context로 연결
        if form.is_valid():
            form.save()
            # 같은 id의 detail로 redirect
            return redirect('articles2:detail', id=id)

    # GET 형식이거나 잘못된 POST 형식일 때
    else:
        # 기존의 값으로 정의
        form = Article2Form(instance=article2)

    context = {
        'form' : form
    }
    # vanila가 나오게 설정
    return render(request, 'update.html', context)

    # 일단 GET&POST 돌리면서 GET은 else 문에서 1차로 거르고 
    # 잘못된 POST는 invalid에서 걸러서
    # context = {'form' : form } 으로 내려 기존값으로 원복시킨다.
    # invalid도 통과한 정상적 POST라면
    # save한 다음 같은 id의 detail로 return redirect 진행한다.
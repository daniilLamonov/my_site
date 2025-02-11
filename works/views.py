from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from works.models import Work


# Create your views here.
def work_list(request):
    works = Work.objects.all()
    paginator = Paginator(works, 2)
    page = request.GET.get('page')
    try:
        works = paginator.page(page)
    except PageNotAnInteger:
        works = paginator.page(1)
    except EmptyPage:
        works = paginator.page(paginator.num_pages)
    return render(request, 'works/work_list.html', {'works': works})
def work_detail(request, slug):
    work = get_object_or_404(Work, slug=slug)
    return render(request, 'works/work_detail.html', {'work': work})

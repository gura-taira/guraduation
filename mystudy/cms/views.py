from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from cms.models import Affair


def affair_list(request):
    """事件の一覧"""
    affairs = Affair.objects.all().order_by('-id')
    return render(request,
                  'cms/affair_list.html',  # 使用するテンプレート
                  {'affairs': affairs})  # テンプレートに渡すデータ


def affair_detail(request, affair_id=None):
    """事件の詳細"""
    detail = get_object_or_404(Affair, pk=affair_id)

    return render(request, 'cms/affair_detail.html', {'detail': detail})

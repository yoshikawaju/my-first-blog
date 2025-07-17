from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def post_list(request):
    # ここにビューのロジックを記述します
    # 例えば、return render(request, 'blog/post_list.html', {})
    return render(request, 'blog/post_list.html', {})
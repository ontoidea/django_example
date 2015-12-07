from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import WriteForm
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    post_list = Post.objects.all().order_by('-created_date')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def content(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/content.html', {'post': post})


@login_required
def write(request):
    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            
            p = Post(author=request.user,subject=subject, content=content, created_date=timezone.now())
            p.save()
            
            #return HttpResponseRedirect('/blog/' + str(p.id))
            return HttpResponseRedirect(reverse('blog:content', args=(p.id,)))
    
    else:
        form = WriteForm()
        
    return render(request, 'blog/write.html', {'form': form})
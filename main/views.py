
from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm, ComentForm,PerfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .decorador import unauthenticated_user, allowed_users


#@unauthenticated_user
def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()

    
        

    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "title": "Meus foruns"
    }
    return render(request, "forums.html", context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form2 = ComentForm()
    form2.save(commit=False)
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)
    
    if "comment-form" in request.POST:
        
        #comment = request.POST.get("comment")
        r = request.POST.get("content1")
        print(r)
        #print(comment+' '+'comment')
        
        if form2.is_valid():
            print("\n\n its valid")
            #new_post = form2.save(commit=False)
            
        else:
            print("form invalido")
        new_comment, created = Comment.objects.get_or_create(user=author, content=r)
        post.comments.add(new_comment.id)


    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        commenr_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=commenr_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
        comment_obj.replies.add(new_reply.id)


    context = {
        "post":post,
        "title": post.title,
        "form":form2
    }
    update_views(request, post)

    return render(request, "detail.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    context = {
        "posts":posts,
        "forum": category,
        "title": "Postagens"
    }

    return render(request, "posts.html", context)



def perfil_usuario(request):
    
    #request.user.author.id
    context = {}
    #instance = get_object_or_404(Author, id=request.user)
    author = Author.objects.get(user=request.user)
    print(author)
    form = PerfilForm(instance=author)
    
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES,instance=author)

        print("post ---")
        if form.is_valid():
            print("valid ---")
            update_profile = form.save(commit=False)
            

        
            
            update_profile.save()

            
            return redirect("home")


    
    context.update({
        "form": form,
        "title": "Update Profile",
    })
    
    return render(request, 'perfil_user.html', context)

@login_required
def create_post(request):
    context = {}
    form1 = PostForm(request.POST ,request.FILES)
    if request.method == "POST":
        if form1.is_valid():
            print("\n\n its valid",form1)
            author = Author.objects.get(user=request.user)
            new_post = form1.save(commit=False)
            new_post.user = author
            new_post.save()
            form1.save_m2m()
            print(form1)
            return redirect("home")
    context.update({
        "form": form1,
        "title": "Criar uma nova postagem"
    })
    return render(request, "create_post.html", context)

def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "10 ultimas postagens"
    }

    return render(request, "latest-posts.html", context)

def search_result(request):

    return render(request, "search.html")
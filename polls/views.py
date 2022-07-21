from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse


def register(request):
    context = {
        'title': 'Registration',
        'action_registratoon': 'active'
    }
    return render(request, 'polls/register.html', context=context)


def login(request):
    context = {
        'title': 'Login',
        'active_login': 'active'
    }
    # return render(request, context=context)


def index(request):
    status = request.user.is_staff
    context = {
        'title': 'This is home page',
        'active_home': 'active',
        'some_list': [1, 2, 3, 4, 5, 6, 7],
        'qw': True,
        'qw2': False,
        'status': status
    }
    return render(request, 'polls/index.html', context=context)


def index2(request):
    context = {
        'title': 'Homepage 2',
        'active_home': 'active',
        'active_homepage2': 'active'
    }
    return render(request, 'polls/index-alt2.html', context=context)


def index3(request):
    context = {
        'title': 'Homepage 3',
        'active_home': 'active',
        'active_homepage3': 'active'
    }
    return render(request, 'polls/index-alt3.html', context=context)


def index4(request):
    context = {
        'title': 'Parallax slider',
        'active_home': 'active',
        'active_homepage4': 'active'
    }
    return render(request, 'polls/index-alt4.html', context=context)


def index_landingpage(request):
    context = {
        'title': 'Landing page',
        'active_home': 'active',
        'active_homepage_landingpage': 'active'
    }
    return render(request, 'polls/index-landingpage.html', context=context)


def typography(request):
    context = {
        'title': 'Typography',
        'active_features': 'active',
        'active_typography': 'active'
    }
    return render(request, 'polls/typography.html', context=context)


def components(request):
    context = {
        'title': 'Components',
        'active_features': 'active',
        'active_components': 'active'
    }
    return render(request, 'polls/components.html', context=context)


def icons(request):
    context = {
        'title': 'Icons',
        'active_features': 'active',
        'active_icons': 'active'
    }
    return render(request, 'polls/icons.html', context=context)


def icon_variations(request):
    context = {
        'title': 'Icon variations',
        'active_features': 'active',
        'active_icon_var': 'active'
    }
    return render(request, 'polls/icon-variations.html', context=context)


def about(request):
    context = {
        'title': 'About us',
        'active_pages': 'active',
        'active_about': 'active'
    }
    return render(request, 'polls/about.html', context=context)


def faq(request):
    context = {
        'title': 'FAQ',
        'active_pages': 'active',
        'active_faq': 'active'
    }
    return render(request, 'polls/faq.html', context=context)


def team(request):
    context = {
        'title': 'Team',
        'active_pages': 'active',
        'active_team': 'active'
    }
    return render(request, 'polls/team.html', context=context)


def services(request):
    context = {
        'title': 'Services',
        'active_pages': 'active',
        'active_services': 'active'
    }
    return render(request, 'polls/services.html', context=context)


def pricingbox(request):
    context = {
        'title': 'Pricing boxes',
        'active_pages': 'active',
        'active_pricingbox': 'active'
    }
    return render(request, 'polls/pricingbox.html', context=context)


def err_404(request):
    context = {
        'title': '404',
        'active_pages': 'active',
        'active_404': 'active'
    }
    return render(request, 'polls/404.html', context=context)


def portfolio2(request):
    context = {
        'title': 'Portfolio 2 columns',
        'active_portfolio': 'active',
        'active_portfolio2': 'active'
    }
    return render(request, 'polls/portfolio-2cols.html', context=context)


def portfolio3(request):
    context = {
        'title': 'Portfolio 3 columns',
        'active_portfolio': 'active',
        'active_portfolio3': 'active'
    }
    return render(request, 'polls/portfolio-3cols.html', context=context)


def portfolio4(request):
    context = {
        'title': 'Portfolio 4 columns',
        'active_portfolio': 'active',
        'active_portfolio4': 'active'
    }
    return render(request, 'polls/portfolio-4cols.html', context=context)


def portfolio_detail(request):
    context = {
        'title': 'Portfolio detail',
        'active_portfolio': 'active',
        'active_detail': 'active'
    }
    return render(request, 'polls/portfolio-detail.html', context=context)


def blog_left_sidebar(request):
    context = {
        'title': 'Blog left sidebar',
        'active_blog': 'active',
        'active_blog_left': 'active'
    }
    return render(request, 'polls/blog-left-sidebar.html', context=context)


def blog_right_sidebar(request):
    context = {
        'title': 'Blog right sidebar',
        'active_blog': 'active',
        'active_blog_right': 'active'
    }
    return render(request, 'polls/blog-right-sidebar.html', context=context)


def blog_fullwidth(requst):
    context = {
        'title': 'Blog fullwidth',
        'active_blog': 'active',
        'active_fullwidth': 'active'
    }
    return render(requst, 'polls/blog-fullwidth.html', context=context)


def post_left_sidebar(request):
    context = {
        'title': 'Post left sidebar',
        'active_blog': 'active',
        'active_post_left': 'active'
    }
    return render(request, 'polls/post-left-sidebar.html', context=context)


def post_right_sidebar(request):
    context = {
        'title': 'Post right sidebar',
        'active_blog': 'active',
        'active_post_right': 'active'
    }
    return render(request, 'polls/post-right-sidebar.html', context=context)


def contact(request):
    context = {
        'title': 'Contact',
        'active_contact': 'active'
    }
    return render(request, 'polls/contact.html', context=context)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'polls/register.html'
    succes_url = reverse_lazy
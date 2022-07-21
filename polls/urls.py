from django.urls import path

from .views import (
    index,
    index2,
    index3,
    index4,
    index_landingpage,
    typography,
    components,
    icons,
    icon_variations,
    about,
    faq,
    team,
    services,
    pricingbox,
    err_404,
    portfolio2,
    portfolio3,
    portfolio4,
    portfolio_detail,
    blog_left_sidebar,
    blog_right_sidebar,
    blog_fullwidth,
    post_left_sidebar,
    post_right_sidebar,
    contact,
    register,
    login
    # detail
)

# urlpatterns = [
#     path("", index, name='index'),
#     path('<str:question_id>/', detail, name='detail')
#
# ]

urlpatterns = [
    path("", index, name='index'),
    path("home2/", index2, name='index2'),
    path("home3/", index3, name='index3'),
    path("home4/", index4, name='index4'),
    path("landing_page/", index_landingpage, name='index_landingpage'),
    path("typography/", typography, name='typography'),
    path("components/", components, name='components'),
    path("icons/", icons, name='icons'),
    path("icon_variations/", icon_variations, name='icon_variations'),
    path("about/", about, name='about'),
    path("faq/", faq, name='faq'),
    path("team/", team, name='team'),
    path("services/", services, name='services'),
    path("pricingbox/", pricingbox, name='pricingbox'),
    path("404/", err_404, name='404'),
    path("portfolio2/", portfolio2, name='portfolio2'),
    path("portfolio3/", portfolio3, name='portfolio3'),
    path("portfolio4/", portfolio4, name='portfolio4'),
    path("portfolio/detail/", portfolio_detail, name='portfolio_detail'),
    path("blog/left/sidebar/", blog_left_sidebar, name='blog_left_sidebar'),
    path("blog/right/sidebar/", blog_right_sidebar, name='blog_right_sidebar'),
    path("blog/fullwidth/", blog_fullwidth, name='blog_fullwidth'),
    path("post/left_sidebar/", post_left_sidebar, name='post_left_sidebar'),
    path("post/right_sidebar/", post_right_sidebar, name='post_right_sidebar'),
    path("contact/", contact, name='contact'),
    path("login/", login, name='login'),
    path("registration/", register, name='register'),
]
#
# li class="regist">
#                           <a href="{% url 'register' %}"> Регистрация <a/>
#                       </li>

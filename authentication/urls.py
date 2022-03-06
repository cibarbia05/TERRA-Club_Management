from django.urls import path

from authentication import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('authentication_actions/', views.authentication_actions, name='authentication_actions'),
    path('learn_more/', views.learn_more, name='learn_more'),
    path('faq/', views.faq, name='faq'),
    path('support/', views.support, name='support'),
    path('signin/', views.sign_in, name='sign_in'),
    path('register_info/', views.register_info, name='register_info'),
    path('register/', views.register, name='register'),
    path('user_page/', views.sign_in, name='user_page'),
    path('member_page/', views.sign_in, name='member_page'),
    path('manager_page/', views.sign_in, name='manager_page'),
    path('manager_member_page/', views.main_page, name='manager_member_page'),
    path('set_account_password_email/<str:email>', views.set_account_password_email, name='set_account_password_email'),

    path('set_account_password/<uidb64>/<token>/<user_email>/',
         views.set_account_password,
         name="set_account_password"),
    path('logout/', views.logout, name='logout'),
    #
    # path('reset_password_sent/',
    #      auth_views.PasswordResetDoneView.as_view(template_name="authentication/password_reset_sent.html"),
    #      name="password_reset_done"),
    #
    # path('reset/<uidb64>/<token>/<user_email>',
    #      views.reset_password,
    #      name="reset_password"),
    #
    # path('reset_password_complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name="authentication/password_reset_done.html"),
    #      name="password_reset_complete"),
]
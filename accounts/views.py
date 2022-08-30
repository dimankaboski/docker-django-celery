from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, FormView
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.urls import reverse

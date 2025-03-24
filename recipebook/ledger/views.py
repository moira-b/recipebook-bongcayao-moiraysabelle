from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect

from .models import Recipe, RecipeImage
from .forms import RecipeForm, AddImageForm

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipesList.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe.html"
    redirect_field_name = ''

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipeForm.html'
    form_class = RecipeForm

class RecipeImageCreateView(CreateView):
    model = RecipeImage
    template_name = 'recipeImageUpload.html'
    form_class = AddImageForm

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = AddImageForm()
        ctx['image_in_Recipe'] = Recipe.objects.get(pk=pk)
        return ctx
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            ri = RecipeImage()
            ri.image = request.FILES.get('image')
            ri.image_in_Recipe = Recipe.objects.get(pk=pk)
            ri.save()

            return redirect(reverse('ledger:recipe', args=[pk]))
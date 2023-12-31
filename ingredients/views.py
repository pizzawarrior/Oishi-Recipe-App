from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import IngredientsForm
from .models import Ingredients
from recipes.models import Recipe


@login_required(login_url="/accounts/login/")
def add_ingredients(request):
    if request.method == 'POST':
        form = IngredientsForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('show_recipe')
            return redirect('recipe_list')
    else:
        form = IngredientsForm()
    context = {'form': form}
    return render(request, 'ingredients/create.html', context)




# # TRY TO REDIRECT TO ATTACH INGREDIENTS TO SPECIFIC RECIPE
# def add_ingredients(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     if request.method == 'POST':
#         form = IngredientsForm(request.POST)
#         if form.is_valid():
#             ingredients = form.save(False)
#             ingredients.author = request.user
#             ingredients.recipe = recipe
#             ingredients.save()
#             return redirect('recipe_list')
#     else:
#         form = IngredientsForm()
#     context = {'form': form, 'recipe': recipe}
#     return render(request, 'ingredients/create.html', context)


@login_required(login_url="/accounts/login/")
def edit_ingredients(request, id):
    ingredients = get_object_or_404(Ingredients, id=id)
    print(ingredients)
    if request.method == 'POST':
        form = IngredientsForm(request.POST, instance = ingredients)
        if form.is_valid():
            form.save()
            return redirect('show_recipe')
    else:
        form = IngredientsForm(instance=ingredients)
    context = {
        'ingredients': ingredients,
        'form': form,
    }
    return render(request, 'ingredients/edit.html', context)


@login_required(login_url="/accounts/login/")
def show_ingredients(request, id):
    ingredients = get_object_or_404(Ingredients, id=id)
    context = {'ingredients': ingredients}

    return render(request, 'ingredients/detail.html', context)



# # @login_required(login_url="/accounts/login/")
# def show_ingredients(request):
#     ingredients = Ingredients.objects.filter(author=request.user)
#     context = {'ingredients': ingredients}
#     return render(request, 'ingredients/detail.html', context)

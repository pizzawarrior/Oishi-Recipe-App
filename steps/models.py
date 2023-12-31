from django.db import models
from recipes.models import Recipe


class RecipeStep(models.Model):
    instruction = models.TextField()
    order = models.PositiveIntegerField()
    recipe = models.ForeignKey(
        Recipe,
        related_name= 'steps',
        on_delete=models.CASCADE
    )

        # Meta ordering may be less performant at scale, consider ordering using ORM
    class Meta:
        ordering= ['order']

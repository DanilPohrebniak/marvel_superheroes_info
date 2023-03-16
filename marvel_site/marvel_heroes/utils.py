from django.db.models import Count
from django.core.cache import cache

from marvel_heroes.models import Category

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_article'},
        {'title': 'Feedback', 'url_name': 'feedback'}
        ]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        cats = Category.objects.annotate(Count('heroes'))
        # if not cats:
        #     cats = Category.objects.annotate(Count('heroes'))
        #     cache.set('cats', cats, 60)

        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
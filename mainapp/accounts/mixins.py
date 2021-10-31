from mainapp.models import Category


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate()

        if not self.request.user.is_authenticated:
            context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

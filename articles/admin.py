from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Tag, Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        seen_is_main_values = set()

        for form in self.forms:
            if form.cleaned_data:
                article = form.cleaned_data.get('article')  # Получаем объект статьи
                is_main = form.cleaned_data.get('is_main', False)

                # Проверка на дублирование по статье и флагу is_main
                if (article, is_main) in seen_is_main_values:
                    raise ValidationError('Дубликат основных разделов не допускается.')

                seen_is_main_values.add((article, is_main))

                # Подсчет основных разделов
                if is_main:
                    main_count += 1

        # Проверка на наличие ровно одного основного раздела
        if main_count == 0:
            raise ValidationError('Необходимо указать один основной раздел.')
        elif main_count > 1:
            raise ValidationError('Основным может быть только один раздел.')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
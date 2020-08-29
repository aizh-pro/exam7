from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.question)

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Choice(models.Model):
    choice_text = models.CharField(max_length=200, null=False, blank=False, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='poll', on_delete=models.CASCADE, verbose_name='опрос')

    def __str__(self):
        return "{}. {}".format(self.pk, self.choice_text)

    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"
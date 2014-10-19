from django.contrib import admin

# Register your models here.

from askapp.models import Tag, Question, Answer, QuestionView, Bookmark, QVote, AVote

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionView)
admin.site.register(Bookmark)
admin.site.register(QVote)
admin.site.register(AVote)
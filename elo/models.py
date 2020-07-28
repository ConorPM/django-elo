from django.db import models
from django.forms import ModelForm
import floppyforms
from .python_elo import database_reader
from .config import GAME


class EloModel(models.Model):
    user_one_name = models.CharField(max_length=100)
    user_one_score = models.IntegerField()
    user_two_name = models.CharField(max_length=100)
    user_two_score = models.IntegerField()


class EloForm(ModelForm):
    class Meta:
        model = EloModel
        fields = "__all__"
        dl = database_reader.pull_list_of_players(GAME)
        widgets = {
            'user_one_name': floppyforms.widgets.Input(datalist=dl),
            'user_two_name': floppyforms.widgets.Input(datalist=dl)

        }

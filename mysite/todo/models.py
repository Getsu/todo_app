from django.db import models

# models.py にクラスを作成し、その中に設定する変数がデータベースのカラムになる
class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)


from django import forms
from django.contrib.auth.forms import UserCreationForm


KIND = (
    ("user", "権限を追加（投稿のみ）"),
    ("group", "グループの権限を追加（編集と削除）"),
)


class UserCreateForm(UserCreationForm):
    kind = forms.ChoiceField(label="権限の設定", choices=KIND)

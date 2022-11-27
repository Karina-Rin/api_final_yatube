from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Группа")
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField(
        max_length=400, verbose_name="Описание группы"
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст поста",
        help_text="Введите текст поста",
        max_length=200,
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="posts",
    )
    image = models.ImageField(
        verbose_name="Картинка", upload_to="posts/", null=True, blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name="Группа",
        help_text="Выберите группу",
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField(
        max_length=500,
        verbose_name="Текст",
        help_text="Текст комментария",
    )
    created = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True,
        db_index=True,
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Пользователь",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Автор",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"], name="unique_follow"
            )
        ]

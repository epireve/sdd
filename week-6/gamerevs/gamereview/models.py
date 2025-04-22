from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Tags(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "Tags"


class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=50, default="null")
    label_tag = models.ManyToManyField(Tags)
    slug = models.SlugField(max_length=150, default="null")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "null":
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150, default="null")

    def __str__(self):
        return f"Review for {self.game.title}"

    def save(self, *args, **kwargs):
        # Only set the slug if this is a new review (no ID yet)
        is_new = self.pk is None

        # First save to get the ID
        super().save(*args, **kwargs)

        # Set the slug and save again, but only if needed
        if is_new or self.slug == "null":
            self.slug = f"{self.id}-{slugify(self.game.title)}"
            # Use update to avoid recursive save
            type(self).objects.filter(pk=self.pk).update(slug=self.slug)

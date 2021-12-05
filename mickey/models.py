from django.db import models

# Create your models here.
class CreatorMixin(models.Model):
    creator = models.ForeignKey(
        'auth.User', verbose_name='creator', editable=False, blank=True, null=True,
        on_delete=models.CASCADE
    )
    def save(self, *args, **kwargs):
        from mickey.middleware import get_current_user
        if not self.creator:
            self.creator = get_current_user()
        super(CreatorMixin, self).save(*args, **kwargs)
    save.alters_data = True

    class Meta:
        abstract = True
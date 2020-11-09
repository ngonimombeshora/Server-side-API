from django.db import models

# More models can be created depending on the what the user requires.


class Device(models.Model):
    name = models.CharField(max_length=20, blank=True, default='device name')
    category = models.CharField(max_length=10, blank=True, default='sensor')
    location = models.CharField(max_length=30, blank=True, default='')
    status = models.CharField(max_length=30, blank=True, default='')
    reading = models.CharField(max_length=30, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User', related_name='devices', on_delete=models.CASCADE, default="not set")

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    class Meta:
        ordering = ('created',)

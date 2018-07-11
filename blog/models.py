from django.db import models

# Create a Blog models
        # title
        # pub_date
        # body
        # image
# Add the Blog app to the settings
# Create a migration
# Migrate
# Add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # 这样后台就会显示title，而不是 Blog Object(1)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

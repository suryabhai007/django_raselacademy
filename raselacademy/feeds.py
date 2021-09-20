from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from . models import Blog

class LatestBlogsFeed(Feed):
    app_name = 'raselacademy'
    title = 'My blog'
    link = '/raselacademy/'
    description = 'Latest post'

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return item.heading

    def item_description(self, item):
        return truncatewords(item.body, 30)

from django.contrib import sitemaps
from django.urls import reverse

from django.contrib.sitemaps import Sitemap
from courses.models import Course


class CoursesSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5
    i18n = True

    def items(self):
        return Course.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        return reverse('courses_show', kwargs={'_id': item.id})


class CoursesStaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    i18n = True

    def items(self):
        return ['courses_index']

    def location(self, item):
        return reverse(item)

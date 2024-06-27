def get_last_three_news(News):
    return News.objects.all().order_by('-created_at')[:3]
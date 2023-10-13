from django.utils.cache import patch_cache_control

class CacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Configurar los encabezados de caché para todos los recursos estáticos
        if request.path.startswith('/static/') or request.path.startswith('/media/'):
            patch_cache_control(response, public=True, max_age=31536000, stale_while_revalidate=604800)

        return response
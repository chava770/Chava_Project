from django.shortcuts import render
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Workers

def home(request):
    # Try to get the data from the cache
    work = cache.get('all_workers')

    # If it's not in the cache, fetch it from the database
    if work is None:
        work = Workers.objects.all()

        # Store the data in the cache
        cache.set('all_workers', work, timeout=None)

    return render(request, 'workers/home.html', {'work':work})

def detail(request, EMPLOYEE_ID):
    # Try to get the data from the cache
    cache_key = f'worker_{EMPLOYEE_ID}'
    worker = cache.get(cache_key)

    # If it's not in the cache, fetch it from the database
    if worker is None:
        worker = Workers.objects.get(EMPLOYEE_ID=EMPLOYEE_ID)

        # Store the data in the cache
        cache.set(cache_key, worker, timeout=None)

    return render(request, 'workers/detail.html', {'worker':worker})

@receiver(post_save, sender=Workers)
def update_worker_cache(sender, **kwargs):
    # Get the updated worker object
    worker = kwargs['instance']

    # Invalidate the cache for this worker
    cache_key = f'worker_{worker.EMPLOYEE_ID}'
    cache.delete(cache_key)

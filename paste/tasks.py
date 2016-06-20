from celery.task import task

from paste.models import PasteItem


@task(name='delete-expired-items')
def delete_expired_items():
    items = PasteItem.objects.all()
    expired_items = filter(lambda x: x.is_expired, items)
    expired_item_ids = map(lambda x: x.id, expired_items)
    items.filter(id__in=expired_item_ids).delete()

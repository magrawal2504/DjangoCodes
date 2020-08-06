# from django.shortcuts import render
from countViewsDownload.models import Hit, Publication, Journal, UserAgent
from django.http import HttpResponse


# Create your views here.
def get_journal_statistics(request):
    summary = []

    journal_ids = Journal.objects.prefetch_related('journal').all()
    production_id = Publication.objects.filter(journal__in=journal_ids)

    if production_id:
        hits = Hit.objects.all()

        for i in production_id:
            total_view = 0
            total_download = 0

            publication_td = hits.filter(publication=i, action='DL')
            publication_tv = hits.filter(publication=i, action='PV')
            if publication_tv:
                total_view = publication_tv.count()
            if publication_td:
                total_download = publication_td.count()

            instance_dict = {
                "journal_id": i.journal.id,
                "total_views": total_view,
                "total_downloads": total_download
            }
            summary.append(instance_dict)
        return HttpResponse(summary)
    else:
        return HttpResponse("No Http Response was found")

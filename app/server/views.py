"""
General server views
"""
from django.shortcuts import redirect


def redirect_to_inventory(request):
    # noqa: W0613
    """
    Redirects any request to /inventory/
    """
    return redirect('/inventory/')

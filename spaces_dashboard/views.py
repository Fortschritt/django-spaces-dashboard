# -*- coding: utf-8 -*-
from actstream.models import target_stream
import json
from django.http import HttpResponse, Http404
from django.shortcuts import render
from collab.decorators import permission_required_or_403
from spaces.models import SpacePluginRegistry
# Create your views here.

def get_activity_stream(space):
    """
    Return a list of recent activities of interest for members of the current
    space.

    The actual events get created by the individual space_plugins
    """
    if space: # space is none for request like e.g. GET /favicon.ico3
        ret = target_stream(space)[:10]
    else:
        ret = None
    return ret

@permission_required_or_403('access_space')
def dashboard(request):
    if request.SPACE is None:
        raise Http404
    extra_context = {}
    extra_context["activity_stream"] = get_activity_stream(request.SPACE)
    return render(request,'spaces_dashboard/dashboard.html',extra_context) 


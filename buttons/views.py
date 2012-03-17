
 #-*-coding: utf-8

#Create your views here.
from myapps.buttons.models import Button, Like
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
import json
import datetime

def index(request):
    render_result = {};

    render_result["buttons"] = Button.objects.all().order_by("public_time");

    return render_to_response("buttons/index.html", render_result);

def button_delete(request, button_id):

    button = Button.objects.get(id=button_id);

    button.delete();

    return HttpResponseRedirect(reverse("myapps.buttons.views.index"));

def button_post(request):
    if (request.method == "POST"):
        name = request.POST["name"];
        pass_hash = request.POST["password"];
        label = request.POST["label"];
        if (Button.objects.filter(name=name).count() != 0):
            return HttpResponse(u"<p>同じ名前</p>");
        new_botton = Button(name=name, password=pass_hash, label=label);
        new_botton.save();
        return HttpResponseRedirect(reverse("myapps.buttons.views.index"));
    button = Button();
    return render_to_response("buttons/post_button.html");

def button_display_page(request, button_id):
    button = Button.objects.get(id=button_id);
    return render_to_response("buttons/display.html", {"id": button_id, "label": button.label});

def button_display_json(request, button_id):
    result = {"like_count":0};
    now_like = Like.objects.filter(button=button_id, used_flag=False);
    
    result["like_count"] = now_like.count();
    now_like.update(used_flag=True);
    return HttpResponse(json.dumps(result));

def button_controler(request, button_id):

    return render_to_response("buttons/time_keeper.html", {"id": button_id});

def like_post(request, button_id):
    button = Button.objects.get(id=button_id);
    if (request.method == "POST"):
        new_like = Like(button=button, used_flag=False);
        new_like.save();
        return HttpResponseRedirect(reverse("myapps.buttons.views.like_post", args=(button_id,)));

    like = Like(button=button);
    return HttpResponse(like.post_form());

def get_like_hist_json(request, button_id):
    result = {};

    start = datetime.datetime.strptime(request.GET["start"], "%Y-%m-%d %H:%M:%S");
    end = datetime.datetime.strptime(request.GET["end"], "%Y-%m-%d %H:%M:%S");
    
    button = Button.objects.get(id=button_id);
    like_list = button.like_set.filter(time__gte=start, time__lte=end);
    
    dic = {};
    for like in like_list:
        delta = like.time - start;
        print like.time, start;
        print delta.seconds
        if (dic.has_key(delta.seconds) == False):
            dic[delta.seconds] = 1;
        else:
            dic[delta.seconds] += 1;
    
    print dic
    result["chart_data"] = [];
    for i in range((end - start).seconds):
        if (dic.has_key(i) == True):
            result["chart_data"].append((i, dic[i]));
        else:
            result["chart_data"].append((i, 0));
    
    return HttpResponse(json.dumps(result));


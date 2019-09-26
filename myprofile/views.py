from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from .models import Profile, Timeline
from .forms import FamilyMemberFormSet, TimelineFormSet, TimelineForm
from django.forms import formset_factory
from django.shortcuts import render


class ProfileList(ListView):
    model = Profile


class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']


class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Profile
    success_url = '/'
    fields = ['first_name', 'last_name']


class ProfileFamilyMemberUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST, instance=self.object)
        else:
            data['familymembers'] = FamilyMemberFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberUpdate, self).form_valid(form)


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-list')



def manage_articles(request):
    # TimelineFormSet = formset_factory(TimelineForm)
    if request.method == 'POST':
        formset = TimelineFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for forms in formset:
                forms.save()
            return redirect('profile-list')
    else:
        formset = TimelineFormSet()
    return render(request, 'add_timeline_form.html', {'formset': formset})

def timeline_view(request):
    context['titles'] = Timeline.obects.all()
    context['timeline'] = Timeline.obects.filter(title=query)
    return render(request, 'timeline.html', context)
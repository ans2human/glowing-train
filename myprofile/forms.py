from django.forms import ModelForm, inlineformset_factory, formset_factory

from .models import Profile, FamilyMember, Timeline


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ()
        # fields = ('')

class FamilyMemberForm(ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()


FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,
                                            form=FamilyMemberForm, extra=1)



class TimelineForm(ModelForm):
    class Meta:
        model = Timeline
        exclude = ('created_date', )

TimelineFormSet = formset_factory(TimelineForm, extra=2)
from django import forms 

class SuggestionForm(forms.Form):
    dishName = forms.CharField(label="Dish Name", max_length=100)
    description = forms.Charfield(label="Description", max_length = 280)
    cuisine = forms.Charfield(label="Cuisine", max_length = 100)

from dal import autocomplete
from django import forms
from django.core.validators import RegexValidator


from .models import Product


class BaseForm(forms.ModelForm):
    """Basic search form"""

    alpha_space = RegexValidator(r"^[a-zA-Z ]+$", "Seules les lettres sont autorisées")
    product_search = forms.CharField(
        max_length=100,
        label=False,
        validators=[alpha_space],
        widget=forms.TextInput(
            attrs={"placeholder": "Recherchez des substituts à un produit"}
        ),
    )

    class Meta:
        model = Product
        fields = ("product_search",)


class ProductForm(forms.ModelForm):
    """autocomplete search form"""

    product_search = forms.ModelChoiceField(
        label=False,
        queryset=Product.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="autocomplete",
            attrs={
                # Set some placeholder
                "data-placeholder": "Recherchez des substituts à un produit",
                # Only trigger autocompletion after 1 character has been typed
                "data-minimum-input-length": 1,
            },
        ),
    )

    class Meta:
        model = Product
        fields = ("product_search",)

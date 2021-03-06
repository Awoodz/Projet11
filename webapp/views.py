from urllib.parse import urlencode

from dal import autocomplete
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from webapp.models import Nutriments, Product
from webapp.utilities.sql.sql_insert import Sql_insert

from .forms import ProductForm


class IndexView(generic.FormView):
    """Index page"""

    # Use autocomplete form
    form_class = ProductForm

    def get(self, request):
        return render(
            request,
            "webapp/index.html",
            {
                "prodform": self.form_class,
            },
        )


def legal_mention(request):
    """Legal mention page"""
    template = loader.get_template("webapp/legalmention.html")
    return HttpResponse(template.render(request=request))


@login_required
def account(request):
    """User account page"""
    template = loader.get_template("webapp/account.html")
    return HttpResponse(template.render(request=request))


@login_required
def saved_products(request):
    """User's saved product page"""
    template = loader.get_template("webapp/saved_products.html")
    # set the user as the actual user
    current_user = request.user
    # filters distinct nutriscore in order to create a filter list in template
    nutriscore_list = Product.objects.filter(
        user_product=current_user.id
    ).values("product_nutriscore").distinct()

    return HttpResponse(template.render(
        {"nutriscore_list": nutriscore_list, },
        request=request
    ))


def ajax_saved_products(request):
    """Filter saved products ajax call"""
    template = loader.get_template("webapp/saved_products.html")
    # set the user as the actual user
    current_user = request.user
    # filters distinct nutriscore in order to create a filter list in template
    nutrichar = request.GET.get("nutrichar")
    if nutrichar == "nofilter":
        products = Product.objects.filter(user_product=current_user.id)
    else:
        products = Product.objects.filter(
            user_product=current_user.id, product_nutriscore=nutrichar
        )
    return HttpResponse(
        template.render(
            {
                "products": products,
            }, request=request
        )
    )


def product(request, product_id):
    """Product page"""
    template = loader.get_template("webapp/product.html")
    # if product id doesn't exist, create 404 error
    product = get_object_or_404(Product, pk=product_id)
    # get the product's nutriments data
    nutriment = Nutriments.objects.get(nutriments_product_id=product_id)

    return HttpResponse(
        template.render(
            {
                "product": product,
                "nutriment": nutriment
                }, request=request
        )
    )


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    """Autocomplete form"""

    def get_queryset(self):
        """Set how autocomplete form must filter"""

        request = Product.objects.all().order_by("id")

        if self.q:
            request = request.filter(
                product_name__unaccent__istartswith=self.q
            )

        return request


class SearchHelpView(generic.FormView):
    """Search help page"""

    # use autocomplete form
    form_class = ProductForm

    def get(self, request):
        """Find products that can match with user search"""
        query = request.GET.get("query")
        # filter products that contain query
        products = Product.objects.filter(
            product_name__unaccent__icontains=query
        )
        return render(
            request,
            "webapp/search_help.html",
            {
                "prodform": self.form_class,
                "query": query,
                "products": products
            },
        )


def save_product(request):
    """Save a user's product"""
    # set the user as the actual user
    current_user = request.user
    # get the product id
    get_product_id = request.GET.get("product_token")

    product = Product.objects.get(pk=get_product_id)
    # insert manytomanyfield in database
    Sql_insert.user_saved_product_inserter(product, current_user)

    return HttpResponse("Vous ne devriez pas voir ceci !")


def search(request):
    """Search page"""
    template = loader.get_template("webapp/search.html")
    # get string in product_search key
    query = request.GET.get("product_search")
    # if autocomplete search form is used
    try:
        # get product with id
        searched_product = Product.objects.filter(id=query)
    # if classic search form is used
    except ValueError:
        # get product with name
        searched_product = Product.objects.filter(
            product_name__unaccent__iexact=query
        )
        # if there is more than one result
        if searched_product.count() != 1:
            # redirect to the search help page
            base_url = reverse("search_help")
            query_string = urlencode({"query": query})
            url = "{}?{}".format(base_url, query_string)
            return redirect(url)

    for picked_product in searched_product:
        nutriscore_list = (
            Product.objects.filter(
                product_category_id=picked_product.product_category_id
            )
            .values("product_nutriscore")
            .distinct()
            .exclude(product_nutriscore__gte=picked_product.product_nutriscore)
            .order_by("product_nutriscore")
        )


    return HttpResponse(
        template.render(
            {
                "searched_product": searched_product,
                "nutriscore_list": nutriscore_list,
            },
            request=request,
        )
    )


def ajax_search(request):
    template = loader.get_template("webapp/product_list.html")
    # set the user as the actual user
    nutrichar = request.GET.get("nutrichar")
    query = request.GET.get("search_prod")
    searched_product = Product.objects.filter(id=query)
    if nutrichar == "nofilter":
        for picked_product in searched_product:
            # search for product from same category with a better nutriscore value
            products = (
                Product.objects.filter(
                    product_category_id=picked_product.product_category_id
                )
                .exclude(product_nutriscore__gte=picked_product.product_nutriscore)
                .order_by("product_nutriscore")[:30]
            )
    else:
        for picked_product in searched_product:
            # search for product from same category with a better nutriscore value
            products = (
                Product.objects.filter(
                    product_category_id=picked_product.product_category_id,
                    product_nutriscore=nutrichar,
                )
            )
    return HttpResponse(
        template.render(
            {
                "products": products,
            }, request=request
        )
    )

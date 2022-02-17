from shopping.models import Category


def check_is_item(record):
    if record.category_type == 'I':
        return True

    return False


def check_is_department(record):
    if record.category_type == 'D':
        return True

    return False


def template_context(request):
    categories = Category.objects.all().order_by('-category_type')

    return {
        'items': list(filter(check_is_item, categories)),
        'departments': list(filter(check_is_department, categories)),
    }

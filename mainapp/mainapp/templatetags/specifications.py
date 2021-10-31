from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Outerwear


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'shoes': {
        'Вид застежки': 'fastener_type',
        'Материал подкладки': 'lining_material',
        'Материал стельки': 'insole_material',
        'Вид каблука': 'type_of_heel',
        'Страна-производитель': 'country_of_origin',
        'Пол': 'gender'
    },
    'outerwear': {
        'Вид застежки': 'fastener_type',
        'Материал подкладки': 'lining_material',
        'Тип рукава': 'sleeve_type',
        'Утеплитель': 'resolution',
        'Длина одежды': 'clothing_length',
        'Направление': 'trend',
        'Страна-производитель': 'country_of_origin',
        'Пол': 'gender'
    },
    'sweatshirts': {
        'Тип рукава': 'sleeve_type',
        'Утеплитель': 'resolution',
        'Направление': 'trend',
        'Страна-производитель': 'country_of_origin',
        'Пол': 'gender'
    },
    'jeans': {
        'Вид застежки': 'fastener_type',
        'Тип карманов': 'type_of_pockets',
        'Утеплитель': 'resolution',
        'Модель джинсов': 'model_jeans',
        'Страна-производитель': 'country_of_origin',
        'Пол': 'gender'
    },

    'costumes': {
        'Вид застежки': 'fastener_type',
        'Материал подкладки': 'lining_material',
        'Тип карманов': 'type_of_pockets',
        'Утеплитель': 'resolution',
        'Модель костюма': 'model_costume',
        'Направление': 'trend',
        'Страна-производитель': 'country_of_origin',
        'Пол': 'gender'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Outerwear):
        if not product.trend:
            PRODUCT_SPEC['outerwear'].pop('Направление', None)
        else:
            PRODUCT_SPEC['outerwear']['Направление'] = 'trend'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)


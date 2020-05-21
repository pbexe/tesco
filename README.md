[![Downloads](https://pepy.tech/badge/tesco)](https://pepy.tech/project/tesco)

# Tesco

 A Python wrapper for the Tesco API

## Installation

`pip install tesco`

## Usage

```python
from tesco import Tesco
from pprint import pprint

t = Tesco("API KEY")
results = t.grocery_search("cake", offset=0, limit=100)

info = t.product_data(tpnc=results[0]["id"])

pprint(info)
```

```python
[{'allergenAdvice': {'allergenText': 'May contain milk and  peanuts and '
                                     'nuts.For allergens, including cereals '
                                     'containing gluten, see ingredients in '
                                     'bold. \n',
                     'allergens': [{'allergenName': 'Contains',
                                    'allergenValues': ['May contain milk',
                                                       'peanuts',
                                                       'nuts.']}]},
  'brand': 'TESCO',
  'calcNutrition': {'calcNutrients': [{'name': 'Energy (kJ)',
                                       'valuePer100': '1624',
                                       'valuePerServing': '556'},
                                      {'name': 'Energy (kcal)',
                                       'valuePer100': '387',
                                       'valuePerServing': '132'},
                                      {'name': 'Fat (g)',
                                       'valuePer100': '14.8',
                                       'valuePerServing': '5.1'},
                                      {'name': 'Saturates (g)',
                                       'valuePer100': '4.8',
                                       'valuePerServing': '1.6'},
                                      {'name': 'Carbohydrate (g)',
                                       'valuePer100': '57.8',
                                       'valuePerServing': '19.8'},
                                      {'name': 'Sugars (g)',
                                       'valuePer100': '34.6',
                                       'valuePerServing': '11.9'},
                                      {'name': 'Fibre (g)',
                                       'valuePer100': '1.1',
                                       'valuePerServing': '0.4'},
                                      {'name': 'Protein (g)',
                                       'valuePer100': '5',
                                       'valuePerServing': '1.7'},
                                      {'name': 'Salt (g)',
                                       'valuePer100': '0.6',
                                       'valuePerServing': '0.2'}],
                    'per100Header': 'Per 100g / Per 100ml',
                    'perServingHeader': 'A serving contains'},
  'description': 'Tesco Angel Layer Cake Each',
  'gda': {'gdaRefs': [{'footers': ['of the reference intake*',
                                   'Typical values per 100g: Energy 1624kJ / '
                                   '387kcal'],
                       'gdaDescription': 'Guideline Amounts Per Serv',
                       'headers': ['1/8 of a cake (34g)'],
                       'values': [{'name': 'Energy',
                                   'percent': '7',
                                   'values': ['556kJ', '132kcal']},
                                  {'name': 'Fat',
                                   'percent': '7',
                                   'rating': 'medium',
                                   'values': ['5.1g']},
                                  {'name': 'Saturates',
                                   'percent': '8',
                                   'rating': 'medium',
                                   'values': ['1.6g']},
                                  {'name': 'Sugars',
                                   'percent': '13',
                                   'rating': 'high',
                                   'values': ['11.9g']},
                                  {'name': 'Salt',
                                   'percent': '3',
                                   'rating': 'medium',
                                   'values': ['0.2g']}]}]},
  'gtin': '05000119153739',
  'ingredients': ['<p><strong>INGREDIENTS LIST:</strong><br><br>Sugar',
                  'Wheat Flour (<strong>Wheat</strong> Flour, Calcium '
                  'Carbonate, Iron, Niacin, Thiamin), Pasteurised '
                  '<strong>Egg</strong> White, Vanilla Flavour Filling (11%), '
                  'Palm Oil, Rapeseed Oil, Humectant (Glycerine), Raising '
                  'Agents (Disodium Diphosphate, Sodium Bicarbonate), '
                  'Emulsifier (Mono- and Di-Glycerides of Fatty Acids), '
                  'Preservative (Potassium Sorbate), Salt, Colours (Carmines, '
                  'Carotenes).<br><br>Vanilla Flavour Filling contains: Sugar, '
                  'Palm Oil, Rapeseed Oil, Glucose Syrup, Rice Starch, '
                  'Emulsifier (Mono- and Di-Glycerides of Fatty Acids), '
                  'Flavouring, Acidity Regulator (Citric Acid), Colour (Plain '
                  'Caramel).</p>'],
  'marketingText': 'Teatime classic Layered sponge with vanilla flavour '
                   'filling for a light, delicate cake\n'
                   'Teatime classic Layered sponge with vanilla flavour '
                   'filling for a light, delicate cake',
  'pkgDimensions': [{'depth': 5.2,
                     'dimensionUom': 'cm',
                     'height': 7.0,
                     'no': 1,
                     'volume': 666.12,
                     'volumeUom': 'cc',
                     'weight': 278.0,
                     'weightUom': 'g',
                     'width': 18.3}],
  'productAttributes': [],
  'productCharacteristics': {'containsLoperamide': False,
                             'healthScore': 38,
                             'isAnalgesic': False,
                             'isDrink': False,
                             'isFood': True,
                             'isHazardous': False,
                             'storageType': 'Ambient'},
  'qtyContents': {'netContents': '1',
                  'numberOfUnits': '1',
                  'quantity': 1.0,
                  'quantityUom': 'SNGL',
                  'unitQty': 'EACH'},
  'storage': ['Not suitable for home freezing. \n'
              'Store in a cool, dry place and once opened in an airtight '
              'container.\n'
              '    '],
  'tpnb': '050556274',
  'tpnc': '254946995'}]
  ```

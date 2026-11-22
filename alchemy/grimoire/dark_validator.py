from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    bon = dark_spell_allowed_ingredients()
    for ingre in bon:
        if ingre in ingredients.lower():
            return f"Ingredients '{ingredients}'- VALID"
    return f"Ingredients '{ingredients}'- INVALID"
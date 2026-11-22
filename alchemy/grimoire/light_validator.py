def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    bon = light_spell_allowed_ingredients()
    for ingre in bon:
        if ingre in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
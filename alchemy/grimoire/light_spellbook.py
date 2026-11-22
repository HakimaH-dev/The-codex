from .light_validator import validate_ingredients

def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    resultat = validate_ingredients(ingredients)
    if resultat.endswith("- VALID"):
        return (f"{spell_name}' Spell recorded: {resultat}")
    else:
        return (f"'{spell_name}' Spell rejected: {resultat}")
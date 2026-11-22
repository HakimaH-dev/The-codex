from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    resultat = validate_ingredients(ingredients)
    if resultat.endswith(": VALID"):
        return f"Dark spell '{spell_name}' recorded: {resultat}"
    else:
        return f"Dark spell '{spell_name}' rejected: {resultat}"
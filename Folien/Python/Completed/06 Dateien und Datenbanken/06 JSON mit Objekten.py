# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>JSON mit Objekten</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # JSON mit Objekten

# %%
import io
import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from pprint import pprint

# %% [markdown]
#
# Falls die verwendeten JSON Dateien nicht automatisch gefunden werden, kann
# über die Environment-Variable `CAM_DATA_DIR_PATH` der korrekte Pfad gesetzt
# werden.

# %%
CAM_DATA_DIR_FROM_ENV = os.getenv("CAM_DATA_DIR_PATH")
if CAM_DATA_DIR_FROM_ENV:
    data_dir = Path(CAM_DATA_DIR_FROM_ENV)
else:
    data_dir = Path().absolute()
print(f"Data directory: {data_dir}")
assert data_dir.exists()


# %% [markdown]
#
# ## Benutzerdefinierte Klassen
#
# Wir definieren einige Klassen, die eine einfache Beschreibung für Menüs in
# einer grafischen Benutzeroberfläche repräsentieren.
#
# Die `from_dict()` Methoden dienen dazu, Instanzen dieser Klassen aus Python
# Dictionaries zu erzeugen.

# %%
@dataclass
class Menu:
    id: str
    name: str
    items: list["MenuItem"]

    @staticmethod
    def from_dict(d):
        return Menu(d["id"], d["name"], [MenuItem.from_dict(m) for m in d["menuitems"]])


# %%
@dataclass
class MenuItem:
    name: str
    onclick: str

    @staticmethod
    def from_dict(d):
        return MenuItem(d["name"], d["onclick"])


# %% [markdown]
#
# ## Erzeugen von Python Objekten aus JSON-Objekten:
#
# - Man kann dem JSON-Decoder einen `object_hook` übergeben. Das ist eine Funktion,
#   die aufgerufen wird, nachdem ein JSON-Objekt in ein Python Dictionary
#   umgewandelt wurde.
# - Der Rückgabewert des `object_hook`s wird anstatt des Dictionaries vom
#   JSON-Decoder zurückgegeben.

# %%
with open(data_dir / "simple-menu.json", mode="r", encoding="utf-8") as file:
    my_json = json.load(file)

# %%
pprint(my_json)


# %%
def menu_hook(d: dict):
    print(f"Menu hook: {d}")
    if "_type" in d and d["_type"] == "menu":
        return Menu.from_dict(d)
    return d


# %%
with open(data_dir / "simple-menu.json", mode="r", encoding="utf-8") as file:
    my_menu = json.load(file, object_hook=menu_hook)

# %%
pprint(my_menu)


# %%
# json.dumps(my_menu)


# %%
def menu_serializer(obj):
    if isinstance(obj, Menu):
        return {
            "_type": "menu",
            "id": obj.id,
            "name": obj.name,
            "menuitems": obj.items,
        }
    if isinstance(obj, MenuItem):
        return {"name": obj.name, "onclick": obj.onclick}
    return obj


# %%
print(json.dumps(my_menu, default=menu_serializer, indent=2))

# %%
with open(data_dir / "simple-menu.json", mode="r", encoding="utf-8") as file:
    file_contents = file.read()

# %%
file_contents == json.dumps(my_menu, default=menu_serializer, indent=2)


# %% [markdown]
#
# Als Alternative kann man auch von der Klasse `JSONEncoder` erben und die
# Methode `default` überschreiben:

# %%
class MenuEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Menu):
            return {
                "_type": "menu",
                "id": obj.id,
                "name": obj.name,
                "menuitems": obj.items,
            }
        elif isinstance(obj, MenuItem):
            return {"name": obj.name, "onclick": obj.onclick}
        return json.JSONEncoder.default(self, obj)


# %%
json.dumps(my_menu, cls=MenuEncoder)

# %%
json.dumps(my_menu, cls=MenuEncoder) == json.dumps(my_menu, default=menu_serializer)

# %%
print(file_contents)

# %%
print(json.dumps(my_menu, cls=MenuEncoder))

# %%
json.dumps(my_menu, cls=MenuEncoder, indent=2) == file_contents


# %% [markdown]
#
# ## Mini-Workshop: Rezepte mit Objekten
#
# Wir haben folgende Klass geschrieben, um Rezepte zu repräsentieren:

# %%
@dataclass
class Recipe:
    title: str
    ingredients: list[str]
    instructions: list[str]
    tips: list[str] = field(default_factory=list)

    def __str__(self):
        out = io.StringIO()
        print(f"# {self.title}\n", file=out)
        print("## Ingredients\n", file=out)
        for ingredient in self.ingredients:
            print(f"- {ingredient}", file=out)
        print("\n## Instructions\n", file=out)
        for n, instruction in enumerate(self.instructions, 1):
            print(f"{n}. {instruction}", file=out)
        print("\n## Tips\n", file=out)
        for tip in self.tips:
            print(f"- {tip}", file=out)
        print("\n", file=out)
        return out.getvalue()


# %% [markdown]
#
# Schreiben Sie Funktionen zum Serialisieren und Deserialisieren von `Recipe`-Instanzen
# ins JSON Format.
#
# Lesen Sie damit die `recipes.json`-Datei ein und überprüfen Sie, dass die
# Serialisierung der eingelesenen Liste mit dem Inhalt der Datei identisch ist.
#
# *Hinweis:* Sie müssen bei `json.dump()` das Keyword-Argument `ensure_ascii=False`
# angeben um Probleme mit Sonderzeichen zu vermeiden.
#
# Iterieren Sie über die Liste der Ergebnisse und rufen Sie `print()` für jedes
# Rezept auf. Stimmt die Ausgabe mit Ihren Erwartungen überein?

# %%
def recipe_hook(d: dict):
    if {"title", "ingredients", "instructions", "tips"}.issubset(d.keys()):
        # print(f"Found recipe: {d}")
        return Recipe(d["title"], d["ingredients"], d["instructions"], d["tips"])
    else:
        return d


# %%
def recipe_serializer(obj):
    if isinstance(obj, Recipe):
        return {
            "title": obj.title,
            "ingredients": obj.ingredients,
            "instructions": obj.instructions,
            "tips": obj.tips,
        }
    else:
        return obj


# %%
with open(data_dir / "recipes.json", "r", encoding="utf-8") as file:
    recipes = json.load(file, object_hook=recipe_hook)

# %%
# recipes

# %%
# json.dumps(recipes, default=recipe_serializer, indent=2, ensure_ascii=False)

# %%
# with open(data_dir / "recipes-dump.json", "w", encoding="utf-8") as file:
#     json.dump(recipes, file, default=recipe_serializer, indent=2, ensure_ascii=False)

# %%
with open(data_dir / "recipes.json", "r", encoding="utf-8") as file:
    recipe_str = file.read()

# %%
json.dumps(
    recipes, default=recipe_serializer, indent=2, ensure_ascii=False
) == recipe_str

# %%
for recipe in recipes:
    print(recipe)

# %%

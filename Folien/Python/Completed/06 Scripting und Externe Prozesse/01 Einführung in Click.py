# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in Click</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Was ist Click?
#
# - Command Line Interface Creation Kit
# - Python-Paket zur Erstellung schöner Kommandozeilenanwendungen
# - Kompositional und einfach zu verwenden

# %% [markdown]
#
# ## Click-Philosophie
#
# - Einfache und intuitive Definition von Kommandos, Argumenten und Optionen
# - Automatische Generierung von Hilfeseiten
# - Beliebig verschachtelte Befehlen
# - Unterstützt Lazy Loading von Unterbefehlen

# %% [markdown]
#
# ## Hauptmerkmale von Click
#
# - Analyse von Befehlszeilenargumenten
# - Behandlung von Optionen und Argumenten
# - Aufforderung zur Eingabe
# - Farbige Terminalausgabe
# - Automatisches Datei-Handling
# - Fortschrittsbalken
# - Starten von Editoren

# %% [markdown]
#
# ## Installation von Click
#
# ```bash
# pip install click
# ```

# %% [markdown]
#
# ## Beispiel: Witz-Erzähler

# %% [markdown]
#
# ### Grundstruktur eines Befehls
#
# ```python
# import click
#
# @click.command()
# def tell_joke():
#     """Dieses Skript erzählt dem Benutzer einen zufälligen Witz."""
#     # Rumpf der Funktion
# ```
#
# - Definiert einen einzelnen Befehl
# - Docstring wird zur Befehlsbeschreibung

# %% [markdown]
#
# ### Optionen mit Prompt
#
# ```python
# @click.option('--name', prompt='Dein Name', help='Die Person, die gegrüßt werden soll.')
# ```
#
# - Definiert eine Befehlszeilenoption
# - Falls nicht angegeben, wird der Benutzer aufgefordert
# - Hilfetext für --help-Ausgabe

# %% [markdown]
#
# ### Echo für Ausgabe
#
# ```python
# click.echo(f"Hallo, {name}! Hier ist ein Witz für dich:")
# ```
#
# - Plattformübergreifende Möglichkeit zum Drucken von Text
# - Behandelt Unicode und verschiedene Terminals

# %% [markdown]
#
# Code: `jokes.py`

# %% [markdown]
#
# ## Beispiel: Zeitreise-Agentur
#
# ### Befehlsargumente mit Auswahlmöglichkeiten
#
# ```python
# @click.argument('destination', type=click.Choice(['past', 'future']))
# ```
#
# - Positionales Argument
# - Beschränkt auf bestimmte Auswahlmöglichkeiten

# %% [markdown]
#
# ### Optionen mit Standardwerten
#
# ```python
# @click.option('--years', default=1, show_default=True, help='Anzahl der Jahre, die gereist werden sollen')
# ```
#
# - Option mit Standardwert
# - Zeigt Standardwert im Hilfetext

# %% [markdown]
#
# ### Boolean Flags
#
# ```python
# @click.option('--return-trip/--one-way', default=True, help='Ob eine Rückreise gebucht werden soll')
# ```
#
# - Boolesche Option mit Ein-/Aus-Flag

# %% [markdown]
#
# ### Verbose-Flag
#
# ```python
# @click.option('--verbose', is_flag=True, help='Ausführliche Ausgabe')
# ```
#
# - Einfaches boolesches Flag

# %% [markdown]
#
# Code: `time_travel_agency.py`

# %% [markdown]
#
# ## Beispiel: Superhelden-Manager
#
# ### Befehlsgruppen
#
# ```python
# @click.group()
# def superhero():
#     """Verwalte dein Superheldenteam!"""
#     pass
# ```
#
# - Erstellt eine Gruppe von Befehlen
# - Ermöglicht Unterbefehle

# %% [markdown]
#
# ### Subbefehle
#
# ```python
# @superhero.command()
# def add(name, power):
#     """Füge deinem Team einen neuen Superhelden hinzu."""
#     # Funktionsrumpf
# ```
#
# - Definiert einen Subbefehl innerhalb einer Gruppe


# %% [markdown]
#
# ### Kontextobjekte
#
# ```python
# @click.pass_context
# def superhero(ctx, file):
#     ctx.ensure_object(dict)
#     ctx.obj['team'] = team
#     ctx.obj['file'] = file
# ```
#
# - Überträgt Daten zwischen Befehlen
# - Nützlich zum Verwalten von Zustand

# %% [markdown]
#
# ### Dateiverarbeitung mit pathlib
#
# ```python
# @click.option('--file', type=click.Path(path_type=Path), default=DEFAULT_FILE)
# ```
#
# - Konvertiert automatisch in pathlib.Path
# - Ermöglicht einfache Dateioperationen
# - Kann angeben, ob Dateien/Verzeichnisse erlaubt sind, etc.

# %% [markdown]
#
# ### Kombination mehrerer Features
#
# ```python
# @click.group()
# @click.option('--file', type=click.Path(path_type=Path), default=DEFAULT_FILE)
# @click.pass_context
# def superhero(ctx, file):
#     # Funktionsrumpf
# ```
#
# - Zeigt, wie verschiedene Features kombiniert werden können

# %% [markdown]
#
# Code: `superhero_manager.py`

# %% [markdown]
#
# ## Beispiel: Task-Manager

# %% [markdown]
#
# ### Farbige Ausgabe
#
# ```python
# click.secho(f"Aufgabe hinzugefügt: {task}", fg="green")
# ```
#
# - Verwendet `click.secho()` für farbige Ausgabe
# - `fg` Parameter bestimmt die Vordergrundfarbe
# - Macht die CLI benutzerfreundlicher und informativer

# %% [markdown]
#
# ### Fortschrittsbalken
#
# ```python
# with click.progressbar(tasks, label="Verarbeite Aufgaben") as bar:
#     for task in bar:
#         # Simuliere Arbeit
#         time.sleep(0.5)
# ```
#
# - Zeigt Fortschritt für lang laufende Prozesse
# - Verbessert das Benutzererlebnis bei zeitaufwändigen Operationen

# %% [markdown]
#
# ### Starten von Editoren
#
# ```python
# click.edit(filename=tmp_filename)
# ```
#
# - Öffnet den Standard-Texteditor des Systems
# - Ermöglicht Bearbeitung von Text in der vertrauten Umgebung des Benutzers
# - Wartet, bis der Benutzer den Editor schließt
# - Funktioniert nicht mit allen Editoren und Systemkonfigurationen

# %% [markdown]
#
# ## Zusammenfassung
#
# - Click bietet eine leistungsstarke, intuitive Möglichkeit, CLIs zu erstellen
# - Bietet eine Vielzahl von Funktionen für komplexe Anwendungen
# - Fördert Best Practices im CLI-Design

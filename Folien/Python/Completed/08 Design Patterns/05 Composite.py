# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Composite</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Designproblem: Benutzeroberfläche
#
# - Komponenten in der Benutzeroberfläche haben eine hierarchische
#   Struktur:
#   -   Bildschirm
#   -   Fenster
#   -   Eingabemaske
#   -   Eingabefeld, Button, etc.
# - Das Interface der Komponenten soll einheitlich sein


# %% [markdown]
# ## Composite (Structural Pattern)
#
# ### Intent
#
# Compose objects into tree structures to represent part-whole
# hierarchies. Composite lets clients treat individual objects and
# compositions of objects uniformly.

# %% [markdown]
# ## Composite (Structural Pattern)
#
# ### Motivation
#
# Graphical editors let users build complex diagrams from simpler
# components. Components can be grouped to form larger components, which
# can themselves be grouped to form even larger components. Code that uses
# these components should not have to distinguish between primitives and
# complex components. The *Composite* pattern describes how to use
# recursive composition so that clients don't have to make this
# distinction.


# %% [markdown]
#
# ## Composite (Structural Pattern)
#
# ### Applicability
#
# Use the Composite pattern when
#
# -   You want to represent part-whole hierarchies of objects.
# -   You want clients to be able to ignore the difference between
#     compositions of objects and individual objects. Clients will treat
#     all objects in the composite structure uniformly.


# %% [markdown]
# ## Composite (Structural Pattern)
#
# ### Structure
#
#
# <img src="img/composite.png"
#      style="display:block;margin:auto;width:70%"/>


# %% [markdown]
# ## Composite (Structural Pattern)
#
# ### Consequences
#
# The *Composite* pattern
#
# -   defines class hierarchies consisting of primitive and composite
#     objects
# -   makes the clients simple
# -   makes it easier to add new kinds of components
# -   can make your design overly general


# %% [markdown]
#
# ## Composite (Structural Pattern)
#
# ### Known uses
#
# `Composite` and `Control` in SWT, abstract syntax trees
# in compilers, ...
#
# ### Related Patterns
#
# -   Chain of Command
# -   Decorator
# -   Iterator
# -   Visitor
# -   ...
#
# ### Example
# ...
#

# %% [markdown]
#
# ## Workshop: RPG-Würfel
#
# In Rollenspielen werden Konflikte zwischen Spielern oft durch Würfeln
# entschieden. Dabei werden oft mehrere Würfel gleichzeitig verwendet. Außerdem
# werden nicht nur die bekannten 6-seitigen Würfel verwendet, sondern auch
# 4-seitige, 8-seitige, 20-seitige Würfel, etc.
#
# Die Anzahl und Art der Würfel wird dabei durch folgende Notation beschrieben:
#
# ```text
# <Anzahl der Würfel> d <Seiten pro Würfel>
# ```
#
# Zum Beispiel wird das Würfeln mit zwei 6-seitigen Würfeln als `2d6`
# beschrieben. Manchmal werden auch komplexere Formeln verwendet:
# `3d20 + 2d6 - 4` bedeutet, dass gleichzeitig drei 20-seitige Würfel und zwei 6-seitige
# Würfel geworfen werden und die Gesamtsumme der Augenzahlen dann um 4
# verringert wird.
#
# In manchen Spielen wird das Werfen der niedrigsten oder höchsten Augenzahl
# besonders behandelt ("katastrophale Niederlage", "kritischer Erfolg").
#
# Wie können Sie das Composite-Pattern verwenden um RPG-Würfel zu implementieren?

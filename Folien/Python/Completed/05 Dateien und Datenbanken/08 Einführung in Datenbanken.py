# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in Datenbanken</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Was ist eine Datenbank?
#
# Eine Sammlung von Daten, die so organisiert und gespeichert ist, dass sie eine
# effiziente Abruf und Manipulation der Daten ermöglicht.
#
# Ein Datenbanksystem ist ein Softwaresystem, das eine Datenbank verwaltet.
#
# Wir unterscheiden im Folgenden nicht weiter zwischen Datenbank und
# Datenbanksystem.

# %% [markdown]
#
# ## Beispiele für Datenbanken:
# - Telefonbuch
# - Bibliothekskatalog
# - Online-Einkaufsseite
# - ...

# %% [markdown]
#
# ## Merkmale einer Datenbank
#
# - Konsistente und genaue Datenspeicherung
# - Effiziente Datenabfrage und -manipulation
# - Einfache gemeinsame Nutzung von Daten zwischen Anwendungen
# - Datensicherheit und Zugriffskontrolle
# - Skalierbarkeit und Flexibilität

# %% [markdown]
#
# ##  Arten von Datenbanken:
#
# Verschiedene Arten von Datenbanken bieten unterschiedliche Kompromisse
# zwischen diesen Merkmalen
#
# - Relationale Datenbanken
# - NoSQL-Datenbanken
# - Graph-Datenbanken
# - Objektorientierte Datenbanken
# - Dokumentorientierte Datenbanken

# %% [markdown]
#
# ### Relationale Datenbanken
#
# - Verwenden eine tabellenbasierte Struktur zum Speichern von Daten
# - Daten werden in Zeilen und Spalten organisiert
# - Beziehungen zwischen Tabellen werden durch Primär- und Fremdschlüssel hergestellt
# - Beispiele sind MySQL, PostgreSQL und Oracle Database


# %% [markdown]
#
# ### NoSQL-Datenbanken:
#
# Dies ist eine allgemeine Kategorie, die auch andere umfasst, wie z.B. graph-
# oder dokumentenorientierte Datenbanken.
#
# - Entwickelt für unstrukturierte Daten und nicht-relationale Datenmodelle
# - Sie verwenden oft keine Tabellen und kein festes Schema
#   - Es gibt aber auch NoSQL Datenbanken mit festem Schema
# - Daten werden als Schlüssel-Wert-Paare, JSON oder in anderen Formaten
#   gespeichert
# - Beispiele sind MongoDB, Couchbase und Cassandra

# %% [markdown]
#
# ### Graphische Datenbanken
#
# - Entwickelt, um komplexe Beziehungen zwischen Datenpunkten darzustellen.
# - Daten werden als Knoten, Kanten und Eigenschaften gespeichert
# - Das Durchlaufen des Graphen ermöglicht komplexe Abfragen und Analysen
# - Beispiele sind Neo4j und OrientDB

# %% [markdown]
#
# ### Objektorientierte Datenbanken
#
# - Entwickelt, um Objekte, Klassen und Methoden zu speichern.
# - Daten werden als Objekte mit Attributen und Verhaltensweisen
#   gespeichert
# - Sie unterstützen Vererbung und Polymorphismus
# - Beispiele sind db4o und ObjectDB

# %% [markdown]
#
# ### Dokumentorientierte Datenbanken
#
# - Entwickelt für die Speicherung und Verwaltung von Dokumenten
# - Daten werden als JSON, XML oder in anderen Formaten gespeichert
# - Flexibles Schema, das sich ändern kann, wenn sich die Daten ändern
# - Beispiele sind MongoDB, CouchDB und RavenDB

# %% [markdown]
#
# # Was ist eine relationale Datenbank?
#
# - Speichert Daten in Tabellen mit vordefinierten Beziehungen
#   - Tabellen bestehen aus Zeilen und Spalten
#   - Jede Tabelle hat einen Primärschlüssel, der jede Zeile eindeutig identifiziert
#   - Beziehungen zwischen Tabellen werden über Fremdschlüssel hergestellt
# - Verwendet in der Regel SQL als Abfragesprache

# %% [markdown]
#
# ## Tabellen und Zeilen
#
# - Tabellen werden verwendet, um zusammenhängende Daten in einem strukturierten
#   Format zu organisieren.
# - Jede Zeile in einer Tabelle stellt einen einzelnen Datensatz dar
# - Zeilen werden durch einen eindeutigen Bezeichner oder Primärschlüssel
#   identifiziert

# %% [markdown]
#
# Tabelle **Kunden**:
#
# | customer_id | name         |
# |-------------|--------------|
# |           1 | John Smith   |
# |           2 | Jane Doe     |
#
# Tabelle **Produkte**:
#
# | item_id | item_name   | price | description                            |
# |---------|-------------|-------|----------------------------------------|
# |    2341 | Tomato soup | 1.99  | Our fantastic tomato soup in tin cans. |
# |     346 | Chickpeas   | 0.59  | Soak in water and enjoy...             |

# %% [markdown]
#
# ## Spalten und Datentypen
#
# - Spalten stellen die Attribute oder Eigenschaften eines jeden Datensatzes
#   dar.
# - Jede Spalte hat einen bestimmten Datentyp, z. B. String, Integer oder Datum
# - Datentypen helfen, die Konsistenz und Genauigkeit der Daten zu
#   gewährleisten.

# %% [markdown]
#
# ## Primärschlüssel und Fremdschlüssel
#
# - Primärschlüssel werden verwendet, um jede Zeile in einer Tabelle eindeutig
#   zu identifizieren.
# - Primärschlüssel können zusammengesetzt sein
# - Fremdschlüssel werden verwendet, um Beziehungen zwischen Tabellen
#   herzustellen.
#   - Fremdschlüssel verweisen auf Primärschlüssel in einer anderen Tabelle

# %% [markdown]
#
# Table **Invoices**
#
# | invoice_no | customer_id |
# |------------|-------------|
# |         12 |           1 |
# |         13 |           2 |
#
# - `invoice_no` ist der Primärschlüssel
# - `customer_id` ist ein Fremdschlüssel, der auf die Tabelle **Kunden** verweist


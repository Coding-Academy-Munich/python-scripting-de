# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Zugriff auf Web Services</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## HTTP Requests and Responses
#
# - HTTP (Hypertext Transfer Protocol) ist die Grundlage der Datenkommunikation
#   für das World Wide Web
# - HTTP-Anfragen und -Antworten sind Nachrichten, die von Clients (z.B.
#   Webbrowsern) und Servern gesendet werden
# - HTTP-Anfragen bestehen aus einer Methode, Kopfzeilen und (manchmal) einem
#   Body
# - HTTP-Antworten bestehen aus einem Statuscode, Headern und (normalerweise)
#   einem Body


# %% [markdown]
#
# ### Häufig vorkommende Response Codes
#
# - `200 OK:` Der Server hat die Anfrage erfolgreich bearbeitet und gibt die
#   angeforderten Daten oder Ressource zurück
# - `201 Erstellt:` Die Anfrage wurde erfüllt und eine neue Ressource wurde
#   erstellt
# - `204 No Content:` Der Server hat die Anfrage erfolgreich bearbeitet, gibt
#   aber keine keinen Inhalt zurück.

# %% [markdown]
#
# - `301 Moved Permanently:` Die angeforderte Ressource wurde dauerhaft an einen
#   neuen Ort verschoben. Der Client sollte seine Lesezeichen und Verweise
#   ändern. Suchmaschinen sollen ihren Index aktualisieren
# - `302 Found` und `303 See Other:` Temporäre Umleitung. Die angeforderte
#   Ressource kann unter einer anderen URL gefunden werden, aber die Umleitung
#   ist temporär und bei zukünftigen Anfragen soll weiterhin die ursprüngliche
#   URL verwendet werden
# - "307 Temporäre Umleitung": Temporäre Umleitung. Der Client soll weiterhin
#   die ursprüngliche HTTP-Methode verwenden (z.B. `GET` oder `POST`)

# %% [markdown]
#
# - `400 Bad Request:` Der Server kann oder will die Anfrage wegen eines
#   offensichtlichen Client-Fehlers nicht bearbeiten, z.B.
#   - fehlerhafte Syntax
#   - ungültiges Request-Message-Framing
#   - irreführendes Anfrage-Routing
# - `401 Unauthorized:` Der Client muss sich authentifizieren, um die
#   angeforderte Antwort zu erhalten
# - `403 Forbidden:` Der Server weigert sich, die Anfrage zu erfüllen, weil der
#   Client keinen Zugriff auf die angeforderte Ressource hat
# - `404 Not Found:` Der Server kann die angeforderte Ressource nicht finden
# - `500 Internal Server Error:` Der Server kann die Anfrage wegen eines
#   internen Problems nicht erfüllen.


# %% [markdown]
#
# ## Einführung in Web-Services
#
# - Web Services sind Softwaresysteme, die die interoperable
#   Maschine-zu-Maschine-Interaktion über ein Netzwerk unterstützen
# - Web-Services werden oft zum Austausch von Daten zwischen verschiedenen
#   Anwendungen und Systemen verwendet
# - Web-Services können verschiedene APIs unterstützen
#   - SOAP
#   - RESTful
#   - GraphQL

# %% [markdown]
#
# ## APIs for Web Services
#
# - Eine API (Application Programming Interface) ist eine Reihe von Regeln, die
# es einer Softwareanwendung mit einer anderen zu interagieren.
# - Webservices sind eine Art von API, die Webprotokolle zur Kommunikation
#   nutzen.
# - Zu den verschiedenen Arten von APIs gehören SOAP, RESTful und GraphQL
# - RESTful APIs nutzen HTTP zum Datenaustausch und sind aufgrund ihrer
#   Einfachheit und Skalierbarkeit die beliebteste Variante
# - GraphQL APIs ermöglichen eine effizientere Datenabfrage, indem sie es den
#   Clients erlauben die Struktur der Daten, die sie benötigen, angeben
# - SOAP ist ein Protokoll für den Austausch von strukturierten Daten zwischen
#   Web Services

# %% [markdown]
#
# # RESTful APIs
#
# ## Was ist eine RESTful API?
#
# - REST steht für "Representational State Transfer" und bezieht sich auf ein
#   Design Muster für den Aufbau von Webdiensten.
# - RESTful APIs werden mit dem HTTP-Protokoll erstellt und folgen einer Reihe
#   von Architekturprinzipien, darunter Zustandslosigkeit, Cachefähigkeit und
#   eine geschichtete Systemarchitektur

# %% [markdown]
#
# ## Aufbau einer RESTful API
#
# - RESTful APIs sind um Ressourcen herum aufgebaut, die durch einen URI
#   identifiziert werden (Uniform Resource Identifier)
# - Ressourcen werden mit einer Reihe von vordefinierten Operationen oder HTTP
#   Methoden, wie `GET`, `POST`, `PUT`, `DELETE` abgerufen, erstellt,
#   modifiziert und gelöscht

# %% [markdown]
#
# ## CRUD-Operationen und HTTP-Methoden
#
# - CRUD steht für "Create, Read, Update, Delete" und bezieht sich auf die
#   Grundoperationen, die mit einer Ressource durchgeführt werden können
# - Jede CRUD-Operation entspricht einer bestimmten HTTP-Methode, zum Beispiel:
# - `GET` für das Lesen einer Ressource
# - `POST` für das Erstellen einer neuen Ressource
# - `PUT` oder `PATCH` für das Aktualisieren einer bestehenden Ressource
# - `DELETE` für das Löschen einer Ressource

# %% [markdown]
#
# ## Überlegungen zur Authentifizierung und Sicherheit
#
# - RESTful APIs können mit einer Vielzahl von Authentifizierungs- und
#   Authentifizierungs- und Autorisierungsmechanismen gesichert werden, wie
#   API-Schlüssel, OAuth und JSON Web Tokens (JWTs)
# - HTTPS (HTTP Secure) wird üblicherweise zur Verschlüsselung von Daten
#   verwendet, die zwischen Clients und Servern ausgetauscht werden, um
#   unbefugten Zugriff oder das Abfangen von Daten zu verhindern.

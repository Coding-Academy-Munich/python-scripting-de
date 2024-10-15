# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adapter</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Zweck
#
# - Anpassung der Schnittstelle einer Klasse an ein erwartetes Interface
# - Zusammenarbeit von Klassen, die aufgrund inkompatibler Schnittstellen nicht
#   zusammenarbeiten können

# %% [markdown]
#
# ## Auch bekannt als
#
# - Wrapper

# %% [markdown]
#
# ## Motivation
#
# - Nutzung einer Bibliotheks-Klasse aufgrund inkompatibler Schnittstellen nicht möglich
# - Beispiel: Grafischer Editor
#   - Grafik-Objekte sind relativ einfach zu realisieren
#   - Text ist komplexer, möglicherweise ist der Einsatz einer externen Bibliothek
#     sinnvoll
# - Die Schnittstelle dieser Bibliothek ist nicht kompatibel mit der Schnittstelle,
#   die unser Editor erwartet
# - Mit einem Adapter können wir die Schnittstelle der Bibliothek an die
#   Schnittstelle unseres Editors anpassen

# %% [markdown]
#
# <img src="img/PlantUML/adapter-example.svg"
#      style="display:block;margin:auto;width:80%"/>

# %% [markdown]
#
# ## Anwendbarkeit
#
# - Nutzung einer bestehenden Klasse mit inkompatibler Schnittstelle
# - [...]

# %% [markdown]
#
# ## Struktur
#
# - Es werden zwei Varianten definiert: Klassenadapter und Objektadapter
# - Klassenadapter verwenden Mehrfachvererbung und werden seltener eingesetzt
# - Klassendiagramm für Objektadapter:
#
# <img src="img/PlantUML/pat_adapter.svg"
#      style="display: block; margin: auto; width: 80%;"/>

# %% [markdown]
#
# ## Teilnehmer
#
# - **Client**
#   - Nutzt das Interface von Target
# - **Target**
#   - Definiert das Interface, das vom Client verwendet wird
# - **Adapter**
#   - Implementiert das Interface von Target und hält eine Referenz auf das Adaptee
# - **Adaptee**
#   - Die Klasse, deren Schnittstelle angepasst werden soll

# %% [markdown]
#
# ## Interaktionen
#
# - Der Client ruft eine Target-Methode auf einem Adapter-Objekt auf
# - Der Adapter ruft die entsprechende Methode auf dem Adaptee auf

# %% [markdown]
#
# ## Konsequenzen
#
# - Klassenadapter
#   - ...
# - Objektadapter
#   - ein Adapter kann mit mehreren adaptierten Objekten zusammenarbeiten
#   - erschwert das Überschreiben von Adaptee-Methoden

# %% [markdown]
#
# ## Weitere Konsequenzen
#
# - Anpassungsaufwand variiert je nachdem, wie unterschiedlich die Schnittstellen sind
# - Klassen mit integrierter Schnittstellenanpassung (pluggable Adapters)
# - 2-Wege-Adapter, wenn verschiedene Clients das gleiche Objekt adaptieren müssen

# %% [markdown]
#
# ## Implementierung
#
# - ...

# %% [markdown]
#
# ## Beispielcode

# %%
from abc import ABC, abstractmethod
from dataclasses import dataclass


# %%
class Employee(ABC):
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def salary(self) -> float:
        ...


# %%
@dataclass
class Company:
    employees: list[Employee]
    monthly_rent: float = 1000.0

    def monthly_expenses(self) -> float:
        return sum(employee.salary() for employee in self.employees) + self.monthly_rent


# %%
@dataclass
class LegacyEmployee:
    first_name: str
    last_name: str
    pay: float


# %%
class LegacyEmployeeAdapter(Employee):
    def __init__(self, legacy_employee: LegacyEmployee):
        self._legacy_employee = legacy_employee

    def name(self) -> str:
        return f"{self._legacy_employee.first_name} {self._legacy_employee.last_name}"

    def salary(self) -> float:
        return self._legacy_employee.pay

    def __repr__(self):
        return f"LegacyEmployee({self.name()}, {self.salary()})"


# %%
_legacy_employee_1 = LegacyEmployee("John", "Doe", 1500.0)
_employee_1 = LegacyEmployeeAdapter(_legacy_employee_1)
_employee_1


# %%
_legacy_employee_2 = LegacyEmployee("Jane", "Miller", 2000.0)
_employee_2 = LegacyEmployeeAdapter(_legacy_employee_2)
_employee_2

# %%
_company = Company([_employee_1, _employee_2])
_company

# %%
_company.monthly_expenses()


# %% [markdown]
#
# ## Praxisbeispiele
#
# - ET++ Draw
# - InterViews 2.6
# - ...

# %% [markdown]
#
# ## Verwandte Muster
#
# - Bridge: ähnliche Struktur, aber andere Absicht (Trennung von Schnittstelle und
#   Implementierung)
# - Decorator: erweitert anderes Objekt, ohne die Schnittstelle zu ändern
# - Proxy: Stellvertreter für ein Objekt, das die gleiche Schnittstelle hat

# %% [markdown]
#
# ## Python-Implementierung
#
# - Python bietet Sprachfeatures, die die Implementierung von Adaptern in manchen Fällen
#   vereinfachen können
# - Monkey Patching
#   - Methoden können nach der Definition zu einem Objekt hinzugefügt werden
# - ...

# %% [markdown]
#
# ### Monkey Patching
#
# - Methoden können nach der Definition zu einem Objekt hinzugefügt werden

# %%
def name(obj) -> str:
    return f"{obj.first_name} {obj.last_name}"


# %%
LegacyEmployee.name = name

# %%
_legacy_employee_1.name()

# %%
LegacyEmployee.salary = lambda obj: obj.pay

# %%
_legacy_employee_1.salary()

# %%
_company2 = Company([_legacy_employee_1, _legacy_employee_2])

# %%
_company2.monthly_expenses()


# %% [markdown]
#
# ## Workshop: Einheitliche Schnittstelle für einen Chat-Client
#
# In diesem Workshop soll eine einheitliche Schnittstelle für einen Chat-Client
# implementiert werden. Der Chat-Client soll mit verschiedenen Messaging-Diensten wie
# SMS, E-Mail und einem In-App-Chat-System kommunizieren können. Die Herausforderung
# besteht darin, dass jeder dieser Dienste seine eigene Art hat, Nachrichten zu senden
# und zu empfangen.
#
# Ihre Aufgabe ist es, den Adapter-Entwurf zu verwenden, um eine gemeinsame
# Kommunikationsschnittstelle für all diese Dienste zu erstellen. Auf diese Weise kann
# die Hauptanwendungslogik Nachrichten einheitlich senden und empfangen, unabhängig vom
# zugrundeliegenden Dienst, der verwendet wird.


# %% [markdown]
#
# Im Folgenden finden Sie den Startercode mit separaten Klassen für jeden
# Messaging-Dienst.
#
# Ihre Aufgabe ist es, Adapter für diese Klassen zu erstellen, damit sie von der
# Chat-Anwendung auf einheitliche Weise verwendet werden können.
#
# Bitte stellen Sie sicher, dass Ihre Lösung diese Richtlinien befolgt:
#
# - Es sollte das Adapter-Muster verwenden, um eine gemeinsame Schnittstelle für alle
#   Messaging-Dienste zu erstellen.
# - Die Schnittstelle sollte Methoden zum Senden und Empfangen von Nachrichten
#   bereitstellen.
# - Die Chat-Anwendung sollte nicht über die spezifischen Details jedes
#   Messaging-Dienstes Bescheid wissen. Stattdessen sollte sie mit allen Diensten über
#   die gemeinsame Schnittstelle interagieren.

# %% [markdown]
#
# Nachdem Sie die Adapter erstellt haben, demonstrieren Sie deren Verwendung, indem Sie
# eine Chat-Anwendung erstellen, die Nachrichten über alle verfügbaren Dienste sendet
# und empfängt. Die Anwendung sollte dies unter Verwendung der gemeinsamen Schnittstelle
# tun, ohne direkt Methoden aufzurufen, die spezifisch für jeden Dienst sind.
#
# Viel Erfolg!

# %%
class SMS:
    def __init__(self):
        self.service_name = "SMS"

    def send_text(self, number, message):
        print(f"Sending text to {number} via {self.service_name}: {message}")

    def receive_text(self, number):
        print(f"Receiving a text from {number} via {self.service_name}")


# %%
class Email:
    def __init__(self):
        self.service_name = "Email"

    def send_email(self, email_address, subject, message):
        print(
            f"Sending email to {email_address} with subject {subject!r} "
            f"via {self.service_name}: {message}"
        )

    def receive_email(self, email_address):
        print(f"Receiving an email from {email_address} via {self.service_name}")


# %%
class InAppChat:
    def __init__(self):
        self.service_name = "In-App Chat"

    def send_message(self, username, message):
        print(f"Sending message to {username} via {self.service_name}: {message}")

    def receive_message(self, username):
        print(f"Receiving a message from {username} via {self.service_name}")


# %%
from abc import ABC, abstractmethod


# %%
class MessagingAdapter(ABC):
    @abstractmethod
    def send(self, to, message):
        pass

    @abstractmethod
    def receive(self, from_):
        pass


# %%
class SMSAdapter(MessagingAdapter):
    def __init__(self, sms: SMS):
        self._sms = sms

    def send(self, to, message):
        self._sms.send_text(to, message)

    def receive(self, from_):
        self._sms.receive_text(from_)


# %%
class EmailAdapter(MessagingAdapter):
    def __init__(self, email: Email):
        self._email = email

    def send(self, to, message):
        self._email.send_email(to, "Mail from Chat App", message)

    def receive(self, from_):
        self._email.receive_email(from_)


# %%
class InAppChatAdapter(MessagingAdapter):
    def __init__(self, chat: InAppChat):
        self._chat = chat

    def send(self, to, message):
        self._chat.send_message(to, message)

    def receive(self, from_):
        self._chat.receive_message(from_)


# %%
class ChatApplication:
    def __init__(self, adapters):
        self._adapters = adapters

    def send_message(self, to, message):
        for adapter in self._adapters:
            adapter.send(to, message)

    def receive_message(self, from_):
        for adapter in self._adapters:
            adapter.receive(from_)


# %%
sms = SMS()
email = Email()
chat = InAppChat()

# %%
sms_adapter = SMSAdapter(sms)
email_adapter = EmailAdapter(email)
chat_adapter = InAppChatAdapter(chat)

# %%
chat_app = ChatApplication([sms_adapter, email_adapter, chat_adapter])

# %%
chat_app.send_message("555-1234", "Hello!")

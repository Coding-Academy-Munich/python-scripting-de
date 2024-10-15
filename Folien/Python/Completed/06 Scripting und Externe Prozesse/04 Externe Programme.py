# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Externe Programme</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Sub-Prozesse
#
# *Hinweis:* Zur Ausführung dieses Notebooks müssen muss das `ext_sample_app`
# Package (in `Examples/ExternalSampleApplication`) installiert sein.
#
# `subprocess.run` ist die bevorzugte Methode um externe Applikationen zu starten.

# %%
from pprint import pprint
from subprocess import TimeoutExpired, run

# %%
# This may not work if `python` is not in your path...
# run(["python", "--version"])

# %% [markdown]
# Mit `shutil.which()` kann man den vollständigen Pfad eines Programms herausfinden.

# %%
import shutil

# shutil.which("python")

# %%
# cp = run([shutil.which("python"), "--version"])


# %%
def print_completed_process(cp):
    print("return code:", cp.returncode)
    print("captured stdout:", repr(cp.stdout))
    print("captured stderr:", repr(cp.stderr))


# %%
# print_completed_process(cp)

# %%
# cp = run(["python", "--version"], capture_output=True, text=True)

# %%
# print_completed_process(cp)

# %% [markdown]
#
# Mit `sys.executable` kann man den Pfad des gerade aktiven Python Interpreters
# herausfinden. Das ist die bevorzugte Methode um einen Python Prozess zu
# starten.

# %%
import sys

# cp = run([sys.executable, "--version"], capture_output=True, text=True)

# %%
# print_completed_process(cp)

# %%
# cp = run([sys.executable, "-m", "ext_sample_app"], capture_output=True, text=True)

# %%
# print_completed_process(cp)

# %%
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "--help"], capture_output=True, text=True
# )

# %%
# print_completed_process(cp)

# %%
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "say-hi"], capture_output=True, text=True
# )

# %%
# print_completed_process(cp)

# %%
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "error"], capture_output=True, text=True
# )

# %%
# print_completed_process(cp)

# %%
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "print-env"],
#     capture_output=True,
#     text=True,
# )

# %%
# pprint(eval(cp.stdout, {}))

# %%
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "print-env"],
#     capture_output=True,
#     text=True,
#     env={b"MY_VAR": b"123", b"YOUR_VAR": b"123"},
# )

# %%
# pprint(eval(cp.stdout, {}))

# %%
# THIS DOES NOT WORK!
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "interact"],
#     capture_output=True, text=True
# )

# %%
# print_completed_process(cp)

# %%
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "interact"],
#     input="exit",
#     capture_output=True,
#     text=True,
# )

# %%
# print_completed_process(cp)

# %%
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "interact"],
#     input="work",
#     capture_output=True,
#     text=True,
# )

# %%
# print_completed_process(cp)

# %%
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "interact"],
#     input="do something impossible",
#     capture_output=True,
#     text=True,
# )

# %%
# print_completed_process(cp)

# %% [markdown]
# ## Popen: Nebenläufige Ausführung von Programmen
#
# Wenn man nicht warten kann, bis das gestartete Programm beendet wird muss man
# die `subprocess.Popen` Klasse verwenden:

# %%
from subprocess import Popen, PIPE
import sys

# %%
# proc = Popen(
#     [sys.executable, "-m", "ext_sample_app", "interact"],
#     stdin=PIPE,
#     stderr=PIPE,
#     stdout=PIPE,
#     encoding="utf-8",
#     universal_newlines=True,
#     bufsize=0,
# )

# %%
# type(proc)

# %% [markdown]
#
# `proc.communicate()` sendet eine Nachricht and `proc`, schließt die Ein- und
# Ausgabeströme und beendet den Prozess.

# %%
# proc.communicate("work")

# %% [markdown]
#
# Mit `proc.poll()` kann man feststellen, ob der Prozess schon beendet wurde und
# was der Rückgabewert war. Falls das Ergebnis `None` ist, ist der Prozess noch
# aktiv. `proc.wait()` wartet eine bestimmte Zeit und gibt den Rückgabewert des
# Prozesses zurück. Falls der Prozess nicht in der vorgegebenen Zeit beendet
# wurde, wird eine `TimeoutExpired` Exception ausgelöst.

# %%
# proc.poll()


# %%
def run_and_communicate(command, timeout=None):
    wait_result = None
    result = None
    proc = Popen(
        [sys.executable, "-m", "ext_sample_app", "interact"],
        stdin=PIPE,
        stderr=PIPE,
        stdout=PIPE,
        encoding="utf-8",
        universal_newlines=True,
        bufsize=0,
    )
    try:
        result = proc.communicate(command, timeout=timeout)
    except TimeoutExpired:
        print("Process did not terminate!")
        proc.terminate()
        wait_result = proc.wait(5.0)
    return result, wait_result


# %%
# run_and_communicate("exit")

# %%
# run_and_communicate("work")

# %%
# run_and_communicate("work slowly", 0.1)

# %%
# run_and_communicate("error")

# %% [markdown]
# ## Kommunikation mit Sockets
#
# Das folgende Beispiel zeigt, wie man einen Prozess starten und dann über
# Sockets mit ihm kommunizieren kann.

# %%
from subprocess import Popen, PIPE
import sys

HOST = "localhost"
PORT = 12345

# %%
from socket import socket, AF_INET, SOCK_STREAM
import sys


def send_message(msg: str):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(msg + "\n", "utf-8"))
        return str(sock.recv(1024), "utf-8")


# %%
# proc = Popen(
#     [
#         sys.executable,
#         "-m",
#         "ext_sample_app",
#         "serve",
#         "--host",
#         HOST,
#         "--port",
#         str(PORT),
#     ],
#     stdin=PIPE,
#     stderr=PIPE,
#     stdout=PIPE,
#     encoding="utf-8",
#     universal_newlines=True,
#     bufsize=0,
# )

# %%
# proc.poll()

# %%
# send_message("Hello, world!")

# %%
# send_message("Are you running?")

# %%
# proc.poll()

# %%
# proc.terminate()

# %%
# proc.poll()

# %%
# try:
#     send_message("Are you still running?")
# except ConnectionRefusedError as err:
#     print("Could not connect to server.")
#     print(err)

# %%
# proc.poll()

# %%

# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>XML</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Das XML Package
#
# Siehe [Python Dokumentation](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)

# %%
from xml.etree import ElementTree
from tempfile import NamedTemporaryFile
import os

# %%
xml_data = """\
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""

# %%
xml_file = NamedTemporaryFile(mode="w", delete=False)
xml_file.write(xml_data)
xml_file.close()

# %%
tree = ElementTree.parse(xml_file.name)

# %%
os.remove(xml_file.name)

# %%
tree

# %%
root = tree.getroot()
root

# %%
root.tag

# %%
root.attrib

# %%
for child in root:
    print(child.tag, child.attrib)

# %%
root[0]

# %%
root[0][1]

# %%
root[0][1].text

# %% [markdown]
# ## LXML
#
# [LXML](https://lxml.de/index.html) ist eine Alternative mit (möglicherweise) höherer Performanz.

# %%

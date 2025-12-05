from logic_layer.LL_api import LL_API


"""
Viewer vill sjá Lið og leikmenn
og þá bara nöfn liða
Handle leikmanns
"""

class PublicViewerUI(LL_API):
     
     def __init__(self):
          super().__init__()
          
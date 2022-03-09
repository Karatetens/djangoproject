import requests

inchikey = str(post.inchikey)
pubchem_requestmw = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/"+inchikey+"/property/MolecularWeight/json").json()
pubchem_mw = pubchem_requestmw['PropertyTable']['Properties'][0]['MolecularWeight']
pubchem_molecular_weight = str(pubchem_mw)
print(pubchem_molecular_weight)

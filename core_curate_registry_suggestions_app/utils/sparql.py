import requests
import xmltodict
from SPARQLWrapper import SPARQLWrapper, JSON
import time

sparql = SPARQLWrapper("http://dbpedia.org/sparql")


def get_abstract(uri):
    try:
        return query_sparql(uri, """dbo:abstract""", "EN")
    except:
        return ""


def get_label(uri):
    try:
        return query_sparql(uri, """rdfs:label""", "EN")
    except:
        return ""


def get_url_homepage(uri):
    try:
        return get_homepage(uri)
    except:
        return ""


def query_sparql(uri, prop, lang=None):
    filter_lang = """filter(langMatches(lang(?prop),"""  "\"" + lang + "\""  """))""" if lang is not None else ""
    sparql.setQuery("""
	    SELECT ?prop
	    WHERE { <""" + uri + """> """ + prop + """ ?prop . """ + filter_lang + """}""")
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        val = result["prop"]["value"]
        return val if val is not None else ""
    return ""


def get_date_creation(uri):
    formation_year = query_sparql(uri, """dbo:formationYear""")
    if formation_year == "":
        formation_year = query_sparql(uri, """dbo:foundingYear""")
    if formation_year == "":
        try:
            formation_year = query_sparql(uri, """dbp:date""")
            formation_year = time.strftime('%Y', time.localtime(float(formation_year)))
        except Exception as e:
            pass
    return formation_year


def get_homepage(uri):
    homepage = query_sparql(uri, """dbp:url""")
    if homepage == "":
        homepage = query_sparql(uri, """foaf:homepage""")
    if homepage == "":
        homepage = query_sparql(uri, """dbp:website""")
    return homepage


def get_entity_names(name):
    list_suggestions = {}

    r = requests.get(
        "http://lookup.dbpedia.org/api/search.asmx/KeywordSearch?QueryClass=organisation&QueryString="+ name)
    try:
        list_results = xmltodict.parse(r.content)['ArrayOfResult']['Result']
    except:
        return list_suggestions

    try:
        list_suggestions[list_results['Label']] = str(list_results['URI'])
    except:
        try:
            for result in list_results:
                list_suggestions[result['Label']] = str(result['URI'])
        except:
            pass

    return list_suggestions

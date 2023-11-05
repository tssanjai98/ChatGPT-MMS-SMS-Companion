import wikipedia

def fetch_wikipedia_content(search_term):
    try:    
        wikipedia.set_lang("en")

        search_results = wikipedia.search(search_term)

        if not search_results:
            return {'error': 'No results found'}
        
        summary = wikipedia.summary(search_results[0])
        
        return {'summary': summary}

    except wikipedia.exceptions.PageError:
        return {'error': 'Page not found'}
    except wikipedia.exceptions.DisambiguationError as e:
        return {'error': 'Disambiguation error, multiple pages found: ' + str(e.options)}
    except Exception as err:
        return {'error': str(err)}

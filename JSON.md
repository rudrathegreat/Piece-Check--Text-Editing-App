# Piece Check - Text Editing Application
## JSON Format
### What is Received

When the respons from the API is received, it is received in a format known as JSON. This JSON Format is used everywhere, esecially when there is the use of communication between applicaions via API.

### How it is Formatted

You can think of the JSON format as a format with a parent and child in a form of hierarchy. A good analogy of this is when you look at family trees. An example of a file formatted using JSON - 

```JSON

{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
```

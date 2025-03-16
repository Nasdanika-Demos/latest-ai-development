This demo mimics the [CrewAI quick start project](https://docs.crewai.com/quickstart).

It generates this documentation site and source code from a Drawio diagram using 
[semantic mapping](https://docs.nasdanika.org/core/mapping/index.html)
to the [CrewAI model](https://crew-ai.models.nasdanika.org/).

```drawio
${representations/drawio/diagram}
```

## Commands

### Save to a model
``nsd model latest-ai-development.drawio save crew.xml``

Loads a model with the [model](https://docs.nasdanika.org/nsd-cli/nsd/model/index.html) command 
and saves to a file with the chained [save](https://docs.nasdanika.org/nsd-cli/nsd/model/save/index.html) command.

### Generate documentation site

```
nsd model latest-ai-development.drawio 
html-app -r root-action.yml 
site -r=-1 -F page-template.yml docs
```

Loads a model, generates an [HTML application](https://html-app.models.nasdanika.org/index.html)
with the [html-app](https://docs.nasdanika.org/nsd-cli/nsd/model/html-app/index.html) command
and then generates this web site from it with the [site](https://docs.nasdanika.org/nsd-cli/nsd/model/html-app/site/index.html) command.


This task demonstrates use of a custom icon.

The connection to the [Reporting analyst agent](../../agents/reporting_analyst/index.html)
associates the agent with the task by [mapping](https://docs.nasdanika.org/core/mapping/index.html#source)
it to the task [agent](https://crew-ai.models.nasdanika.org/references/eClassifiers/Task/references/eStructuralFeatures/agent/index.html)
reference:

```yaml
features:
  source: agent
```

The connection from the [Research task](../research_task/index.html)
associates the agent with the task by mapping
it to the task [context](https://crew-ai.models.nasdanika.org/references/eClassifiers/Task/references/eStructuralFeatures/context/index.html)
reference:

```yaml
features:
  target: context
```